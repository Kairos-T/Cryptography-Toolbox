from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def substitution_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key[alphabet.index(char.lower())].upper()
            else:
                result += key[alphabet.index(char)]
        else:
            result += char
    return result

def vigenere_cipher(text, key):
    key_len = len(key)
    result = ""
    for i in range(len(text)):
        shift = ord(key[i % key_len].lower()) - 97
        if text[i].isalpha():
            if text[i].isupper():
                result += chr((ord(text[i]) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(text[i]) + shift - 97) % 26 + 97)
        else:
            result += text[i]
    return result

def aes_encrypt(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def aes_decrypt(key, data):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()

def rsa_encrypt(public_key, data):
    ciphertext = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext.hex()

def rsa_decrypt(private_key, ciphertext):
    plaintext = private_key.decrypt(
        bytes.fromhex(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

def show_menu():
    print("Select a cryptography technique:")
    print("-"*20)
    print("| 1. Caesar Cipher")
    print("| 2. Substitution Cipher")
    print("| 3. Vigenere Cipher")
    print("| 4. AES Encryption")
    print("| 5. RSA Encryption")
    print("| 6. Exit")
    print("-"*20)


key = b'Insert 32-byte secret key here'

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        text = input("Enter the text to encrypt/decrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted = caesar_cipher(text, shift)
        decrypted = caesar_cipher(encrypted, 26-shift)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "2":
        text = input("Enter the text to encrypt/decrypt: ")
        key = input("Enter the substitution key: ")
        encrypted = substitution_cipher(text, key)
        decrypted = substitution_cipher(encrypted, key)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "3":
        text = input("Enter the text to encrypt/decrypt: ")
        key = input("Enter the Vigenere key: ")
        encrypted = vigenere_cipher(text, key)
        decrypted = vigenere_cipher(encrypted, key)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "4":
        text = input("Enter the text to encrypt/decrypt: ")
        encrypted = aes_encrypt(key, text)
        decrypted = aes_decrypt(key, encrypted)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "5":
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        data = input("Enter the text to encrypt: ")
        encrypted = rsa_encrypt(public_key, data)
        decrypted = rsa_decrypt(private_key, encrypted)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "6":
        break
        
    else:
        print("Invalid choice. Please try again.")