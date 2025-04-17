import string
import random
import datetime
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

#pseudo-random password
def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))

#default path
@app.route('/', methods = ['GET'])
def home():
    return jsonify({"message": "Hello, this is Password Vault API"})

#path with post method (will not work like default)
@app.route('/generate-password', methods = ['POST'])

#function that writes key one time
def load_create_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:  
            key_file.write(key)
        return key


#function generating password py-json-py
def generate_password():
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    data = request.get_json()#fetching json data

    if not data or 'length' not in data or 'service' not in data:
         return jsonify({"error": "Provide 'length' and 'service'"}), 400 #sending data as json
    
    length = data['length']
    service = data['service']
    
    if not isinstance(length, int) or length < 5:
         return jsonify({"error": "Length must be a number bigger than 4"}), 400

    password = pass_gen(length)#passing length to randomizer

    key = load_create_key()#creating or using existing key
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())#encrypting password

    with open("my_passwords.txt", "a") as file:
        file.write(f"{current_time} | {service} | {encrypted_password}\n")

    return jsonify({"status": "success", "Time": current_time, "password": password, "service": service}), 201 #showing user pass


AUTH_TOKEN = "supersecret1234"

#authorization and pass dump
@app.route('/get-passwords', methods = ['GET'])

def get_passwords():
    token = request.headers.get("Authorization")
    
    if token != f"Bearer {AUTH_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    
    key = load_create_key()#creating or using existing key
    cipher = Fernet(key)
    passwords = []

    with open("my_passwords.txt", "r") as file:
        for line in file:    
            wordlist = line.strip().split(' | ')#splitting words into array
            if len(wordlist) == 3:
                timestamp, service, encrypted = wordlist
                decrypted_password = cipher.decrypt(encrypted.encode()).decode()#decrypting password      
                passwords.append({
                    "timestamp": timestamp,
                    "service": service,
                    "password": decrypted_password
                })
    

    return jsonify({"Your data": passwords}), 200 #showing user pass    

if __name__ == '__main__':
    app.run(debug=True)
