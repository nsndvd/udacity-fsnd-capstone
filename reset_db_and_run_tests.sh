#/bin/bash
set -e
dropdb grandprix
createdb grandprix
psql -U grandprix grandprix < test.pgsql
python3 test_api.py
