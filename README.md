# Grand Prix

*Grand prix* is a resource booking system for a software company.

## Motivation

Our remote team is sharing some `resource`s in the office. We need a system to list available resources, and to give `developer`s a way to `book` these resources when they start working with them. Each developer can book many resources, but one resource can be booked by only one developer at a time. `Managers` can decide to cancel a booking that belongs to some other developer. Normal developers can only cancel their own bookings.

The name, `grandprix`, is due to the fact that normally our resources are named after companies involved in car races.

## Roles

There are two user roles, `developer` and `manager`.
Developers can book shared resources for themselves. Developers can always book a free resources, and can always release a resource that they own.
Managers can always free resources, no matter who booked them. Managers can also configure resources and developers.

More in detail, here are the list of permissions:
### Developer:
- `delete:own_bookings` Delete only the bookings that belong to the same user
- `get:bookings` Get existing bookings
- `get:developers` Show existing developers
- `get:resources` Show existing resources
- `post:bookings` Create new bookings
### Manager:
- `delete:all_bookings` Delete all bookings, no matter who they belong to
- `delete:developers` Delete an existing developer
- `delete:own_bookings` Delete only the bookings that belong to the - same user
- `delete:resources` Delete an existing resource
- `get:bookings` Get existing bookings
- `get:developers` Show existing developers
- `get:resources` Show existing resources
- `patch:resources` Edit an existing resource
- `post:bookings` Create new bookings
- `post:developers` Create new developers
- `post:resources` Create new resources

# Heroku

The API is exposed on Heroku at `https://bigpreybirds-grandprix.herokuapp.com`

## How to deploy
```
git remote add heroku https://git.heroku.com/bigpreybirds-grandprix.git
git push heroku master
```

# Backend instructions for running locally
- make sure to run at least `python 3.7`
- install python dependences with `pip install requirements.txt`
- Create a psql database and user named `grandprix`. Make sure the user has access rights for the database. In psql console:
    - `CREATE DATABASE grandprix;`
    - `CREATE USER grandprix WITH PASSWORD 'grandprix';`;
    - `GRANT ALL PRIVILEGES ON DATABASE 'grandprix' to grandprix;`
- Run `flask db upgrade` to setup the database
- Run `export FLASK_APP=app.py`
- Run `flask run --reload`

# Frontend instructions
- navigate to `frontend` folder
- run `npm install` (you need node and npm)
- run `ng serve`
- open your browser on http://localhost:4200
- to connect to a local backend, change the endpoint in the environments.ts file (default is heroku)

# Running backend tests instructions
In psql console:
- `CREATE DATABASE grandprix;`
- `CREATE USER grandprix WITH PASSWORD 'grandprix';`;
- `GRANT ALL PRIVILEGES ON DATABASE 'grandprix' to grandprix;`

then in console:
- `psql -U grandprix grandprix < test.pgsql`
- `python3 test_api.py`

A Postman collection is also present, but it's just a partial implementation. All endpoints and roles are tested in unittests.

# Auth0

Domain: `nsndvd.eu.auth0.com`

ClientId: `ttMrqpym89t5HC5oiA93YYvoi2XFXoyM`

Secret: `Npn2jdmPJnxRnu_OzayDhl7LFTcJ59HT3ukO53B9FMfCfh5RbwAjedEq-JKbMB1p`

## Ready Users

The following users are fully configured on the instance that is running on Heroku, and on the tests.

If new users are created, it's important to note that a new entry must be created in the Users table and the `username` must be set to the value of the `sub` contained in the Authorization token. This value is also displayed in the frontend, after login, just below the page title, in the form `User:<sub>`.
It's also important to note that only users with the role `manager` can create suche entries.

- Manager user
    - Role: `Manager`
    - email: `davide.ensini+manager@gmail.com`
    - password: `helloUdacityR3vi3wer`

- Developer Alice user
    - Role: `Developer`
    - email: `davide.ensini+developeralice@gmail.com`
    - password: `helloUdacityR3vi3wer`

- Developer Bob user
    - Role: `Developer`
    - email: `davide.ensini+developerbob@gmail.com`
    - password: `helloUdacityR3vi3wer`

# API Endpoints

### GET '/healthy'
`curl -X GET http://{{host}}/healthy -H "Content-Type: application/json"`
- Authorization: `public`
- Checks if the APIs are alive
- Returns: A JSON containing `{healthy: true}`

### GET '/resources'
`curl -X GET http://{{host}}/resources  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `get:resources`
- Fetches the available resources
- Returns: A JSON list containing the available resources.

### POST '/resources/'
`curl -d '{"name": "The resource name", "note": "Some notes about the resourc", "img_url": "The url for this resource"}' -X POST http://{{host}}/resources  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `post:resources`
- Adds a new resource
- Payload: a JSON representation of the resource to be added.
- Returns: A JSON object representing the added resource.

### PATCH '/resources/<int:resource_id>'
`curl -d '{"name": "The resource name", "note": "Some notes about the resourc", "img_url": "The url for this resource"}' -X PATCH http://{{host}}/resources/{{resource_id}}  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `patch:resources`
- Edits an existing resource
- Argument: the id for the resource to be edited
- Payload: the fields to be edited, with their new value
- Returns: A JSON object representing the modified resource.

### DELETE '/resources/<int:resource_id>'
`curl -X DELETE http://{{host}}/resources/{{resource_id}}  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `delete:resources`
- Deletes an existing resource
- Argument: the id for the resource to be deleted
- Returns: A JSON object containing `{deleted_id=<resource_id>}`

### GET '/developers/'
`curl -X GET http://{{host}}/deveolpers/ -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `get:developers`
- Fetches the existing developers
- Returns: A JSON list of the esisting developers

### POST '/developers/'
`curl -d '{"full_name": "The developer name", "username": "the developer sub from Auth0"}' -X POST http://{{host}}/developers  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `post:developers`
- Adds a new developer
- Payload: a JSON representation of the developer to be added.
- Returns: A JSON object representing the added developer.

### DELETE '/developers/<int:developer_id>'
`curl -X DELETE http://{{host}}/developers/{{developer_id}}  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `delete:developers`
- Deletes an existing developer
- Argument: the id for the developer to be deleted
- Returns: A JSON object containing `{deleted_id=<developer_id>}`

### GET '/bookings/'
`curl -X GET http://{{host}}/bookings/ -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `get:bookings`
- Fetches the existing bookings
- Returns: A JSON list of the esisting bookings

### POST '/bookings/'
`curl -d '{"resource_id": <resource_id>, expected_duration_hours: <expected_hours>}' -X POST http://{{host}}/bookings  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `post:bookings`
- Adds a new booking, that is associated to the developer who is currently logged in. The Authorization token is here used for recognizing the developer.
- Payload: a JSON representation of the booking to be added.
- Returns: A JSON object representing the added booking.

### DELETE '/bookings/<int:booking_id>'
`curl -X DELETE http://{{host}}/bookings/{{booking_id}}  -H "Content-Type: application/json" -H "Authorization: Bearer {{user token}}"`
- Authorization: requires permission `delete:own_booking` if deleting an own permission, or `delete:all_bookings` if deleting somebody else's booking.
- Deletes an existing booking
- Argument: the id for the booking to be deleted
- Returns: A JSON object containing `{deleted_id=<booking_id>}`
