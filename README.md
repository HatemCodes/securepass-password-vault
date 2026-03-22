
# 🔐 SecurePass - Password Manager and Crypto Toolkit

SecurePass is a web-based application built for CPSC 329. It integrates user authentication, encrypted password storage, and cryptographic tools like Caesar and RSA encryption. The project is built using Flask and structured for both educational and practical demonstration of core security concepts.

---

## 📁 Project Structure and File Descriptions

### 🔧 Root Directory

- `api.py`: Main Flask server with all route definitions for pages, APIs, encryption tools, and vault logic.
- `CredentialProcess.py`: Handles user credential storage using SHA-256 hashing with a fixed salt.
- `users.json`: Stores hashed credentials of all registered users.
- `vault_data.json`: Stores encrypted service credentials per user using Caesar cipher.

### 📄 Templates Directory (HTML Frontend)

- `templates/base.html`: Main homepage UI.
- `templates/auth/`: Login and Register page templates.
- `templates/pm/`: User dashboard, vault management, and services UI.
- `templates/crypto/`: Caesar and RSA encryption tool UIs.

### 🔐 `app/crypto/`

- `caesar.py`: Contains Caesar cipher logic (encrypt/decrypt functions).
- `rsa.py`: Contains RSA logic: key generation, encryption, and decryption.

### 🧰 `app/utils/`

- `json_storage.py`: Utility to load, save, and generate unique IDs for vault entries.

### 📦 Other Files

- `requirements.txt`: Python dependencies required to run the app.
- `.gitignore`: Prevents committing of unwanted files.
- `.git/`: Git configuration and commit history folder.

---

## ⚙️ How It Works

### 🧾 User Authentication

- Users register or login using a username and password.
- These credentials are **hashed with a fixed salt using SHA-256** and stored in `users.json`.

### 🔐 Vault Management

- Each user can store multiple services (e.g., Gmail, Facebook).
- For each service, the **username and password are encrypted** with Caesar cipher and stored in `vault_data.json`.
- On retrieval, values are decrypted and displayed securely.

### 🌀 Caesar Cipher Tool

- Offers manual encryption/decryption based on a user-defined shift.
- Accessible via the `/caesar.html` route.

### 🛡️ RSA Tool

- Generates public/private key pairs.
- Allows users to encrypt and decrypt messages using the RSA algorithm.
- Supports manual encryption via `/rsa.html`.

---

## 🚀 Running the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/cpsc-329-final-project.git
cd cpsc-329-final-project
```

### Step 2: Set Up the Environment

(Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ If encoding issues occur in `requirements.txt`, open the file and re-save it using UTF-8 encoding.

### Step 4: Launch the App

```bash
python api.py
```

Go to `http://127.0.0.1:5000` in your browser.

---

## 🧪 Example Interactions

### Registering a User

```json
POST /register
{
  "username": "hatemiscool",
  "password": "testpass123"
}
```

### Caesar API Usage

```json
POST /caesar
{
  "text": "secure",
  "shift": 5,
  "mode": "encrypt"
}
```

### Saving a Vault Entry

```json
POST /vault
{
  "service": "Gmail",
  "username": "hatemiscool@gmail.com",
  "password": "mypassword123"
}
```

---

## 👨‍💻 Authors and Credits

- **Hatem C. , Yousif B. , Mcveigth B.** – Authentication and cryptography integration
- **Rydon L. , Emily N.** – Add frontend/UI/database/etc.

---

## ⚠️ Disclaimer

This application is built for **educational purposes only**. It should NOT be used to store sensitive personal information. Use secure, industry-grade password managers for real-world needs.
