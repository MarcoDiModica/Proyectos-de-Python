#con print podemos imprimir texto o varbles
print("hola buenas")

#podemos printear el type de la variable
x = 5
print(type(x))

#podemos hacer que entre dentro de la declaracion poniendo : al final de la linea, la siguiente mientras este en la misma TAB estara dentro de la declaracion
if x > 5:
    print("x es mayor que 5")
elif x < 5:
    print("x es menor que 5")
else:
    print("x es igual a 5")


#la f que hay antes de la string sirve para incrustar elementos dentro del texto
for i in range(6):
    print(f"el valor de i es: {i}")

#en python no se usa el ++ para incrementar en 1, se tiene que hacer manualmente
contador = 0
while contador <= 5:
    print(f"el valor del contador es {contador}")
    contador += 1

#el range podemos poner 2 valores objetivos, el inicial y el final, pero si solamente ponemos un valor comenzara desde 0 hasta el numero que pongamos, el valor inicial esta
#siempre incluido, pero el valor final no esta incluido, entonces tenemos que sumar 1 al valor esperado
for i in range (-6,6):
    print(i)

#asi podemos acortar los decimales de un float
numero = 3.14159
print(f"{numero:.2f}")

#los diferentes tipos de variables que hay en python
a = 10 #int
b = 2.14 #float
c = 1 + 2j #complex                                             LUEGO SE EXPANDE
d = True #bool
d = "buenas tardes" #str
lista = [1, "dos", .314] #list                                  LUEGO SE EXPANDE
tupla = (1, "dos", .314) #tuple                                 LUEGO SE EXPANDE
diccionario = {"uno": 1, "dos": 2, "tres": 3} #dict             LUEGO SE EXPANDE
conjunto = {1,2,3,4} #set                                       LUEGO SE EXPANDE

#Operaciones Aritmeticas
a+b #suma
a-b #resta
a*b #multiplicacion
a/b #division
a//b #division entera (redondea hacia abajo al entero más cercano)
a%b #Modulo (resto de la division)
a**b #Exponenciacion

#Operaciones de Comparacion
a == b #igualdad
a != b #desigualdad
a > b #mayor que
a < b #menor que
a >= b #mayor o igual
a <= b #menor o igual

#Operadores Logicos
a and b #(verdadero si tanto a como b son verdaderos)
a or b #(verdadero si a o b son verdaderos)
not a #(verdadero si a es falso)

#Operaciones de Asignacion
a = b
a += b #(equivalente a a = a + b)
a -= b #(equivalente a a = a - b)
a *= b #(equivalente a a = a * b)
a /= b #(equivalente a a = a / b)
a %= b #(equivalente a a = a % b)
a **= b #(equivalente a a = a ** b)

#Complex : son un tipo de número que se compone de una parte real y una parte imaginaria

#Listas : Las listas funcionan parecido a C 

print(lista[0]) #esto imprimira lo que haya en el primer lugar de la lista

lista[1] = 10 #puedes cambiar cualquier elemento de la lista
print(lista) #puedes printear una lista entera

lista.append(6) #agregas el elemnto 6 (en este caso) al final de la lista

lista.insert(1, 20) #insertas en la posicion 1 el numero 20, es decir que si la lista era [1,2,3,6] pasara a ser [1,20,2,3,6], en este caso no sustituye ningun valor simplemente lo instera

lista.remove(20) #busca el elmento 20 y lo elimina

lista.pop(0) #elimina el elemnto el la posicion 0

for element in lista:
    print(element)
    #puedes recorrer una lista en un bucle de esta manera bastante mas facil que en C

for elemento in range(len(lista)):
    print(elemento)
    #esto seria la representacion de lo que se hace en C pero en python

lista.sort() #puedes ordenar la lista de menor a mayor
lista.sort(reverse=True) #hace lo mismo que antes solo que ahora lo hace de mayor a menor

#en caso de ordenar una lista de strings se ordenaran alfabeticamente, ten en cuenta que las mayusculas se consideran menos que las minuscular, si quieres ordenar tu lista
#sin que se tenga en cuenta eso puedes usar:
lista.sort(key=str.lower)

