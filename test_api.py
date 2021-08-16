import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy


from app import create_app

DEVELOPER_ALICE_AUTH_HEADERS = {
    'Authorization': os.environ['DEVELOPER_ALICE_TOKEN'],
    'Content-Type': 'application/json'
}

DEVELOPER_BOB_AUTH_HEADERS = {
    'Authorization': os.environ['DEVELOPER_BOB_TOKEN'],
    'Content-Type': 'application/json'
}

MANAGER_AUTH_HEADERS = {
    'Authorization': os.environ['MANAGER_TOKEN'],
    'Content-Type': 'application/json'
}

INVALID_TOKEN_HEADERS = {
    'Authorization': 'Bearer PINO',
    'Content-Type': 'application/json'
}


class GrandPrixTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_healthy(self):
        res = self.client().get('/healthy')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['healthy'], True)

    def test_unauthenticated_401(self):
        res = self.client().get('/dashboard')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header missing.')

    def test_unauthorized_403(self):
        res = self.client().delete(
            '/resources/1',
            headers=DEVELOPER_ALICE_AUTH_HEADERS
            )
        self.assertEqual(res.status_code, 403)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 403)
        self.assertEqual(
            data['message'],
            'The user doesn\'t have the required permission')

    def test_invalid_token_400(self):
        res = self.client().get('/developers', headers=INVALID_TOKEN_HEADERS)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(
            data['message'],
            'Unable to parse authentication token.')

    def test_get_dashboard_successful(self):
        res = self.client().get(
            '/dashboard',
            headers=DEVELOPER_ALICE_AUTH_HEADERS
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(data), list)

    def test_get_dashboart_401(self):
        res = self.client().get('/dashboard')
        self.assertEqual(res.status_code, 401)

    def test_get_resources_successful(self):
        res = self.client().get(
            '/resources',
            headers=DEVELOPER_ALICE_AUTH_HEADERS
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(data), list)

    def test_get_resources_401(self):
        res = self.client().get('/resources')
        self.assertEqual(res.status_code, 401)

    def test_patch_resource_successful(self):
        res = self.client().patch('/resources/1', data=json.dumps({
            "name": "renamed"
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['name'], 'renamed')

    def test_patch_resource_404(self):
        res = self.client().patch('/resources/100', data=json.dumps({
            "name": "404 anyeay"
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 404)

    def test_patch_resource_403(self):
        res = self.client().patch('/resources/1', data=json.dumps({
            "name": "403 anyway"
        }), headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_post_resource_successful(self):
        res = self.client().post('/resources', data=json.dumps({
            "name": "New resource",
            "note": None,
            "img_url": None
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['name'], 'New resource')
        self.assertIsNotNone(data['id'])

    def test_post_resource_403(self):
        res = self.client().post('/resources', data=json.dumps({
            "name": "New resource",
            "note": None,
            "img_url": None
        }), headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_post_resource_422(self):
        res = self.client().post('/resources', data=json.dumps({
            "name_misspelled": "New resource",
            "note": 42,
            "img_url": None
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 422)

    def test_delete_resource_successful(self):
        res = self.client().delete(
            '/resources/4',
            headers=MANAGER_AUTH_HEADERS
            )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['deleted_id'], 4)

    def test_delete_resource_403(self):
        res = self.client().delete(
            '/resources/4',
            headers=DEVELOPER_ALICE_AUTH_HEADERS
            )
        self.assertEqual(res.status_code, 403)

    def test_delete_resource_404(self):
        res = self.client().delete(
            '/resources/100',
            headers=MANAGER_AUTH_HEADERS
            )
        self.assertEqual(res.status_code, 404)

    def test_get_developers_successful(self):
        res = self.client().get(
            '/developers',
            headers=MANAGER_AUTH_HEADERS
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(data), list)

    def test_get_developers_403(self):
        res = self.client().get(
            '/developers',
            headers=DEVELOPER_BOB_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_post_developer_successful(self):
        res = self.client().post('/developers', data=json.dumps({
            "full_name": "A new developer",
            "username": "A sub from auth0"
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['full_name'], 'A new developer')
        self.assertEqual(data['username'], "A sub from auth0")
        self.assertIsNotNone(data['id'])

    def test_post_developer_403(self):
        res = self.client().post('/developers', data=json.dumps({
            "full_name": "A new developer",
            "username": "A sub from auth0"
        }), headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_post_developer_422(self):
        res = self.client().post('/developers', data=json.dumps({
            "full_name": "A new developer",
            "username": None
        }), headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 422)

    def test_delete_developer_successful(self):
        res = self.client().delete(
            '/developers/5',
            headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['deleted_id'], 5)

    def test_delete_developer_403(self):
        res = self.client().delete(
            '/developers/5',
            headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_delete_developer_404(self):
        res = self.client().delete(
            '/developers/100',
            headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 404)

    def test_get_bookings_successful(self):
        res = self.client().get(
            '/bookings',
            headers=DEVELOPER_BOB_AUTH_HEADERS)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(data), list)

    def test_get_bookings_401(self):
        res = self.client().get('/bookings')
        self.assertEqual(res.status_code, 401)

    def test_post_booking_successful(self):
        res = self.client().post('/bookings', data=json.dumps({
            "resource_id": 5,
            "expected_duration_hours": 2
        }), headers=DEVELOPER_BOB_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['developer_id'], 4)
        self.assertEqual(data['resource_id'], 5)
        self.assertIsNotNone(data['start_time'])
        self.assertEqual(data['expected_duration_hours'], 2)

    def test_post_booking_401(self):
        res = self.client().post('/bookings', data=json.dumps({}))
        self.assertEqual(res.status_code, 401)

    def test_post_booking_422_missing_fields(self):
        res = self.client().post('/bookings', data=json.dumps({
            "expected_duration_hours": 2
        }), headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 422)

    def test_post_booking_422_already_booked(self):
        res = self.client().post('/bookings', data=json.dumps({
            "resource_id": 1,
            "expected_duration_hours": 2
        }), headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 422)

    def test_developer_delete_own_booking_successful(self):
        res = self.client().delete(
            '/bookings/3',
            headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['deleted_id'], 3)

    def test_developer_delete_other_developer_booking_403(self):
        res = self.client().delete(
            '/bookings/4',
            headers=DEVELOPER_ALICE_AUTH_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_manager_delete_other_developer_booking_successfull(self):
        res = self.client().delete('/bookings/5', headers=MANAGER_AUTH_HEADERS)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['deleted_id'], 5)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
