import string
import random
import datetime
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

#pseudo-random password
def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))

@app.route('/', methods = ['GET'])
def home():
    return jsonify({"message": "Hello, this is Password Vault API"})

@app.route('/generate-password', methods = ['POST'])
def generate_password():
    data = request.get_json()

    if not data or 'length' not in data or 'service' not in data:
         return jsonify({"error": "Provide 'length' and 'service'"})
    else:
        length = data['length']
        service = data['service']
        print(length, service)
        return jsonify({"length": length, "service": service})


if __name__ == '__main__':
    app.run(debug=True)