lista_ordenada = sorted(lista) #asi no modificas la lista original

lista_invertida = list(reversed(lista)) #lo mismo que lo anterior solo que con la lista invertida
#reversed no se usa exclusivamente para lista por esa razon devemos especificar el datatype del mismo antes de ejecutar la funcion

lista.reverse() #invierte el orden de los elemntos en la lista

lista.count(2) #con count puedes contar el numero de veces que aparece ese elemento en la lista

lista.index(2) #encuentras el indice del elemento desdeado

lista.clear() #Para vaciar la lista

lista1 = [1,2,3,4]
lista2 = lista1.copy() #para copiar los elementos de una lista a otra

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2) #con esto puedes sumarle a la lista1 la lista 2

lista3 = [[1,2,3],[4,5,6],[7,8,9]] #a esto se le llaman listas anidadas
#se puede acceder a los elementos como un array bidimensional
lista3[0][1] #el segundo elemento de la primera lista

lista4 = [i**2 for i in range(10)] #esta es la creacion de una lista donde contiene todos los cuadrados de los numeros del 0 al 9
i**2 #esto calcula el cuadrado

len(lista) #devuelve el largo de la lista, si la lista tiene 5 elementos devolvera el valor 5, no devolvera el indice mas alto
max(lista) #devuelve el valor mas grande en la lista
min(lista) #devuelve el valor mas pequeno en la lista
sum(lista) #devuelve la suma de todos los elementos de la lista
enumerate(lista) #Esta función se utiliza para iterar sobre una lista (o cualquier otro iterable) de manera que también tengas acceso al índice de cada elemento.
zip(lista) #Esta función se utiliza para iterar sobre múltiples listas (u otros iterables) al mismo tiempo. Se suele utilizar en for

lista5 = [1,2,3,4,5,6]
sublista = lista[2:5] #crea una sublista, desde el indice 2 al indice 5

#para comprobar si un elemento esta en la lista puedes hacer tal que asi:
valor = 5
if valor in lista:
    lista.index(valor)
    #... y aqui continuas con el codigo

#TUPLAS

#Las tuplas son similares a las listas, pero son inmutables, lo que significa que no puedes cambiar sus elementos una vez creadas.
#Crear una tupla: tupla = (1, 2, 3)
#Acceder a elementos: tupla[0] (devuelve el primer elemento de la tupla)
#Longitud de una tupla: len(tupla)
#Contar elementos: tupla.count(1) (devuelve el número de veces que 1 aparece en la tupla)
#Encontrar la posición de un elemento: tupla.index(2) (devuelve el índice del primer elemento que es igual a 2)
#Las tuplas son más eficientes en términos de memoria y rendimiento que las listas, por lo que se pueden utilizar +
# + en lugar de las listas cuando los datos no necesitan ser modificados.

#DICCIONARIOS

#Los diccionarios son una colección desordenada de pares clave-valor.
#Crear un diccionario: diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
#Acceder a elementos: diccionario['uno'] (devuelve el valor asociado con la clave ‘uno’)
#Modificar elementos: diccionario['uno'] = 10
#Añadir elementos: diccionario['cuatro'] = 4
#Eliminar elementos: del diccionario['cuatro']
#Comprobar si una clave está en el diccionario: 'uno' in diccionario (devuelve True si ‘uno’ está en las claves del diccionario)
#Obtener todas las claves: diccionario.keys()
#Obtener todos los valores: diccionario.values()
#Obtener todos los pares clave-valor: diccionario.items()
#Los diccionarios son muy eficientes para buscar, añadir y eliminar elementos, por lo que se utilizan a menudo para almacenar datos que necesitan ser accedidos rápidamente.

#CONJUNTOS

