def ex1(str):
    print(str)

def ex2(min,max):
    for i in range(min,max):
        print(i)

def ex3():
    numero = int(input("Introduce un numero: "))
    if numero % 2 == 0:
        print("es PAR")
    else:
        print("es IMPAR")

def ex4():
    numero = float(input("Introduce un numero: "))
    if numero > 0:
        print("el numero es positivo")
    elif numero < 0:
        print("el numero es negativo")
    else:
        print("el numero es 0")

def ex5(n):
    #fibonacci
    a, b = 0, 1
    for i in range(n-1):
        print(a, end=', ')
        a, b = b, a + b
    print(a, end='.')

def ex6(*, a,b):
    return a + b

#print(ex6(a=2,b=3))

def ex7(n):
    if n == 0:
        return 1
    else:
        return n * ex7(n-1)
    
import math as mt

def ex8(a,b):
    num = mt.pow(a,a)
    if num % b == 0:
        print("la potencia de A es divisible entre B")
    else:
        print("la potencia de A no es divisible entre B")

import random as rd

def ex9(minimo, maximo):
    print(f"Vas a intentar adivinar un número aleatorio entre el {minimo} y el {maximo}, probaremos tu INTUICIÓN")
    numero = int(input("INTRODUCE EL NÚMERO: "))
    numero_aleatorio = rd.randint(minimo, maximo)
    diferencia = abs(numero - numero_aleatorio)
    rango = maximo - minimo
    proximidad = (rango - diferencia) / rango * 100
    print(f"Tu número está al {proximidad}% de proximidad al número aleatorio.")

#MIRAR EN EL DOCUMENTO DE TKINTER

def ex10():
    guacamoles = [rd.randint(0,1) for _ in range(10)]
    print(guacamoles)

class ex12:
    def __init__(self) -> None:
        self.colores = ('rojo', 'verde', 'azul', 'rojo', 'verde', 'rojo', 'azul', 'verde', 'verde', 'rojo')
    
    def color_mas_frequente(self):
        return max(set(self.colores), key= self.colores.count)
    
    def printColorMasFrequente(self):
        color_frquente = self.color_mas_frequente()
        print(self.colores)
        print(f"el color mas frequente es: {color_frquente}")

# colores = ex12()
# colores.printColorMasFrequente()

def ex12(a,b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error! Division por cero.")
        return None
    else:
        return resultado
    
def ex13():
    diccionario = {'a':1,'b':2,'c':3}

    try:
        print(diccionario['d'])
    except KeyError:
        print("la clave no se encuentra en el diccionario")

class ex14:
    def __init__(self, nombre_archivo):
        self.monstruos = ['Cthulhu', 'Byakhee', 'Deep Ones', 'Great Old One', 'Yog-Sothoth', 'Azathoth', 'Shoggoth', 'Outer God', 'Nyarlathotep', 'Dunwich Horror']
        self.nombre_archivo = nombre_archivo

    def anadir_monstruo(self, monstruo):
        self.monstruos.append(monstruo)

    def crear_archivo(self):
        with open(self.nombre_archivo, 'w') as f:
            for monstruo in self.monstruos:
                f.write(monstruo + '\n')

    def leer_archivo(self):
        with open(self.nombre_archivo, 'r') as f:
            lineas = f.readlines()
        print(f'Hay {len(lineas)} monstruos en el archivo.')

# monstruos = ex14('monstruos_lovecraft.txt')
# monstruos.crear_archivo()
# monstruos.leer_archivo()
# monstruos.anadir_monstruo('Elder Thing')
# monstruos.anadir_monstruo('Night Gaunt')
# monstruos.crear_archivo()
# monstruos.leer_archivo()

class ex15_persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def decir_hola(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# persona = Persona("Juan", 30)
# print(persona.decir_hola())

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_informacion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"

class Revista(Libro):
    def __init__(self, titulo, autor, numero):
        super().__init__(titulo, autor)
        self.numero = numero

    def obtener_informacion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Numero: {self.numero}"

class Periodico(Libro):
    def __init__(self, titulo, autor, fecha):
        super().__init__(titulo, autor)
        self.fecha = fecha

    def obtener_informacion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Fecha: {self.fecha}"

# libro = Libro("Don Quijote", "Miguel de Cervantes")
# print(libro.obtener_informacion())

# revista = Revista("National Geographic", "John Doe", 123)
# print(revista.obtener_informacion())

# periodico = Periodico("El País", "Jane Doe", "16/11/2023")
# print(periodico.obtener_informacion())

import os

def listar_archivos(directorio):
    archivos = []
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_completa):
            tamano = os.path.getsize(ruta_completa) / (1024 * 1024 * 1024)  # Convertir a gigabytes
            archivos.append((tamano, archivo))
    return archivos

# archivos = listar_archivos(os.path.expanduser("~/Desktop"))

# # Ordenar los archivos por tamaño
# archivos.sort()

# # Añadir los nombres de los archivos a un archivo de texto
# with open('archivos_en_el_escritorio.txt', 'w') as f:
#     for tamano, nombre in archivos:
#         f.write(f"({tamano:.3f} GB :Size ){nombre} \n")

def primegenerator():
    yield 2
    primenumbers = [2]
    candidate = 3
    while True:
        if all(candidate % prime != 0 for prime in primenumbers):
            primenumbers.append(candidate)
            yield candidate
        candidate += 2

# generator = primegenerator()
# for _ in range(10):
#     print(next(generator))