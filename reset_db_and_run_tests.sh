#/bin/bash
set -e
dropdb grandprix --if-exists
createdb grandprix
psql -U grandprix grandprix < test.pgsql
python3 test_api.py