#Los conjuntos son una colección desordenada de elementos únicos.
#Crear un conjunto: conjunto = {1, 2, 3}
#Añadir elementos: conjunto.add(4)
#Eliminar elementos: conjunto.remove(1)
#Comprobar si un elemento está en el conjunto: 1 in conjunto (devuelve True si 1 está en el conjunto)
#Operaciones de conjuntos: 
# unión (conjunto1 | conjunto2) simplemete los junta, como si se sumasen
# intersección (conjunto1 & conjunto2) guarda el ultimo elemento de el primer conjunto y el primero del segundo conjunto
# diferencia (conjunto1 - conjunto2) devuelve los elementos que estan en el primer conjunto pero en el segundo no
# diferencia simétrica (conjunto1 ^ conjunto2) devuelve los elementos que estan en el conjunto 1 o en el conjunto 2 pero no en ambos
#Los conjuntos son muy eficientes para comprobar si un elemento está presente, por lo que se utilizan a menudo para eliminar duplicados o para probar la pertenencia a un conjunto.

#ESTRUCTURAS DE CONTROL

#if ejecuta un bloque si la condicion es True
#elif ejecuta un bloque si la anterior es falsa y la suya es verdadera
#else ejecuta un bloque si todas las anteriores condiciones son falsas

#for Ejecuta un bloque de código para cada elemento en una secuencia
#while Ejecuta un bloque de código mientras una condición sea verdadera.

#break Termina el bucle actual y reanuda la ejecución en la siguiente instrucción después del bucle.
#continue Salta el resto de la iteración actual y pasa a la siguiente iteración del bucle.
#pass No hace nada y se utiliza cuando se requiere una declaración sintácticamente pero no se quiere ejecutar ningún código. (se suele usar cuando aun no has implementado el metodo y no quieres que salte error)

#puedes enumerar listas
lista7 = ['a', 'b', 'c', 'd', 'e']
for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")

#Iterar sobre múltiples listas a la vez
lista8 = [1, 2, 3]
lista9 = ['a', 'b', 'c']
for num, letra in zip(lista8, lista9):
    print(f"Número: {num}, Letra: {letra}")

#Bucle while con else:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("El bucle ha terminado")

#metodo .join()
lista = ['hola', 'mundo']
s = ' '.join(lista) #el ' ' que hay antes del join es el separador que se usara, se puede usar lo que quieras o no usar ninguno EJEMPLOS:(' ' '-' '')
print(s)  # Imprime "hola mundo"

#metodo split
s = "hola mundo"
lista = s.split(' ')
print(lista)  # Imprime ['hola', 'mundo']

#metodo replace(viejo, nuevo)
s = "hola mundo"
s = s.replace('mundo', 'Python')
print(s)  # Imprime "hola Python"

#metodos UPPER LOWER (cambia de mayusculas a minusculas y viceversa)
s = "hola mundo"
print(s.upper())  # Imprime "HOLA MUNDO"
print(s.lower())  # Imprime "hola mundo"

#metodo strip (quita los espacios al principio y al final de la string)
s = "   hola mundo   "
s = s.strip()
print(s)  # Imprime "hola mundo"

#FUNCIONES

def saludo(nombre):
    print(f"Hola, {nombre}")

def suma(a, b):
    return a + b

#Funcion de tipo argumento obligatorio
def obl_arg(*, a, b): #se usa el * antes de los argumentos
    print(a, b)
obl_arg(a=1, b=2)  # Imprime "1 2"

#Usar * o ** para los argumentos de las funciones
def desempaquetar(a, b, c):
    print(a, b, c)
lista = [1, 2, 3]
desempaquetar(*lista)  # Imprime "1 2 3"

#Decoradores de funciones
def mi_decorador(func):
    def envoltura():
        print("¡Esto se imprime antes de llamar a la función!")
        func()
        print("¡Esto se imprime después de llamar a la función!")
    return envoltura

@mi_decorador
def di_hola():
    print("¡Hola!")

di_hola()

#Cuando aplicamos mi_decorador a di_hola con el símbolo @, estamos diciendo que di_hola debe ser 
#pasada a mi_decorador como argumento. Entonces, cuando llamamos a di_hola(), en realidad estamos llamando a envoltura(), que imprime los mensajes adicionales y luego llama a di_hola.

#Funciones anonimas (lambda)
suma = lambda a, b: a + b
print(suma(5, 3))  # Imprime "8"

