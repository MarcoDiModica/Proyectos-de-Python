import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sqlite3

# Configuración inicial
N = 50  # Tamaño de la cuadrícula NxN
ON = 255  # Nodo encendido
OFF = 0  # Nodo apagado
vals = [ON, OFF]  # Valores de los nodos

# Población inicial (probabilidad de que una celda esté encendida)
poblacion_inicial = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

# Contador de generaciones
generaciones = 0

# Velocidad de la animación (en milisegundos)
velocidad = 50

# Colores personalizables
color_vivo = 'black'
color_muerto = 'white'

# Conexión a la base de datos
conn = sqlite3.connect('juego_vida.db')
c = conn.cursor()

# Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS estados
          (generacion integer, estado text)''')

def guardar_estado():
    # Convertir la población a una cadena de texto
    estado = ''.join(map(str, poblacion_inicial.flatten()))
    # Insertar el estado en la base de datos
    c.execute("INSERT INTO estados VALUES (?, ?)", (generaciones, estado))
    conn.commit()

def cargar_ultima_generacion():
    # Obtener la última generación de la base de datos
    c.execute("SELECT generacion FROM estados ORDER BY generacion DESC LIMIT 1")
    generacion = c.fetchone()[0]
    # Obtener el estado de la base de datos
    c.execute("SELECT estado FROM estados WHERE generacion=?", (generacion,))
    estado = c.fetchone()[0]
    # Convertir la cadena de texto a una matriz numpy
    poblacion_inicial = np.array(list(map(int, estado))).reshape((N, N))

def cargar_estado(generacion):
    # Obtener el estado de la base de datos
    c.execute("SELECT estado FROM estados WHERE generacion=?", (generacion,))
    estado = c.fetchone()[0]
    # Convertir la cadena de texto a una matriz numpy
    poblacion_inicial = np.array(list(map(int, estado))).reshape((N, N))

def actualizar(data):
  global poblacion_inicial, generaciones
  # Copia de la población inicial
  nueva_poblacion = poblacion_inicial.copy()
  # Iterar por cada celda
  for i in range(N):
    for j in range(N):
      # Calcular la suma total de los vecinos
      total = int((poblacion_inicial[i, (j-1)%N] + poblacion_inicial[i, (j+1)%N] +
                  poblacion_inicial[(i-1)%N, j] + poblacion_inicial[(i+1)%N, j] +
                  poblacion_inicial[(i-1)%N, (j-1)%N] + poblacion_inicial[(i-1)%N, (j+1)%N] +
                  poblacion_inicial[(i+1)%N, (j-1)%N] + poblacion_inicial[(i+1)%N, (j+1)%N])/255)
      # Reglas del Juego de la Vida
      if poblacion_inicial[i, j]  == ON:
        if (total < 2) or (total > 3):
          nueva_poblacion[i, j] = OFF
      else:
        if total == 3:
          nueva_poblacion[i, j] = ON
  # Actualizar la población
  poblacion_inicial = nueva_poblacion
  mat.set_data(poblacion_inicial)
  generaciones += 1  # Incrementar el contador de generaciones
  plt.title("Generaciones: " + str(generaciones))
  return [mat]

# Configurar la animación
fig, ax = plt.subplots()
cmap = plt.cm.colors.ListedColormap([color_muerto, color_vivo])
mat = ax.matshow(poblacion_inicial, cmap=cmap)
ani = animation.FuncAnimation(fig, actualizar, interval=velocidad, save_count=50)

# Interactividad
def onclick(event):
    # Obtener las coordenadas del clic
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        # Convertir las coordenadas a enteros
        x, y = int(x), int(y)
        # Cambiar el estado de la celda
        poblacion_inicial[y, x] = ON if poblacion_inicial[y, x] == OFF else OFF
        # Actualizar la visualización
        mat.set_data(poblacion_inicial)
        fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()