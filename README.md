# Grand Prix

*Grand prix* is a resource booking system for a software company.

## Motivation

Our remote team is sharing some `resource`s in the office. We need a system to list available resources, and to give `developer`s a way to `book` these resources when they start working with them. Each developer can book many resources, but one resource can be booked by only one developer at a time. `Managers` can decide to cancel a booking that belongs to some other developer. Normal developers can only cancel their own bookings.

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