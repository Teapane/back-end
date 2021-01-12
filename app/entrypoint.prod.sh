#!/bin/sh

if [ "$DATABASE" = "heroku-postgresql" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"
