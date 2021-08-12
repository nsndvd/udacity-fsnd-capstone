# Grand Prix

*Grand prix* is a resource booking system for a software company.

There are two user roles, `developer` and `manager`.
Developers can book shared resources for themselves. Developers can always book a free resources, and can always release a resource that they own.
Managers can always free resources for everybody. Managers can also configure resources and users.

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

## Backend instructions for running locally
- make sure to run at least `python 3.7`
- install python dependences with `pip install requirements.txt`
- Create a psql database and user named `grandprix`. Make sure the user has access rights for the database. In psql console:
    - `CREATE DATABASE grandprix;`
    - `CREATE USER grandprix WITH PASSWORD 'grandprix';`;
    - `GRANT ALL PRIVILEGES ON DATABASE 'grandprix' to grandprix;`
- Run `flask db upgrade` to setup the database
- Run `export FLASK_APP=app.py`
- Run `flask run --reload`

## Frontend instructions
- navigate to `frontend` folder
- run `npm install` (you need node and npm)
- run `ng serve`
- open your browser on http://localhost:4200
- to connect to a local backend, change the endpoint in the environments.ts file (default is heroku)

## Running backend tests instructions
- run `pytest test_api.py`