#region LISTA DE FUNCIONES BUILD-IN EN PYTHON

# abs()
# Devuelve el valor absoluto de un número.
print(abs(-5))  # Imprime 5

# all()
# Devuelve True si todos los elementos del iterable son verdaderos (o si el iterable está vacío).
print(all([True, True, False]))  # Imprime False

# any()
# Devuelve True si cualquier elemento del iterable es verdadero. Si el iterable está vacío, devuelve False.
print(any([True, False, False]))  # Imprime True

# bin()
# Convierte un número entero a una cadena binaria con el prefijo "0b".
print(bin(10))  # Imprime '0b1010'

# bool()
# Devuelve un valor booleano, es decir, uno de True o False.
print(bool(0))  # Imprime False
print(bool(1))  # Imprime True

# enumerate()
# Toma una colección (por ejemplo, una tupla) y la devuelve como un objeto enumerado.
for i, valor in enumerate(['a', 'b', 'c']):
    print(i, valor)
# Imprime:
# 0 a
# 1 b
# 2 c

# filter()
# Usa una función de filtro para excluir elementos en un objeto iterable.
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Imprime [2, 4, 6]

# map()
# Devuelve el iterador especificado con la función especificada aplicada a cada elemento.
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))  # Imprime [1, 4, 9, 16, 25]

# max()
# Devuelve el elemento más grande en un iterable.
print(max([1, 2, 3]))  # Imprime 3

# min()
# Devuelve el elemento más pequeño en un iterable.
print(min([1, 2, 3]))  # Imprime 1

# sum()
# Devuelve la suma de todos los elementos de un iterable.
print(sum([1, 2, 3, 4, 5]))  # Imprime 15

# zip()
# Devuelve un objeto zip, que es un iterador de tuplas donde el primer elemento de cada iterador se empareja, luego el segundo elemento de cada iterador se empareja, etc.
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
combinado = zip(numeros, letras)
print(list(combinado))  # Imprime [(1, 'a'), (2, 'b'), (3, 'c')]

# round()
# Redondea un número.
print(round(3.14159, 2))  # Imprime 3.14

# sorted()
# Devuelve una versión ordenada de una lista.
print(sorted([3, 1, 4, 1, 5, 9]))  # Imprime [1, 1, 3, 4, 5, 9]

# len()
# Devuelve la longitud de un objeto.
print(len('hola'))  # Imprime 4

# type()
# Devuelve el tipo de un objeto.
print(type(123))  # Imprime <class 'int'>

# str()
# Devuelve una cadena.
print(str(123))  # Imprime '123'

# int()
# Devuelve un número entero.
print(int('123'))  # Imprime 123

# float()
# Devuelve un número de punto flotante.
print(float('3.14'))  # Imprime 3.14

# list()
# Devuelve una lista.
print(list('hola'))  # Imprime ['h', 'o', 'l', 'a']

# dict()
# Devuelve un diccionario.
print(dict([(1, 'uno'), (2, 'dos')]))  # Imprime {1: 'uno', 2: 'dos'}

# set()
# Devuelve un conjunto.
print(set([1, 2, 2, 3, 3, 3]))  # Imprime {1, 2, 3}

# frozenset()
# Devuelve un objeto frozenset.
print(frozenset([1, 2, 2, 3, 3, 3]))  # Imprime frozenset({1, 2, 3})

# chr()
# Devuelve un carácter del código Unicode especificado.
print(chr(65))  # Imprime 'A'

# ord()
# Convierte un número entero que representa el Unicode del carácter especificado.
print(ord('A'))  # Imprime 65

# hex()
# Convierte un número en un valor hexadecimal.
print(hex(255))  # Imprime '0xff'

# oct()
# Convierte un número en un octal.
print(oct(8))  # Imprime '0o10'

# pow()
# Devuelve el valor de x a la potencia de y.
print(pow(2, 3))  # Imprime 8

# range()
# Devuelve una secuencia de números, comenzando desde 0 e incrementando por 1 (por defecto).
print(list(range(10)))  # Imprime [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# tuple()
# Devuelve una tupla.
print(tuple([1, 2, 3]))  # Imprime (1, 2, 3)

