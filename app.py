from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return jsonify({"message": "Hello, this is Password Vault API"})

@app.route('/generate-password', methods = ['POST'])
def generate_password():
    data = request.get_json()
    length = data['length']
    service = data['service']
    print(length, service)
    return jsonify({"length": length, "service": service})


if __name__ == '__main__':
    app.run(debug=True)
