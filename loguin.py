import tkinter as tk
from tkinter import messagebox
import sqlite3

def centrar_ventana(ventana, ancho=400, alto=300):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def administrar_usuario():
    ventana = tk.Toplevel()
    ventana.title("Administrar Usuario")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Usuario").pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)

    tk.Label(ventana, text="Contraseña Anterior").pack(pady=5)
    entry_password_anterior = tk.Entry(ventana, show="*")
    entry_password_anterior.pack(pady=5)

    tk.Label(ventana, text="Nueva Contraseña").pack(pady=5)
    entry_password = tk.Entry(ventana, show="*")
    entry_password.pack(pady=5)

    tk.Label(ventana, text="Confirmar Contraseña").pack(pady=5)
    entry_confirm_password = tk.Entry(ventana, show="*")
    entry_confirm_password.pack(pady=5)

    def guardar_cambios():
        usuario = entry_usuario.get()
        password_anterior = entry_password_anterior.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()

        if not usuario:
            messagebox.showerror("Error", "El usuario no puede estar vacío")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return

        try:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (usuario,))
            resultado = cursor.fetchone()

            if resultado:
                if resultado[0] == password_anterior:
                    cursor.execute("UPDATE usuarios SET password = ? WHERE usuario = ?", (password, usuario))
                    conn.commit()
                    messagebox.showinfo("Éxito", f"Usuario '{usuario}' actualizado correctamente")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "Contraseña anterior incorrecta")
            else:
                messagebox.showerror("Error", "Usuario no encontrado")

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error de base de datos: {e}")

    tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

    centrar_ventana(ventana)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    administrar_usuario()
