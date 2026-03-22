import json
import os

# File where the vault data will be stored
VAULT_FILE = 'vault_data.json'

# Load all vault entries from the JSON file
def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []  # Return empty list if file doesn't exist yet
    with open(VAULT_FILE, 'r') as file:
        return json.load(file)  # Load and return JSON data as Python list

# Save all vault entries to the JSON file
def save_vault(data):
    with open(VAULT_FILE, 'w') as file:
        json.dump(data, file, indent=4)  # Pretty print with 4-space indentation

# Generate a unique ID for a new vault entry
def generate_id(entries):
    if not entries:
        return 1  # Start IDs at 1 if vault is empty
    return max(entry['id'] for entry in entries) + 1  # Get next available ID