# slice()
# Devuelve un objeto de corte.
s = slice(1, 3)
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[s])  # Imprime ['b', 'c']

# reversed()
# Devuelve un iterador invertido.
print(list(reversed([1, 2, 3])))  # Imprime [3, 2, 1]

# iter()
# Devuelve un objeto iterador.
it = iter([1, 2, 3])
print(next(it))  # Imprime 1
print(next(it))  # Imprime 2
print(next(it))  # Imprime 3

# next()
# Devuelve el siguiente elemento en un objeto iterable.
it = iter([1, 2, 3])
print(next(it))  # Imprime 1
print(next(it))  # Imprime 2
print(next(it))  # Imprime 3

# open()
# Abre un archivo y devuelve un objeto de archivo.
# f = open('mi_archivo.txt', 'r')
# print(f.read())  # Imprime el contenido del archivo
# f.close()

# input()
# Permite la entrada del usuario.
# nombre = input("¿Cuál es tu nombre? ")
# print(nombre)

# eval()
# Evalúa y ejecuta una expresión.
print(eval('3 + 4'))  # Imprime 7

# exec()
# Ejecuta el código especificado (u objeto).
exec('a = 5; b = 6; print(a + b)')  # Imprime 11

# compile()
# Devuelve el código fuente especificado como un objeto, listo para ser ejecutado.
codigo = compile('a = 5; b = 6; print(a + b)', 'codigo', 'exec')
exec(codigo)  # Imprime 11

# globals()
# Devuelve la tabla de símbolos global actual como un diccionario.
print(globals())  # Imprime el diccionario global actual

# locals()
# Devuelve un diccionario actualizado de la tabla de símbolos local actual.
def prueba():
    x = 5
    print(locals())  # Imprime {'x': 5}
prueba()

# vars()
# Devuelve el diccionario __dict__ de un objeto.
class Prueba:
    x = 5
print(vars(Prueba))  # Imprime {'x': 5, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Prueba' objects>, '__weakref__': <attribute '__weakref__' of 'Prueba' objects>, '__doc__': None}

# isinstance()
# Devuelve True si un objeto especificado es una instancia de un objeto especificado.
print(isinstance(5, int))  # Imprime True

# issubclass()
# Devuelve True si una clase especificada es una subclase de un objeto especificado.
class MiClase(int): pass
print(issubclass(MiClase, int))  # Imprime True

# super()
# Devuelve un objeto temporal de la superclase.
class MiClase(int):
    def __init__(self, x):
        super().__init__()
print(MiClase(5))  # Imprime 5

# property()
# Obtiene, establece, elimina una propiedad.
class MiClase:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor

    @x.deleter
    def x(self):
        del self._x

c = MiClase()
c.x = 5  # Establece la propiedad x
print(c.x)  # Obtiene la propiedad x
del c.x  # Elimina la propiedad x

# hasattr()
# Devuelve True si el objeto especificado tiene el atributo especificado (propiedad/método).
class MiClase:
    x = 5
print(hasattr(MiClase, 'x'))  # Imprime True

# getattr()
# Devuelve el valor del atributo especificado (propiedad o método).
class MiClase:
    x = 5
print(getattr(MiClase, 'x'))  # Imprime 5

# setattr()
# Establece el valor del atributo especificado (propiedad o método).
class MiClase:
    x = 5
setattr(MiClase, 'x', 10)
print(MiClase.x)  # Imprime 10

# delattr()
# Elimina el atributo especificado (propiedad o método) del objeto especificado.
class MiClase:
    x = 5
delattr(MiClase, 'x')
print(hasattr(MiClase, 'x'))  # Imprime False

# staticmethod()
# Devuelve un método estático para una función.
class MiClase:
    @staticmethod
    def mi_metodo():
        print("¡Hola!")
MiClase.mi_metodo()  # Imprime "¡Hola!"

# classmethod()
# Convierte un método en un método de clase.
class MiClase:
    x = 5

    @classmethod
    def incrementar_x(cls):
        cls.x += 1
