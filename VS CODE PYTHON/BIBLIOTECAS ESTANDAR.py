#COLLECTIONS

'''Esta biblioteca de Python proporciona alternativas a los contenedores incorporados de Python, 
como dict, list, set y tuple. Implementa tipos de contenedores especializados que proporcionan 
alternativas a los contenedores generales incorporados de Python.'''

from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict

# namedtuple
# Descripción: Es una función de fábrica para crear subclases de tuplas con campos nombrados.
# Uso: Se utiliza cuando necesitas una tupla, pero también quieres que los campos tengan nombres para hacer tu código más legible y auto-documentado.
Color = namedtuple('Color', ['red', 'green', 'blue'])
pixel = Color(60, 170, 200)
print("namedtuple:", pixel.red)

# deque
# Descripción: Es un contenedor similar a una lista con adiciones y eliminaciones rápidas en ambos extremos.
# Uso: Se utiliza cuando necesitas agregar o eliminar elementos de manera eficiente en cualquier lado de una lista.
d = deque('ghi')
d.append('j')
d.appendleft('f')
print("deque:", d)

# ChainMap
# Descripción: Es una clase similar a `dict` que te permite vincular rápidamente una serie de mapeos para que puedan tratarse como una sola unidad.
# Uso: Se utiliza cuando necesitas combinar varios diccionarios en uno solo, pero sin combinar realmente los diccionarios.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 3, 'date': 4, 'apple': 5}
combined_dict = ChainMap(dict1, dict2)
print("ChainMap:", combined_dict['apple'])

# Counter
# Descripción: Es una subclase de `dict` para contar objetos hashable.
# Uso: Se utiliza cuando necesitas contar la ocurrencia de diferentes objetos en una colección.
c = Counter('hello world')
print("Counter:", c)

# OrderedDict
# Descripción: Es una subclase de `dict` que recuerda el orden de las entradas que se agregaron.
# Uso: Se utiliza cuando el orden de inserción es importante para tu código.
d = OrderedDict()
d['apple'] = 1
d['banana'] = 2
print("OrderedDict:", d)

# defaultdict
# Descripción: Es una subclase de `dict` que llama a una función de fábrica para suministrar valores faltantes.
# Uso: Se utiliza cuando quieres un valor predeterminado para las claves que aún no existen en el diccionario.
d = defaultdict(int)
print("defaultdict:", d['apple'])

# UserDict
# Descripción: Son envoltorios alrededor de los objetos de diccionario, lista y cadena, respectivamente, para facilitar la creación de subclases.
# Uso: Se utilizan para facilitar la creación de subclases de los objetos de diccionario, lista y cadena, respectivamente.
d = UserDict({'apple': 1, 'banana': 2})
print("UserDict:", d)


#CSV

'''Esta biblioteca se utiliza para leer y escribir datos en formato CSV (valores separados por comas), 
que es el formato más común para importar y exportar datos de hojas de cálculo y bases de datos. 
Proporciona funcionalidades para leer y escribir datos en formato CSV, permitiendo a los programadores 
decir “escribe estos datos en el formato preferido por Excel” o “lee datos de este archivo que fue generado por Excel”, 
sin conocer los detalles precisos del formato CSV utilizado por Excel.'''

import csv

# csv.reader
# Descripción: Retorna un objeto reader que iterará sobre las líneas del `csvfile` proporcionado.
# Uso: Se utiliza para leer datos de un archivo CSV.
with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("csv.reader:", row)

# csv.writer
# Descripción: Retorna un objeto writer que convierte los datos del usuario en cadenas delimitadas y las escribe en un objeto con el método `write()`.
# Uso: Se utiliza para escribir datos en un archivo CSV.
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])


#MATPLOTLIB

'''Es una biblioteca de Python para la creación de visualizaciones estáticas, animadas e interactivas. 
Matplotlib facilita la creación de gráficos de calidad para publicaciones, figuras interactivas que 
pueden hacer zoom, paneo, actualización, y permite personalizar el estilo visual y el diseño.'''

import matplotlib.pyplot as plt
import numpy as np

# plot()
# Descripción: Esta función se utiliza para dibujar líneas a partir de puntos x e y.
# Uso: Se utiliza para crear gráficos de líneas.
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# scatter()
# Descripción: Esta función crea un gráfico de dispersión.
# Uso: Se utiliza para crear gráficos de dispersión, que son útiles cuando tienes un montón de datos que quieres trazar, pero quieres que sean representados como puntos individuales en lugar de líneas conectadas.
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.show()

# bar()
# Descripción: Esta función se utiliza para crear gráficos de barras.
# Uso: Los gráficos de barras son útiles cuando quieres comparar una sola categoría de datos entre grupos individuales subcategorías.
languages =['Python', 'Java', 'C', 'C++', 'JavaScript']
popularity = [56, 39, 34, 34, 29]
plt.bar(languages, popularity)
plt.show()

# hist()
# Descripción: Esta función se utiliza para crear histogramas.
# Uso: Los histogramas son útiles cuando necesitas una representación gráfica de los datos y su distribución de frecuencia.
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

# pie()
# Descripción: Esta función se utiliza para crear gráficos de pastel.
# Uso: Los gráficos de pastel muestran el tamaño de los elementos en una serie de datos, proporcional a la suma de los elementos.
sizes = [25, 20, 45, 10]
labels = ['Cats', 'Dogs', 'Tigers', 'Goats']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()


#NUMPY

'''Es una biblioteca de Python que proporciona un objeto de matriz N-dimensional potente y funciones matemáticas avanzadas. 
NumPy es esencial para la computación científica con Python y se utiliza para realizar operaciones en arrays multidimensionales de manera eficiente.'''

