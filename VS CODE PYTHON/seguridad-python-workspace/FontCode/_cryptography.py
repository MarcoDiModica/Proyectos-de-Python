# Importamos las bibliotecas necesarias
from cryptography.fernet import Fernet

# Generamos una clave
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Cargamos la clave
def load_key():
    return open("secret.key", "rb").read()

# Encriptamos un mensaje
def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

# Desencriptamos un mensaje
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Ejemplo de uso
if __name__ == "__main__":
    generate_key()
    msg = "Mi Nombre es Marco Di Modica"
    encrypted = encrypt_message(msg)
    print("Mensaje encriptado:", encrypted)
    decrypted = decrypt_message(encrypted)
    print("Mensaje desencriptado:", decrypted)