MiClase.incrementar_x()
print(MiClase.x)  # Imprime 6

# __import__()
# Esta función es invocada por la declaración import.
math = __import__('math')
print(math.sqrt(16))  # Imprime 4.0

# compile()
# Devuelve el código fuente especificado como un objeto, listo para ser ejecutado.
codigo = compile('a = 5; b = 6; print(a + b)', 'codigo', 'exec')
exec(codigo)  # Imprime 11

# eval()
# Evalúa y ejecuta una expresión.
print(eval('3 + 4'))  # Imprime 7

# exec()
# Ejecuta el código especificado (u objeto).
exec('a = 5; b = 6; print(a + b)')  # Imprime 11

# format()
# Formatea un valor especificado.
print(format(123, '.2f'))  # Imprime '123.00'

# help()
# Ejecuta el sistema de ayuda incorporado.
# help(list)

# memoryview()
# Devuelve un objeto de vista de memoria.
bytes = bytearray('hola', 'utf-8')
vista = memoryview(bytes)
print(vista[0])  # Imprime 104

# object()
# Devuelve un nuevo objeto.
obj = object()
print(obj)  # Imprime algo como <object object at 0x00000213E2733C40>

# repr()
# Devuelve una versión legible de un objeto.
print(repr('hola'))  # Imprime "'hola'"
#endregion

#modulos y paquetes en python

# game.py
#import draw

def play_game():
    ...

def main():
    result = play_game()
    #draw.draw_game(result)

# draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...

#Estructura habitual dentro de python (pero no es necesario)

def main():
    print("¡Hola, mundo!")

if __name__ == "__main__":
    main()

#MANEJO DE EXCEPCIONES

try:
    x = 1 / 1  # No causa una excepción
except ZeroDivisionError:
    print("¡Error: División por cero!")
else:
    print("¡Todo salió bien!")
finally:
    print("¡Siempre me ejecuto, pase lo que pase!")

#LEVANTAR EXCEPCIONES

def dividir(a, b):
    if b == 0:
        raise ValueError("¡No puedes dividir por cero!")
    return a / b

#Entrada y salida de archivos

#con el open si el archivo no existe lo creara

#escribir archivos

f = open('mi_archivo.txt', 'w')  # Abre el archivo en modo de escritura
f.write('¡Hola, mundo!')  # Escribe en el archivo
f.close()  # Cierra el archivo

#leer archivos

f = open('mi_archivo.txt', 'r')  # Abre el archivo en modo de lectura
contenido = f.read()  # Lee el contenido del archivo
print(contenido)  # Imprime el contenido del archivo
f.close()  # Cierra el archivo

#with El uso de with asegura que el archivo se cierre correctamente después de que se haya terminado con él.

# Escribir en un archivo
with open('mi_archivo.txt', 'w') as f:
    f.write('¡Hola, mundo!')

# Leer de un archivo
with open('mi_archivo.txt', 'r') as f:
    contenido = f.read()
    print(contenido)  # Imprime '¡Hola, mundo!'

#region INFO ADICIONAL SOBRE EL MANEJO DE ARCHIVO

#Manejo de archivos CSV: Python proporciona el módulo csv para leer y escribir archivos CSV (valores separados por comas). Esto es útil para trabajar con datos tabulares2.

#Manejo de archivos JSON: Python proporciona el módulo json para leer y escribir archivos JSON (JavaScript Object Notation). Esto es útil para trabajar con datos estructurados de una manera que es fácil de leer para los humanos y fácil de analizar para las máquinas2.

#Lectura y escritura de archivos de Excel: Con la ayuda de bibliotecas de terceros como openpyxl o pandas, Python puede leer y escribir archivos de Excel. Esto es útil para trabajar con hojas de cálculo2.

#Lectura y escritura de archivos de base de datos: Python puede interactuar con varias bases de datos (como SQLite, MySQL, PostgreSQL, etc.) para leer y escribir datos2.

#Manejo de archivos de configuración: Python puede leer y escribir archivos de configuración, lo que es útil para almacenar configuraciones y preferencias para tu programa2.

