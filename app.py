import string
import random
import datetime
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

#function generating password py-json-py
def generate_password():

    data = request.get_json()#fetching json data

    if not data or 'length' not in data or 'service' not in data:
         return jsonify({"error": "Provide 'length' and 'service'"}), 400 #sending data as json
    
    length = data['length']
    service = data['service']
    
    if not isinstance(length, int) or length < 5:
         return jsonify({"error": "Length must be a number bigger than 4"}), 400

    password = pass_gen(length)#passing length to randomizer

    return jsonify({"status": "success", "password": password}), 201 #showing user pass

if __name__ == '__main__':
    app.run(debug=True)
