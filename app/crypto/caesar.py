# Caesar cipher encryption function
def encrypt(text, shift):
    result = []  # List to store encrypted characters
    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Determine base ASCII depending on case
            shifted = (ord(char) - base + shift) % 26 + base  # Apply Caesar shift
            result.append(chr(shifted))  # Convert back to character and append
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)  # Join the list into a final string

# Caesar cipher decryption function (uses negative shift)
def decrypt(text, shift):
    return encrypt(text, -shift)
