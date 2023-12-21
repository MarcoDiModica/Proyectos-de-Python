import tkinter as tk
from tkinter import filedialog, messagebox, ttk, font
import os
from send2trash import send2trash
import ctypes
import getpass
import sys

windowlen = 440

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if not is_admin():
#     # Re-lanza el programa con privilegios de admin
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Función para limpiar una ubicación
def limpiar_ubicacion(ubicacion):
    try:
        # Verifica si la ruta existe
        if not os.path.exists(ubicacion):
            raise FileNotFoundError(f"No se encontró la ubicación: {ubicacion}")
        # Envía los archivos a la papelera
        send2trash(ubicacion)
        messagebox.showinfo("Limpiar", f"Se limpió la ubicación: {ubicacion}")
    except FileNotFoundError as fnf_error:
        messagebox.showerror("Error", f"No se encontró la ubicación: {ubicacion}\nError: {str(fnf_error)}")
    except OSError as os_error:
        messagebox.showerror("Error", f"No se pudo eliminar el archivo en la ubicación: {ubicacion}\nError: {str(os_error)}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado al limpiar la ubicación: {ubicacion}\nError: {str(e)}")

# Función para ejecutar la limpieza
def ejecutar_limpieza():
    # Verifica si se tienen permisos de administrador
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showerror("Error", "Se requieren permisos de administrador para ejecutar la limpieza.")
        return

    # Obtiene las ubicaciones seleccionadas
    ubicaciones_seleccionadas = []
    for ubicacion, data in ubicaciones_vars.items():
        if data['var'].get():
            ubicaciones_seleccionadas.append(data['ruta'])

    # Crea una nueva ventana para la barra de progreso
    progress_window = tk.Toplevel(window)
    progress_window.title("Progreso de la limpieza")
    progress_window.geometry("320x100")

    # Configura la barra de progreso
    progress = ttk.Progressbar(progress_window, length=200, mode='determinate')
    progress.pack()

    progress['maximum'] = len(ubicaciones_seleccionadas)
    progress['value'] = 0

    # Limpia las ubicaciones seleccionadas
    for ubicacion in ubicaciones_seleccionadas:
        limpiar_ubicacion(ubicacion)
        progress['value'] += 1

    # Resetea la barra de progreso
    progress['value'] = 0

    # Cierra la ventana de progreso
    progress_window.destroy()

# Función para agregar una ubicación
def agregar_ubicacion():
    global windowlen
    ubicacion = filedialog.askdirectory()
    if ubicacion:
        var = tk.IntVar()
        ubicaciones_vars[ubicacion] = var
        checkbox = tk.Checkbutton(window, text=ubicacion, variable=var)
        checkbox.pack()
        windowlen += 20
        # Ajusta el tamaño de la ventana en función del número de casillas de verificación
        window.geometry(f"320x{windowlen}")


# Crea la ventana principal
window = tk.Tk()
window.title("Limpieza de archivos")
window.geometry(f"320x{windowlen}")
window.resizable(False, False)
window.configure(bg="white")

helv36 = font.Font(family='Helvetica', size=10, weight='bold')

# Obtén el nombre de usuario actual
username = getpass.getuser()

# Variables de control para las casillas de verificación de las ubicaciones
ubicaciones_vars = {
    "Archivos Temporales 1": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\Temp",
        "var": tk.IntVar()
    },
    "Archivos Temporales 2": {
        "ruta": f"C:\\Windows\\Temp",
        "var": tk.IntVar()
    },
    "Papelera de reciclaje": {
        "ruta": f"C:\\$Recycle.Bin",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Windows\\INetCache",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet (Edge)": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet (Chrome)": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet (Firefox)": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\Mozilla\\Firefox\\Profiles",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet (Opera)": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Cache",
        "var": tk.IntVar()
    },
    "Archivos Temporales de Internet (Brave)": {
        "ruta": f"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache",
        "var": tk.IntVar()
    },

    # Agrega más ubicaciones aquí
}

# Etiqueta de selección de ubicaciones
label = tk.Label(window, text="Selecciona las ubicaciones a limpiar:", font=helv36, bg="white")
label.pack(pady=10)

# Crea una casilla de verificación para cada ubicación
for ubicacion, data in ubicaciones_vars.items():
    checkbox = tk.Checkbutton(window, text=ubicacion, variable=data['var'], bg="white", font=helv36)
    checkbox.pack(pady=2)

# Barra de progreso
progress = ttk.Progressbar(window, length=200, mode='determinate')
progress.pack(pady=10)

# Botón de agregar
button = tk.Button(window, text="Agregar", command=agregar_ubicacion, font=helv36, bg="lightgray")
button.pack(pady=5)

# Botón de ejecutar
button = tk.Button(window, text="Ejecutar", command=ejecutar_limpieza, bg='lightgray', font=helv36)
button.pack(pady=5)

# Inicia el bucle de la interfaz de usuario
window.mainloop()