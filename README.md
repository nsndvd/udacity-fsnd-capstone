# Grand Prix

*Grand prix* is a resource booking system for a software company.

There are two user roles, `developer` and `manager`.
Developers can book shared resources for themselves. Developers can always book a free resources, and can always release a resource that they own.
Managers can always free resources for everybody. Managers can also configure resources and users.

## Backend instructions
- navigate to the `backend` folder
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

## Running backend tests instructions
- navigate to the `backend` folder
- run `pytest test_api.py`
