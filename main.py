import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from Agregar_combi import CombiApp  # Importar la clase


def abrir_agregar_combi():
    ventana = Toplevel()  # Crear una nueva ventana
    app = CombiApp(ventana)  # Iniciar la interfaz en la nueva ventana
    ventana.mainloop()

def editar_combi():
    ventana = tk.Toplevel(root)
    ventana.title("Editar Combi")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Formulario para Editar Combi").pack(pady=20)

def costo_ruta():
    ventana = tk.Toplevel(root)
    ventana.title("Costo de Ruta")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Formulario para Costo de Ruta").pack(pady=20)

def registrar_viaje():
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Viaje")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Formulario para Registrar Viaje").pack(pady=20)

def catalogo():
    ventana = tk.Toplevel(root)
    ventana.title("Catálogo")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Sección de Catálogo").pack(pady=20)

def administrar_usuario():
    ventana = tk.Toplevel(root)
    ventana.title("Administrar Usuario")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Administración de Usuarios").pack(pady=20)

def salir():
    root.quit()

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Combis")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_agregar_combi = tk.Button(frame, text="Agregar combi", command=abrir_agregar_combi)
btn_agregar_combi.grid(row=0, column=0, padx=5, pady=5)


btn_editar = tk.Button(frame, text="Editar combi", command=editar_combi)
btn_editar.grid(row=1, column=0, padx=5, pady=5)

btn_costo_ruta = tk.Button(frame, text="Costo de ruta", command=costo_ruta)
btn_costo_ruta.grid(row=0, column=1, padx=5, pady=5)

btn_registrar_viaje = tk.Button(frame, text="Registrar viaje", command=registrar_viaje)
btn_registrar_viaje.grid(row=0, column=2, padx=5, pady=5)

btn_catalogo = tk.Button(frame, text="Catálogo", command=catalogo)
btn_catalogo.grid(row=0, column=3, padx=5, pady=5)

btn_admin_usuario = tk.Button(frame, text="Administrar usuario", command=administrar_usuario)
btn_admin_usuario.grid(row=0, column=4, padx=5, pady=5)

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.pack(pady=10)

mensaje = tk.Label(root, text="BIENVENIDO\nAgregue su primera combi", font=("Arial", 12))
mensaje.pack(pady=20)

root.mainloop()
