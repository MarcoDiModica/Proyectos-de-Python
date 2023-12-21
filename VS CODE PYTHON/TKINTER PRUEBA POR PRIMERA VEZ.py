import random as rd
import tkinter as tk
from tkinter import messagebox

def mostrar_maximo(event):
    label_max.pack(padx=5, pady=1)
    entry_max.pack(padx=5, pady=1)
    entry_max.focus()

def mostrar_numero(event):
    label_num.pack(padx=5, pady=1)
    entry_num.pack(padx=5, pady=1)
    entry_num.focus()

def calcular_proximidad(event):
    minimo = int(entry_min.get())
    maximo = int(entry_max.get())
    numero = int(entry_num.get())
    numero_aleatorio = rd.randint(minimo, maximo)
    diferencia = abs(numero - numero_aleatorio)
    rango = maximo - minimo
    proximidad = (rango - diferencia) / rango * 100
    mostrar_grafico(proximidad, numero_aleatorio)
    reiniciar()

def mostrar_grafico(proximidad, numero_aleatorio):
    grafico = tk.Toplevel(root)
    grafico.title("Gráfico de proximidad")
    canvas = tk.Canvas(grafico, width=200, height=200)
    canvas.pack()
    canvas.create_oval(50, 50, 150, 150)  # Círculo exterior
    canvas.create_arc(50, 50, 150, 150, start=90, extent=-360*proximidad/100, fill="blue", outline="")  # Arco de proximidad
    canvas.create_oval(70, 70, 130, 130, fill='white')  # Círculo interior
    grafico.after(1000, lambda: messagebox.showinfo("Resultado", f"Tu número está al {proximidad}% de proximidad al número aleatorio {numero_aleatorio}.", parent=grafico))

def reiniciar():
    entry_min.delete(0, tk.END)
    entry_max.delete(0, tk.END)
    entry_num.delete(0, tk.END)
    label_max.pack_forget()
    entry_max.pack_forget()
    label_num.pack_forget()
    entry_num.pack_forget()
    entry_min.focus()

root = tk.Tk()
root.title("Adivina el número")
root.geometry("200x300")

label_min = tk.Label(root, text="Mínimo:")
label_min.pack(padx=5, pady=1)
entry_min = tk.Entry(root)
entry_min.pack(padx=5, pady=1)
entry_min.bind("<Return>", mostrar_maximo)
entry_min.focus()

label_max = tk.Label(root, text="Máximo:")
entry_max = tk.Entry(root)
entry_max.bind("<Return>", mostrar_numero)

label_num = tk.Label(root, text="Tu número:")
entry_num = tk.Entry(root)
entry_num.bind("<Return>", calcular_proximidad)

root.mainloop()
