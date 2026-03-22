# SecurePass — Encrypted Password Vault

## 🧠 Overview

SecurePass is a full-stack web application designed to securely store and manage user passwords using multiple layers of encryption and authentication techniques.

Developed as a final project for CPSC 329 (Cybersecurity), the system demonstrates practical implementation of modern security principles, including **public-key encryption, hashing, and secure credential handling**.

---

## 🔐 Key Features

* 🔑 **RSA Public-Key Encryption**
  Encrypts sensitive password data using asymmetric cryptography

* 🔒 **SHA-256 Hashing with Salt**
  Secures user credentials before storage

* 🔄 **Custom Encryption Modules**
  Includes Caesar cipher and RSA-based encryption/decryption logic

* 👤 **Authentication System**
  Login and registration with secure validation

* 📦 **JSON-based Storage**
  Structured storage of user credentials and vault data

* 🌐 **REST API (Flask)**
  Backend endpoints for encryption, authentication, and data handling

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-CORS

### Security & Cryptography

* RSA Encryption
* SHA-256 (hashlib)
* Caesar Cipher

### Data Handling

* JSON storage

---

## 🏗️ System Design

The application follows a client-server architecture:

1. **Frontend Layer**
   User interface for login, registration, and vault access

2. **Backend Layer (Flask API)**
   Handles authentication, encryption, and data storage

3. **Security Layer**
   Applies hashing and encryption before storing or retrieving data

---

## 🧪 Security Features

* Passwords are never stored in plaintext
* Hashing with salt prevents rainbow table attacks
* Encryption ensures secure storage and retrieval
* Input validation protects against malformed data

---

## 📁 Project Structure

```bash
securepass/
│
├── app.py
├── users.json
├── vault_data.json
├── encryption/
│   ├── rsa.py
│   └── caesar.py
│
└── templates/
```

---

## 📚 References

This project was built using guidance from multiple sources on web security, cryptography, and Flask development.

See full citations:
👉 

---

## 📈 Future Improvements

* Replace Caesar cipher with stronger encryption methods
* Use a database instead of JSON storage
* Implement token-based authentication (JWT)
* Add HTTPS and deployment security layers

---

## 👤 Author

**Hatem Chehade**
Computer Science Student @ University of Calgary
