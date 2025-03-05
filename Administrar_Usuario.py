import tkinter as tk
from tkinter import messagebox

def administrar_usuario():
    ventana = tk.Toplevel()
    ventana.title("Administrar Usuario")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Usuario").pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)
    
    tk.Label(ventana, text="Nueva Contraseña").pack(pady=5)
    entry_password = tk.Entry(ventana, show="*")
    entry_password.pack(pady=5)
    
    tk.Label(ventana, text="Confirmar Contraseña").pack(pady=5)
    entry_confirm_password = tk.Entry(ventana, show="*")
    entry_confirm_password.pack(pady=5)
    
    def guardar_cambios():
        usuario = entry_usuario.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
        
        if not usuario:
            messagebox.showerror("Error", "El usuario no puede estar vacío")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        messagebox.showinfo("Éxito", f"Usuario '{usuario}' actualizado correctamente")
        ventana.destroy()
    
    tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    administrar_usuario()
    root.mainloop()
