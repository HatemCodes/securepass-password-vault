# 🔐 SecurePass — Encrypted Password Vault & Crypto Toolkit

## 🧠 Overview

SecurePass is a full-stack web application designed to securely store and manage user credentials while demonstrating core cybersecurity concepts such as hashing, encryption, and secure authentication.

Originally developed for CPSC 329 (Cybersecurity), this project was extended into a **portfolio-ready system** showcasing real-world implementations of encryption workflows and backend security design.

---

## 🚀 Features

* 🔐 **Secure Authentication**

  * Passwords hashed using SHA-256 with salting
  * No plaintext credential storage

* 🔑 **Encrypted Password Vault**

  * Store and manage service credentials
  * Caesar-based encryption for stored data
  * Secure retrieval and decryption

* 🧠 **Cryptography Tools**

  * Caesar Cipher (encrypt/decrypt + analysis)
  * RSA Encryption (key generation + message encryption)
  * Frequency Analysis

* 🌐 **Full Web Application**

  * Flask backend (REST-style routes)
  * Interactive frontend using HTML + Tailwind CSS
  * Dynamic UI with Alpine.js

---

## 🏗️ Architecture

The system follows a modular client-server design:

* **Frontend (Templates)**
  Handles user interaction, forms, and visualization

* **Backend (Flask API)**
  Processes authentication, encryption, and vault logic

* **Security Layer**
  Applies hashing and encryption before data storage

* **Storage Layer**
  JSON-based persistence for users and vault entries

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** HTML, Tailwind CSS, Alpine.js
* **Security:** SHA-256, Caesar Cipher, RSA, AES (module included)
* **Storage:** JSON

---

## 📁 Project Structure

```bash
securepass-password-vault/
├── api.py
├── CredentialProcess.py
├── requirements.txt
├── users.json
├── vault_data.json
├── app/
│   ├── crypto/
│   └── utils/
├── templates/
```

---

## ▶️ Running Locally
### First, install zip file
#### Second, extract all from zip file
##### Third, open the file in terminal
- Then run these commands
```bash
pip install -r requirements.txt
python api.py
```

Then open:
👉 http://127.0.0.1:5000

---

## 🧪 Example Use Cases

* Register/login securely
* Store encrypted credentials in vault
* Perform encryption using Caesar or RSA tools
* Analyze ciphertext with frequency tools

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.
It should not be used to store sensitive real-world credentials.

---

## 👤 Author

**Hatem Chehade**
Computer Science Student @ University of Calgary
