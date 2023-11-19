def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Shift the character based on the shift value
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            # Append the shifted character to the encrypted text
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift):
    # To decrypt, we use the negative of the shift value
    return encrypt(encrypted_text, -shift)

# Example usage:
plaintext = "Hello, World!"
shift_value = 3

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, shift_value)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text, shift_value)
print(f"Decrypted text: {decrypted_text}")