#np.array: Crea un array a partir de una lista o tupla1.
#np.empty: Crea un array sin inicializar de una forma y tipo específicos2.
#np.zeros: Crea un array lleno de ceros3.
#np.ones: Crea un array lleno de unos4.
#np.full: Crea un array de una forma y tipo específicos, lleno de un valor determinado5.
#np.identity: Crea una matriz identidad6.
#np.arange: Crea un array con valores espaciados uniformemente dentro de un intervalo dado7.
#np.linspace: Crea un array con muestras numéricas espaciadas uniformemente en un intervalo especificado8.
#np.random.rand: Crea un array de la forma dada y lo llena con muestras aleatorias de una distribución uniforme en el intervalo [0, 1)9.
#np.reshape: Da una nueva forma a un array sin cambiar sus datos
#np.append: Añade valores al final de un arra
#np.delete: Devuelve un nuevo array con subarrays a lo largo de un eje eliminados
#np.concatenate: Une una secuencia de arrays a lo largo de un eje existente
#np.split: Divide un array en múltiples subarrays de igual tamaño
#np.transpose: Permuta las dimensiones de un array
#np.dot: Calcula el producto de dos arrays
#np.sqrt: Devuelve la raíz cuadrada de cada elemento del array
#np.sin: Calcula el seno de cada elemento del array
#np.cos: Calcula el coseno de cada elemento del array
#np.log: Calcula el logaritmo natural de cada elemento del array
...


#OS

'''La biblioteca OS en Python proporciona una forma versátil de usar funcionalidades dependientes del sistema operativo'''

#os.getcwd(): Este método devuelve el directorio de trabajo actual.
#os.chdir(path): Este método cambia el directorio de trabajo actual a la ruta especificada.
#os.system(command): Este método ejecuta el comando (una cadena) en un subproceso.
#os.name: Este atributo devuelve el nombre del módulo dependiente del sistema operativo importado.
#os.error: Es un alias de la excepción incorporada OSError.
#os.popen(): Este método se utiliza para abrir una tubería hacia o desde el comando.
#os.fork(): Este método se utiliza para crear un proceso secundario.
#os.execv(): Este método se utiliza para reiniciar un programa en Python.
#os.spawnp(): Esta función se utiliza para crear nuevos procesos.


#SYS

'''La biblioteca sys en Python es un módulo incorporado que proporciona acceso a algunas variables y funciones que interactúan fuertemente con el intérprete de Python.'''

#sys.argv: Es una lista en Python, que contiene los argumentos de línea de comandos pasados a un script. Con la ayuda de sys.argv, 
#    puedes pasar argumentos a tu script de Python desde la línea de comandos.
#sys.exit(): Esta función permite salir del programa Python. Esto es especialmente relevante para programas que tienen una condición de salida.
#sys.version: Es una cadena que contiene el número de versión del intérprete de Python y otra información adicional sobre el número de compilación y el compilador utilizado.
#sys.path: Es una lista de cadenas que especifica la ruta de búsqueda para los módulos. Inicializado desde la variable de entorno PYTHONPATH, 
#    además de un conjunto predeterminado de rutas.
#sys.platform: Esta función se utiliza para obtener el nombre de la plataforma en la que se está ejecutando Python.
#sys.stdin: Se utiliza para la entrada estándar interactiva. Por ejemplo, la entrada del teclado.
#sys.stdout: Se utiliza para la salida estándar. Por ejemplo, imprimir en la consola.
#sys.stderr: Se utiliza para la salida de error estándar. Por ejemplo, imprimir mensajes de error en la consola.
#sys.exc_info(): Esta función devuelve una tupla que contiene información sobre la excepción que se está manejando actualmente.


#REQUESTS

'''La biblioteca requests de Python es una biblioteca poderosa y fácil de usar para hacer solicitudes HTTP. Proporciona métodos para enviar solicitudes 
HTTP utilizando los verbos más comunes, y también ofrece funcionalidad para manejar aspectos de la comunicación HTTP como cookies y encabezados.'''

#requests.get(url, params=None, **kwargs): Este método envía una solicitud GET al URL especificado1. Puedes pasar parámetros opcionales a la solicitud a través del 
#    argumento params1.
#requests.post(url, data=None, json=None, **kwargs): Este método envía una solicitud POST al URL especificado2. Puedes enviar datos a través del cuerpo 
#    de la solicitud usando los argumentos data o json2.
#requests.put(url, data=None, **kwargs): Este método envía una solicitud PUT al URL especificado3. Al igual que con post(), puedes enviar datos a través del 
#    cuerpo de la solicitud3.
#requests.patch(url, data=None, **kwargs): Este método envía una solicitud PATCH al URL especificado4. Puedes enviar datos a través del cuerpo de la solicitud4.
#requests.delete(url, **kwargs): Este método envía una solicitud DELETE al URL especificado5.
#requests.head(url, **kwargs): Este método envía una solicitud HEAD al URL especificado6. Se utiliza para obtener los encabezados HTTP6.
#requests.options(url, **kwargs): Este método envía una solicitud OPTIONS al URL especificado7. Se utiliza para obtener las opciones de
#    comunicación disponibles para un URL dado7.
#requests.request(method, url, **kwargs): Este método es un método más general que puede enviar una solicitud 
#    HTTP de cualquier tipo (GET, POST, PUT, DELETE, etc.) al URL especificado8.
#requests.session(): Este método crea una sesión que permite persistir ciertos parámetros a través de las solicitudes9. 
#    Esto puede ser útil para cosas como mantener las cookies entre solicitudes9


#SIGUIETNE