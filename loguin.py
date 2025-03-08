import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

ARCHIVO_USUARIOS = "usuarios.txt"

# Cargar usuarios desde un archivo
def cargar_usuarios():
    if not os.path.exists(ARCHIVO_USUARIOS):
        return {}
    with open(ARCHIVO_USUARIOS, "r") as f:
        return dict(line.strip().split(",") for line in f)

# Guardar usuarios en un archivo
def guardar_usuario(usuario, password):
    with open(ARCHIVO_USUARIOS, "a") as f:
        f.write(f"{usuario},{password}\n")

usuarios_registrados = cargar_usuarios()

# Función para borrar texto por defecto
def on_entry_click(event, entry, texto_default, ocultar=False):
    if entry.get() == texto_default:
        entry.delete(0, tk.END)
        if ocultar:
            entry.config(show="*")  # Oculta la contraseña

# Función para restaurar texto por defecto
def on_focus_out(event, entry, texto_default, ocultar=False):
    if entry.get() == "":
        entry.insert(0, texto_default)
        if ocultar:
            entry.config(show="")  # Muestra el texto normal

# Mostrar pantalla de registro
def mostrar_registro():
    login_frame.pack_forget()
    registro_frame.pack()

# Mostrar pantalla de login
def mostrar_login():
    registro_frame.pack_forget()
    login_frame.pack()

# Validar entrada
def validar_entrada(usuario, password):
    if not usuario or not password:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return False
    return True

# Registrar usuario
def crear_cuenta():
    usuario = entry_usuario_reg.get().strip()
    password = entry_password_reg.get().strip()
    confirm_password = entry_confirmar_reg.get().strip()
    
    if not validar_entrada(usuario, password):
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return
    
    if usuario in usuarios_registrados:
        messagebox.showerror("Error", "El usuario ya existe")
        return
    
    usuarios_registrados[usuario] = password
    guardar_usuario(usuario, password)
    messagebox.showinfo("Éxito", "Cuenta creada con éxito")
    mostrar_login()

# Iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get().strip()
    password = entry_password.get().strip()
    
    if not validar_entrada(usuario, password):
        return
    
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == password:
        messagebox.showinfo("Inicio de sesión", f"Bienvenido, {usuario}!")
        root.destroy()  # Cierra la ventana de login
        subprocess.run(["python", "main.py"])  # Ejecuta el sistema principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear ventana
root = tk.Tk()
root.title("Login y Registro")
root.geometry("300x400")
root.resizable(False, False)

# --------- LOGIN FRAME ---------
login_frame = tk.Frame(root)
login_frame.pack(expand=True)

# Imagen
img = Image.open("assets/side-img.png").resize((100, 100))
img = ImageTk.PhotoImage(img)
tk.Label(login_frame, image=img).pack(pady=10)

# Entradas de usuario y contraseña
entry_usuario = tk.Entry(login_frame, width=30, justify="center")
entry_usuario.pack(pady=5)
entry_usuario.insert(0, "Usuario")
entry_usuario.bind("<FocusIn>", lambda event: on_entry_click(event, entry_usuario, "Usuario"))
entry_usuario.bind("<FocusOut>", lambda event: on_focus_out(event, entry_usuario, "Usuario"))

entry_password = tk.Entry(login_frame, width=30, justify="center")
entry_password.pack(pady=5)
entry_password.insert(0, "Contraseña")
entry_password.bind("<FocusIn>", lambda event: on_entry_click(event, entry_password, "Contraseña", ocultar=True))
entry_password.bind("<FocusOut>", lambda event: on_focus_out(event, entry_password, "Contraseña", ocultar=True))

# Botón de inicio de sesión
tk.Button(login_frame, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=10)

# Enlace a registro
tk.Label(login_frame, text="¿No tienes cuenta?").pack()
tk.Button(login_frame, text="Regístrate", fg="blue", bd=0, command=mostrar_registro).pack()

# --------- REGISTRO FRAME ---------
registro_frame = tk.Frame(root)

tk.Label(registro_frame, text="Registro", font=("Arial", 14)).pack(pady=10)

entry_usuario_reg = tk.Entry(registro_frame, width=30, justify="center")
entry_usuario_reg.pack(pady=5)
entry_usuario_reg.insert(0, "Usuario")
entry_usuario_reg.bind("<FocusIn>", lambda event: on_entry_click(event, entry_usuario_reg, "Usuario"))
entry_usuario_reg.bind("<FocusOut>", lambda event: on_focus_out(event, entry_usuario_reg, "Usuario"))

entry_password_reg = tk.Entry(registro_frame, width=30, justify="center")
entry_password_reg.pack(pady=5)
entry_password_reg.insert(0, "Contraseña")
entry_password_reg.bind("<FocusIn>", lambda event: on_entry_click(event, entry_password_reg, "Contraseña", ocultar=True))
entry_password_reg.bind("<FocusOut>", lambda event: on_focus_out(event, entry_password_reg, "Contraseña", ocultar=True))

entry_confirmar_reg = tk.Entry(registro_frame, width=30, justify="center")
entry_confirmar_reg.pack(pady=5)
entry_confirmar_reg.insert(0, "Confirmar Contraseña")
entry_confirmar_reg.bind("<FocusIn>", lambda event: on_entry_click(event, entry_confirmar_reg, "Confirmar Contraseña", ocultar=True))
entry_confirmar_reg.bind("<FocusOut>", lambda event: on_focus_out(event, entry_confirmar_reg, "Confirmar Contraseña", ocultar=True))

# Botones de registro
tk.Button(registro_frame, text="Crear Cuenta", command=crear_cuenta).pack(pady=10)
tk.Button(registro_frame, text="Volver", command=mostrar_login).pack()

# Mostrar pantalla de login al iniciar
root.mainloop()

