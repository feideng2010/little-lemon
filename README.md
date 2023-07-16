
# Pre requirements

- Docker
- Python 3.11

# Install require packages

`pip install -r requirements.txt`

# To Start

Under the project directory

for windows with PowerShell run:
`.\start.ps1`

for linux with bash run:
`./start.sh`

## EndPoints

### User End Points

#### Create User

- auth/users/ (POST)

#### Obtain Token

- auth/token/login/ (POST)

#### Alter Link for Obtain Token

- api-token-auth/ (POST)

#### Current User

- auth/users/me

### Menu End Points

#### Menu List

- api/menu/ (GET)

#### Single Menu Item

- api/menu/{id} (GET)

### Booking End Points

#### Booking List

- restaurant/booking/tables/ (GET)

#### Booking Create

- restaurant/booking/tables/ (POST)
