# 🔐 SecurePass — Encrypted Password Vault & Crypto Toolkit

## 📸 Demo
<img width="1920" height="430" alt="{AB048445-A51F-449A-B8DF-8552598404A4}" src="https://github.com/user-attachments/assets/554b0a07-3c5c-4798-ad3a-307ccd662d35" />
<img width="1468" height="820" alt="{EAAEB4CC-F6A1-4E32-9EA3-57BFD99B6FB2}" src="https://github.com/user-attachments/assets/282704ef-8583-4c65-b4a6-523e9c6f8d17" />
<img width="1555" height="761" alt="{F7B139E5-8C68-482C-A09D-8136B34BF1C0}" src="https://github.com/user-attachments/assets/ae956c88-0c5d-431e-a6b8-8a3fb8c088e9" />
<img width="1601" height="974" alt="{0A88C375-40C8-4685-BC17-AB55F74BBE79}" src="https://github.com/user-attachments/assets/26565ec9-d950-4b78-8ff9-2cffc9d62fcc" />
<img width="1086" height="888" alt="{7B40A39F-E9AC-49F4-BF5B-360880F7CB68}" src="https://github.com/user-attachments/assets/7bc9e417-397d-4666-92ca-bc39e57aa6f8" />

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
## 🔒 Security Note

This project demonstrates core cryptographic concepts but does not implement production-grade security practices such as secure key management, HTTPS enforcement, or database-level protections.
## 👤 Author

**Hatem Chehade**
Computer Science Student @ University of Calgary