#Manejo de archivos de registro: Python proporciona el módulo logging para escribir mensajes de registro en un archivo. Esto es útil para la depuración y el seguimiento de eventos en tu programa2.

#Serialización y deserialización de objetos de Python: Python ofrece la capacidad de serializar y deserializar objetos de Python utilizando módulos como pickle y json. El módulo pickle implementa protocolos binarios para serializar y deserializar una estructura de objetos de Python4.

#Manejo de archivos grandes y múltiples archivos a la vez: Python ofrece técnicas avanzadas para trabajar con archivos grandes y realizar operaciones en múltiples archivos a la vez5.

#Trabajar con archivos comprimidos: Python puede leer y escribir archivos comprimidos, como los archivos ZIP

#endregion

#modulos

#creacion de un modulo

# mi_modulo.py
def hola_mundo():
    print("¡Hola, mundo!")

#uso de un modulo

# app.py
#import mi_modulo

#mi_modulo.hola_mundo()  # Imprime: ¡Hola, mundo!

#importacion de nombres especificos

# app.py
#from mi_modulo import hola_mundo

hola_mundo()  # Imprime: ¡Hola, mundo!

#renombrar modulos

# app.py
#import mi_modulo as mm

#mm.hola_mundo()  # Imprime: ¡Hola, mundo!

#modulos Estandar
# app.py
import math

print(math.pi)  # Imprime: 3.141592653589793


#PROGRAMACION ORIENTADA A OBJETOS

#La programación orientada a objetos (POO) es un paradigma de programación que utiliza objetos y sus interacciones para diseñar aplicaciones y programas de software.

#CLASES Las clases proporcionan un medio de agrupar datos y funcionalidad juntos. Crear una nueva clase crea un nuevo tipo de objeto.

class MiClase:
    variable = "variable"

    def funcion(self):
        print("Esta es una función de la clase.")

#Objetos es una instancia de una clase. Un objeto incluye tanto los datos (el estado del objeto) como los métodos (las funciones que manipulan el objeto).

objeto = MiClase()

#HERENCIA La herencia es una forma de organizar las clases en una jerarquía desde la más general hasta la más específica.

class OtraClase(MiClase):
    pass

#Encapsulamiento El encapsulamiento se refiere a la ocultación de los detalles de implementación de una clase de los usuarios de la clase.

class Coche:
    def __init__(self):
        self.__maxima_velocidad = 200

    def conducir(self):
        print(f'Conduciendo a una velocidad máxima de {self.__maxima_velocidad}')

mi_coche = Coche()
mi_coche.conducir()  # Imprime: Conduciendo a una velocidad máxima de 200

#POLIMORFISMO El polimorfismo permite utilizar una interfaz común para diferentes tipos de datos.

class Coche:
    def conducir(self):
        print("El coche está conduciendo")

class Barco:
    def conducir(self):
        print("El barco está navegando")

def iniciar_viaje(vehiculo):
    vehiculo.conducir()

mi_coche = Coche()
mi_barco = Barco()

iniciar_viaje(mi_coche)  # Imprime: El coche está conduciendo
iniciar_viaje(mi_barco)  # Imprime: El barco está navegando

#METODOS MAGICOS Python ofrece métodos especiales con dos guiones bajos al principio y al final del nombre del método, que puedes definir para añadir “magia” a tus clases. 
# Son operadores de sobrecarga y métodos especiales en clases.

class Ejemplo:
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return f"Valor: {self.valor}"
    
#DECORADORES

class MiClase2:
    @staticmethod
    def metodo_estatico():
        pass

#MIXINS

class Mixin:
    def metodo_mixin(self):
        pass

class OtraClaseMas(Mixin):
    pass


#METACLASES

class Meta(type):
    pass

class MiClase44(metaclass=Meta):
    pass

#self es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables y métodos de la clase.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"Este coche es un {self.marca} {self.modelo}.")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")

# Llamar al método mostrar_informacion
mi_coche.mostrar_informacion()  # Imprime: Este coche es un Toyota Corolla.