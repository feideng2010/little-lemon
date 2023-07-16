<#
This script is to start the backend db and the web
server
#>

# Start the backend db by running the docker-compose up -d
# with the docker-compose.yml file path ./mysql/docker-compose.yml

# Setup server name/ip, port numbers
$DB_SERVER = "127.0.0.1"
$DB_PORT = "3306"

# Start the backend db
Write-Host "Starting the backend db..."
docker-compose -f ./mysql/docker-compose.yml up -d

# wait untile the process is done
Write-Host "Waiting for the backend db to start..."
Start-Sleep -s 10

# Test DB connection setup
$connection = $false
$counter = 0

# Keep testing the connection until it is true or more than 10 times
while ($connection -eq $false -and $counter -lt 10 ) {
    $test = Test-NetConnection $DB_SERVER -Port $DB_PORT
    $connection = $test.TcpTestSucceeded
    Write-Host "Waiting for the backend db to start..."
    Start-Sleep -s 3
}

# Start the web server by running 'python manage.py runserver'
# if the connection is true
if ($connection -eq $true) {
    Write-Host "Starting the web server..."
    python manage.py runserver
}
else {
    Write-Host "Failed to start the database server..."
    Write-Host "Failed to start the web server..."
}


