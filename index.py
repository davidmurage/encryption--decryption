from cryptography.fernet import Fernet


# Generate a random symmetric key
def generate_key():
    return Fernet.generate_key()


# Encrypt a message with the key
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


# Decrypt an encrypted message with the key
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()


if __name__ == "__main__":
    key = generate_key()
    message = "Karima boys CENTER"

    encrypted_message = encrypt_message(key, message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_message(key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
