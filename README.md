# Password Vault API (Flask)

Password Vault is a simple backend API built with Python and Flask. It allows you to generate secure, random passwords, encrypt and store them, and retrieve previously saved passwords — all with token-based authorization.

## Features

- Generate pseudo-random secure passwords
- Encrypt passwords using `cryptography.Fernet`
- Save to file with timestamp and service name
- Retrieve stored passwords (decrypted) via API
- Token-based access control
- Clean JSON API responses
- Easily extendable (database, user auth, frontend)

## API Endpoints

### `POST /generate-password`

Generates a new password, encrypts it, and saves it to file.

#### JSON Body:

{
  "length": 12,
  "service": "Gmail"
}

#### Response:

{
  "status": "success",
  "Time": "2025-04-15 21:37",
  "password": "R@p3z!kfJ6wQ",
  "service": "Gmail"
}

###  'GET /get-passwords'

Returns all previously saved passwords — requires authorization header.

####  Required Header:

Authorization: Bearer supersecret1234

#### Response:

{
  "Your data": [
    {
      "timestamp": "2025-04-15 21:37",
      "service": "Gmail",
      "password": "R@p3z!kfJ6wQ"
    }
  ]
}

##  How to Run

###  Install dependencies:

pip install -r requirements.txt

### Run the server:

python app.py

### API will be running at:

http://127.0.0.1:5000


## Project Structure

- app.py – Flask server with all routes

- key.key – encryption key file (auto-generated)

- my_passwords.txt – log of encrypted passwords

- requirements.txt – list of required packages

##

###  Educational project by Jakub JKoder — learning backend development with Python and Flask.
