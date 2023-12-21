import random as rd

def generar_contrasena():
    letras_minusculas = [chr(i) for i in range(97, 123)]  # Letras minúsculas en ASCII
    letras_mayusculas = [chr(i) for i in range(65, 91)]  # Letras mayúsculas en ASCII
    simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', ':', ';', '<', '>', ',', '.', '?', '/']
    contrasena = [rd.choice(letras_mayusculas) for _ in range(rd.randint(1, 2))]  # Asegura que haya al menos 1 o 2 letras mayúsculas
    contrasena.append(rd.choice(simbolos))  # Asegura que haya al menos un símbolo
    while len(contrasena) < 8:  # Asegura que la contraseña tenga 8 caracteres
        contrasena.append(rd.choice(letras_minusculas))  # Añade un carácter aleatorio
    rd.shuffle(contrasena)  # Mezcla los caracteres
    return ''.join(contrasena)

contrasena = generar_contrasena()
print(f"Contraseña generada: {contrasena}")