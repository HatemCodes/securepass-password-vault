from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, session
from flask_cors import CORS
import CredentialProcess as CP
from flask import render_template, request
from app.crypto import caesar, rsa
from app.utils.json_storage import generate_id, load_vault, save_vault

# Caesar cipher helper functions
def encrypt_value(text):
    return caesar.encrypt(text, 3)  # Caesar shift encryption with fixed shift

def decrypt_value(text):
    return caesar.decrypt(text, 3)  # Caesar shift decryption with fixed shift

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
CORS(app, supports_credentials=True)

# Globals to store session state (temporary)
uname = ""
pwd = ""

# Route: Main page
@app.route('/')
@app.route('/base.html')
def mainpage():
    return render_template('templates/base.html')

# Route: Dashboard page
@app.route('/dashboard.html')
def dashboard():
    return render_template('templates/pm/dashboard.html', username = uname)

# Route: Service page
@app.route('/service.html')
def service():
    return render_template('templates/pm/service.html')

# Route: Login page
@app.route('/login.html')
def login():
    return render_template('templates/auth/login.html')

# Route: Register page
@app.route('/register.html')
def register():
    return render_template('templates/auth/register.html')

# Route: Caesar cipher tool page
@app.route('/caesar.html', methods=["GET", "POST"])
def caesar_page():
    result = None
    if request.method == "POST":
        text = request.form.get("text")
        shift = int(request.form.get("shift", 0))
        action = request.form.get("action")

        if action == "encrypt":
            result = caesar.encrypt(text, shift)
        elif action == "decrypt":
            result = caesar.decrypt(text, shift)

    return render_template('templates/crypto/caesar.html', result=result)

# API route: Caesar cipher encryption/decryption
@app.route('/caesar', methods=["POST"])
def caesar_api():
    data = request.get_json()
    text = data.get("text")
    shift = int(data.get("shift", 0))
    mode = data.get("mode")

    if not text or mode not in ("encrypt", "decrypt"):
        return jsonify({"error": "Invalid input"}), 400

    if mode == "encrypt":
        result = caesar.encrypt(text, shift)
    else:
        result = caesar.decrypt(text, shift)

    return jsonify({"result": result})

# Route: Frequency analysis tool page
@app.route('/frequency.html')
def frequency():
    return render_template('templates/crypto/frequency.html')

# Route: RSA encryption/decryption page
@app.route('/rsa.html', methods=["GET", "POST"])
def rsa_page():
    result = None
    keys = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            keys = rsa.generate_keys()
        elif action == "encrypt":
            text = request.form.get("text")
            n = int(request.form.get("n"))
            e = int(request.form.get("e"))
            result = rsa.encrypt(text, (n, e))
        elif action == "decrypt":
            text = request.form.get("text")
            n = int(request.form.get("n"))
            d = int(request.form.get("d"))
            result = rsa.decrypt(eval(text), (n, d))  # Eval used for ciphertext list

    return render_template('templates/crypto/rsa.html', result=result, keys=keys)

# Route: Crypto tools page
@app.route('/tools.html')
def tools():
    return render_template('templates/crypto/tools.html')

# Route: Vault frontend page
@app.route('/vault.html')
def vault():
    return render_template('templates/pm/vault.html')

# API route: Get vault data
@app.route('/vault', methods=['GET'])
def get_vault():
    global uname
    entries = load_vault()
    user_entries = [
        {
            "id": e["id"],
            "service": e["service"],
            "username": decrypt_value(e["username"]),
            "password": decrypt_value(e["password"])
        }
        for e in entries if e["vault_owner"] == uname
    ]
    return jsonify(user_entries)

# API route: Add a new service to vault
@app.route('/vault', methods=['POST'])
def add_to_vault():
    global uname
    data = request.get_json()
    service = data.get("service")
    service_login_username = data.get("username")
    password = data.get("password")

    if not service or not service_login_username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    entries = load_vault()
    new_entry = {
        "id": generate_id(entries),
        "vault_owner": uname,
        "service": service,
        "username": encrypt_value(service_login_username),
        "password": encrypt_value(password)
    }

    entries.append(new_entry)
    save_vault(entries)

    return jsonify({"message": "Service saved"}), 201

# API route: Delete a service from vault
@app.route('/vault/<int:id>', methods=['DELETE'])
def delete_service(id):
    entries = load_vault()
    new_entries = [e for e in entries if e["id"] != id]

    if len(entries) == len(new_entries):
        return jsonify({"error": "Service not found"}), 404

    save_vault(new_entries)
    return jsonify({"message": "Service deleted"}), 200

# API route: Update/edit a vault entry
@app.route('/vault/<int:id>', methods=['PUT'])
def update_service(id):
    data = request.get_json()
    entries = load_vault()
    updated = False

    for e in entries:
        if e["id"] == id:
            e["service"] = data.get("service", e["service"])
            if "username" in data:
                e["username"] = encrypt_value(data["username"])
            if "password" in data:
                e["password"] = encrypt_value(data["password"])
            updated = True
            break

    if not updated:
        return jsonify({"error": "Service not found"}), 404

    save_vault(entries)
    return jsonify({"message": "Service updated"}), 200

# API route: Register new user
@app.route('/register', methods = ['POST'])
def RegisterUser():
    global uname
    global pwd
    data = request.json
    username, password = data.get('username'), data.get('password')

    uname = username
    pwd = password

    # Check if username already exists
    hashed_username = CP.hash_with_fixed_salt(username)
    if CP.get_user_credentials_password(hashed_username) is not None:
        return make_response(jsonify({
            "message": "Username already taken. Please choose another one."
        }), 400)

    # Store credentials
    CP.store_user_credentials(username=uname, password=pwd)

    # Return success with redirect info
    response = make_response(jsonify({
        "message": "Register successful, you will be redirected to the dashboard",
        "redirect_url": url_for('dashboard')
    })), 200

    return response

# API route: Login process
@app.route('/login', methods=['POST'])
def LoginProcess():
    global uname
    data = request.json
    username, password = data.get("uname"), data.get("password")

    print(username)
    print(password)

    passwordBackend = CP.get_user_credentials_password(hashed_username=CP.hash_with_fixed_salt(value=username))
    if CP.hash_with_fixed_salt(password) == passwordBackend:
        uname = username
        response = make_response(jsonify({
            "message": "Login successful, you will be redirected to dashboard page",
            "redirect_url": url_for('dashboard')
        })), 200

        return response

    else:
        return jsonify({
            "error": "Invalid credentials!"
        }), 401

# Run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
