import hashlib
import json
import os

# Fixed salt and file path
FIXED_SALT = "this_is_a_fixed_salt_value"
USER_DATA_FILE = 'users.json'

# Hash with fixed salt
def hash_with_fixed_salt(value):
    return hashlib.sha256((FIXED_SALT + value).encode('utf-8')).hexdigest()

# Store a user credential as key-value pair: {hashed_username: hashed_password}
def store_user_credentials(username, password):
    hashed_username = hash_with_fixed_salt(username)
    hashed_password = hash_with_fixed_salt(password)

    # Load existing data or initialize new dict
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # Store or update the user
    data[hashed_username] = hashed_password

    # Save updated data
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"User '{username}' stored securely.")

# Retrieve all users (hashed usernames and passwords)
def get_all_users():
    if not os.path.exists(USER_DATA_FILE):
        print("No user data found.")
        return {}

    with open(USER_DATA_FILE, 'r') as f:
        return json.load(f)

# Get password hash given a hashed username
def get_user_credentials_password(hashed_username):
    if not os.path.exists(USER_DATA_FILE):
        return None

    with open(USER_DATA_FILE, 'r') as f:
        data = json.load(f)

    return data.get(hashed_username)


def is_username_taken(username):
    hashed_username = hash_with_fixed_salt(username)
    return get_user_credentials_password(hashed_username) is not None

"""
NOTE
JSON FORMAT STORING:
{
    username : password
}

username and password are both is hashed (with salt) applied.

"""
