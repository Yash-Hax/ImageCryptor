from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# Define the key size
KEY_SIZE = 32  # 256-bit key

def generate_key():
    # Generate a random key
    return get_random_bytes(KEY_SIZE)

def encrypt_image(input_file, output_file, key):
    # Encrypt an image
    cipher = AES.new(key, AES.MODE_EAX)
    with open(input_file, 'rb') as file:
        data = file.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        nonce = cipher.nonce
    with open(output_file, 'wb') as file:
        file.write(ciphertext)
    return nonce

def decrypt_image(input_file, output_file, key, nonce):
    # Decrypt an image
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    with open(input_file, 'rb') as file:
        ciphertext = file.read()
        data = cipher.decrypt(ciphertext)
    with open(output_file, 'wb') as file:
        file.write(data)

# Generate a random key
key = generate_key()

# Encrypt an image
nonce = encrypt_image('image.jpg', 'encrypted_image.bin', key)

# Decrypt the image
decrypt_image('encrypted_image.bin', 'decrypted_image.jpg', key, nonce)