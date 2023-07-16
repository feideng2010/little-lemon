#!/bin/bash

# Start the backend db by running the docker-compose up -d
# with the docker-compose.yml file path ./mysql/docker-compose.yml

# Setup server name/ip, port numbers
DB_SERVER="127.0.0.1"
DB_PORT="3306"

# Start the backend db
echo "Starting the backend db..."
docker-compose -f ./mysql/docker-compose.yml up -d

# Wait until the process is done
echo "Waiting for the backend db to start..."
sleep 10

# Test DB connection setup
connection=false
counter=0

# Keep testing the connection until it is true or more than 10 times
while [ "$connection" = false ] && [ "$counter" -lt 10 ]; do
    # connection equals to result of nc -z -w 3 $DB_SERVER $DB_PORT
    if nc -z -w 3 "$DB_SERVER" "$DB_PORT"; then
        connection=true
    fi
    echo "Waiting for the backend db to start..."
    sleep 3
    ((counter++))
done

# Start the web server by running "python manage.py runserver" if the connection is true
if [ "$connection" = true ]; then
    echo "Starting the web server..."
    python3 manage.py runserver
else
    echo "Failed to start the database server..."
    echo "Failed to start the web server..."
fi