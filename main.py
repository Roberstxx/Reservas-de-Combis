import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3  # Para interactuar con la base de datos
from Agregar_combi import CombiApp
from Catalogo_combis import abrir_catalogo
from Reservar_Asientos import ReservaAsientosApp
from Editar_Combi import EditarCombiApp
from Administrar_Usuario import administrar_usuario

# Función para centrar ventanas
def centrar_ventana(ventana, ancho=750, alto=500):
    
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Función para verificar combis registradas en la base de datos
def verificar_combis_registradas():
    """
    Consulta en la base de datos si ya existen combis registradas.

    Returns:
        bool: True si hay combis registradas, False de lo contrario.
    """
    try:
        conexion = sqlite3.connect("combis.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM combis")
        resultado = cursor.fetchone()
        return resultado[0] > 0
    except Exception as e:
        messagebox.showerror("Error", f"Error al consultar la base de datos: {e}")
        return False
    finally:
        if 'conexion' in locals():
            conexion.close()

# Función para actualizar el mensaje dinámico
def actualizar_mensaje():
    """
    Cambia el mensaje de bienvenida dependiendo de si hay combis registradas.
    """
    if verificar_combis_registradas():
        mensaje.config(text="🚐 REGISTRA TU VIAJE 🚐")
    else:
        mensaje.config(text="✨ BIENVENIDO ✨\nAgregue su primera combi")

# Funciones para abrir ventanas secundarias
def abrir_agregar_combi():
    """
    Abre la ventana para agregar una nueva combi y la configura como modal.
    """
    ventana = Toplevel(root)
    ventana.grab_set()  # Modal
    ventana.transient(root)  # Relacionada con la ventana principal
    ventana.title("Agregar Combi")
    app = CombiApp(ventana)
    ventana.protocol("WM_DELETE_WINDOW", lambda: [ventana.destroy(), actualizar_mensaje()])

def editar_combi():
    """
    Abre la ventana para editar una combi y la configura como modal.
    """
    ventana = Toplevel(root)
    ventana.grab_set()
    ventana.transient(root)
    ventana.title("Editar Combi")
    app = EditarCombiApp(ventana)

def abrir_reservar_asientos():
    """
    Abre la ventana para reservar asientos y la configura como modal.
    """
    ventana_reserva = Toplevel(root)
    ventana_reserva.grab_set()
    ventana_reserva.transient(root)
    ventana_reserva.title("Reservar Asientos")
    app_reserva = ReservaAsientosApp(ventana_reserva)
    centrar_ventana(ventana_reserva, 800, 450)  # Centrar la ventana aquí

def abrir_administrar_usuario():
    """
    Abre la ventana para administrar usuarios.
    """
    ventana = Toplevel(root)
    ventana.grab_set()
    ventana.transient(root)
    ventana.title("Administrar Usuario")
    administrar_usuario()

# Función para cerrar la aplicación
def salir():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Combis")
root.configure(bg="#2C2F33")  # Fondo

centrar_ventana(root)

# Crear Frame principal
frame = tk.Frame(root, bg="#2C2F33", padx=20, pady=20)
frame.pack(pady=10)

# Crear Frame para los botones y organizarlos en una línea
botones_frame = tk.Frame(frame, bg="#2C2F33")
botones_frame.pack()

# Estilizar los botones
estilo_boton = {
    "bg": "#7289DA",
    "fg": "white",
    "font": ("Arial", 12, "bold"),
    "relief": "ridge",
    "bd": 3
}

btn_agregar_combi = tk.Button(botones_frame, text="Agregar combi", command=abrir_agregar_combi, **estilo_boton)
btn_agregar_combi.grid(row=0, column=0, padx=8, pady=10)

btn_editar_combi = tk.Button(botones_frame, text="Editar combi", command=editar_combi, **estilo_boton)
btn_editar_combi.grid(row=0, column=1, padx=8, pady=10)

btn_reserva_asientos = tk.Button(botones_frame, text="Registrar viaje", command=abrir_reservar_asientos, **estilo_boton)
btn_reserva_asientos.grid(row=0, column=2, padx=8, pady=10)

btn_catalogo = tk.Button(botones_frame, text="Catálogo", command=abrir_catalogo, **estilo_boton)
btn_catalogo.grid(row=0, column=3, padx=8, pady=10)

btn_administrar_usuario = tk.Button(botones_frame, text="Administrar usuario", command=abrir_administrar_usuario, **estilo_boton)
btn_administrar_usuario.grid(row=0, column=4, padx=8, pady=10)

btn_salir = tk.Button(root, text="Salir", command=salir, **estilo_boton)
btn_salir.pack(pady=20)

# Crear el mensaje dinámico
mensaje = tk.Label(
    root,
    text="✨ BIENVENIDO ✨\nAgregue su primera combi",
    font=("Arial", 16, "bold"),
    fg="#F1C40F",
    bg="#2C2F33",
    padx=10,
    pady=10
)
mensaje.pack(pady=20)

# Actualizar el mensaje al iniciar la aplicación
actualizar_mensaje()

root.mainloop()

