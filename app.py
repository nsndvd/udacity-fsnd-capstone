from auth import check_permissions, get_sub, requires_auth
from logging import error
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from model import Developer, Booking, Resource, db


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/healthy')
    def route_healthy():
        return jsonify({'healthy': True})

    @app.route('/bookings')
    @requires_auth(permission="get:bookings")
    def get_bookings(token):
        bookings = Booking.query.all()
        return jsonify([r.format() for r in bookings])

    @app.route('/bookings', methods=['POST'])
    @requires_auth(permission="post:bookings")
    def post_bookings(auth_payload):
        body = request.get_json()
        try:

            # find the current user
            auth_sub = get_sub(auth_payload)
            user = Developer.query.filter(
                Developer.username == auth_sub).one_or_none()
            if user is None:
                abort(404)

            # fail if the resource is booked already
            booking_for_same_resource = Booking.query.filter(
                Booking.resource_id == body.get("resource_id")).one_or_none()
            if booking_for_same_resource is not None:
                abort(400)

            # create the booking
            new_booking = Booking()
            new_booking.developer_id = user.id
            new_booking.resource_id = body.get("resource_id")
            new_booking.expected_duration_hours = body.get(
                "expected_duration_hours")
            new_booking.insert_or_update()
            return jsonify(new_booking.format())

        except Exception as error:
            print(error)
            abort(422)

    @app.route('/bookings/<int:booking_id>', methods=['DELETE'])
    @requires_auth()  # No explicit permission here, finer control is required
    def delete_booking(auth_payload, booking_id):

        booking = Booking.query.filter(Booking.id == booking_id).one_or_none()

        # find the current user
        auth_sub = get_sub(auth_payload)
        user = Developer.query.filter(
            Developer.username == auth_sub).one_or_none()
        if user is None:
            abort(404)

        if not (
            (
                # user wants to delete their own permission and they can
                booking.developer_id == user.id and
                'delete:own_bookings' in auth_payload[
                    'permissions']
            )
            or (
                # user wants to somebody else's permission and they can
                'delete:all_bookings' in auth_payload['permissions']
            )
        ):
            abort(403)

        try:
            booking.delete()
            return jsonify({
                "deleted_id": booking_id
            })
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/resources')
    @requires_auth(permission="get:resources")
    def get_resources(auth_payload):
        resources = Resource.query.all()
        return jsonify([r.format() for r in resources])

    @app.route('/resources', methods=["POST"])
    @requires_auth(permission='post:resources')
    def post_resource(auth_payload):
        body = request.get_json()
        try:
            new_resource = Resource()
            new_resource.img_url = body.get("img_url")
            new_resource.name = body.get("name")
            new_resource.note = body.get("note")
            new_resource.insert_or_update()
            return jsonify(new_resource.format())
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/resources/<int:resource_id>', methods=["DELETE"])
    @requires_auth(permission='delete:resources')
    def delete_resource(auth_payload, resource_id):
        resource = Resource.query.filter(
            Resource.id == resource_id).one_or_none()
        if resource is None:
            abort(404)

        try:
            resource.delete()
            return(jsonify({
                "deleted_id": resource_id
            }))
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/resources/<int:resource_id>', methods=["PATCH"])
    @requires_auth(permission='post:resources')
    def patch_resource(auth_payload, resource_id):
        body = request.get_json()
        resource = Resource.query.filter(
            Resource.id == resource_id).one_or_none()
        if resource is None:
            abort(404)

        try:
            resource.img_url = body.get("img_url") or resource.img_url
            resource.name = body.get("name") or resource.name
            resource.note = body.get("note") or resource.note
            resource.insert_or_update()
            return jsonify(resource.format())
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/developers')
    @requires_auth(permission='get:developers')
    def get_developers(auth_payload):
        developers = Developer.query.all()
        return jsonify([r.format() for r in developers])

    @app.route('/developers', methods=["POST"])
    @requires_auth(permission='post:developers')
    def post_developers(auth_payload):
        body = request.get_json()
        try:
            new_developer = Developer()
            new_developer.full_name = body.get("full_name")
            new_developer.username = body.get("username")
            new_developer.insert_or_update()
            return jsonify(new_developer.format())
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/developers/<int:developer_id>', methods=['DELETE'])
    @requires_auth(permission='delete:developers')
    def delete_developers(auth_payload, developer_id):
        developer = Developer.query.filter(
            Developer.id == developer_id).one_or_none()
        if developer is None:
            abort(404)

        try:
            developer.delete()
            return(jsonify({
                "deleted_id": developer_id
            }))
        except Exception as error:
            print(error)
            abort(422)

    @app.route('/dashboard')
    @requires_auth(permission='get:resources')
    def get_dashboard(auth_payload):

        res = db.session.query(
            Resource,
            Booking.id,
            Booking.start_time,
            Booking.expected_duration_hours,
            Developer.full_name,
            Developer.username
        ).outerjoin(
            Booking, Resource.id == Booking.resource_id
        ).outerjoin(
            Developer, Developer.id == Booking.developer_id
        ).all()

        try:
            return jsonify([
                {
                    "resource": a[0].format(),
                    "booking": {
                        "id": a[1],
                        "start_time": a[2],
                        "expected_duration_hours": a[3]
                    } if a[1] is not None else None,
                    "developer": {
                        "name": a[4],
                        "sub": a[5]
                    } if a[4] is not None else None
                } for a in res
            ]
            )
        except Exception as error:
            print(error)
            abort(422)

    # HANDLERS

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "error": 422,
            "message": "Unprocessable data, something is wrong"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": 400,
            "message": error.description or "Bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "error": 401,
            "message": error.description or 'Unauthorized'
        }), 401

    @app.errorhandler(403)
    def not_allowed(error):
        return jsonify({
            "error": 403,
            "message": error.description or 'User not allowed'
        }), 403

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "error": 500,
            "message": "Whoops we did it wrong. Sorry!"
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
