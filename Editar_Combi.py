import tkinter as tk
from tkinter import simpledialog, messagebox, Canvas, filedialog
from PIL import Image, ImageTk
import os

class EditarCombiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editar Combis")
        self.root.configure(bg="#2C2F33")
        
        self.frame = tk.Frame(root, padx=20, pady=20, bg="#2C2F33")
        self.frame.pack()
        
        self.btn_atras = tk.Button(self.frame, text="← Atrás", width=20, bg="#7289DA", fg="white", font=("Arial", 10, "bold"),
                                   command=self.root.destroy)
        self.btn_atras.grid(row=0, column=0, sticky='w', pady=5)
        
        self.label_titulo = tk.Label(self.frame, text="Editar Combi", font=("Arial", 16, "bold"), fg="white", bg="#2C2F33")
        self.label_titulo.grid(row=0, column=1, columnspan=2)
        
        self.combis = self.cargar_combis()
        
        self.label_seleccionar = tk.Label(self.frame, text="Seleccionar combi:", fg="white", bg="#2C2F33")
        self.label_seleccionar.grid(row=1, column=0, pady=5)
        
        self.combi_var = tk.StringVar()
        self.combi_menu = tk.OptionMenu(self.frame, self.combi_var, *self.combis, command=self.cargar_datos_combi)
        self.combi_menu.grid(row=1, column=1, pady=5)
        
        self.entries = {}
        info_labels = ["Rutas", "Horarios", "Placas", "Modelo", "Marca"]
        
        for i, label in enumerate(info_labels):
            lbl = tk.Label(self.frame, text=label, width=20, fg="white", bg="#2C2F33")
            lbl.grid(row=2+i, column=0, pady=2)
            entry = tk.Entry(self.frame, width=22, bg="#99AAB5", fg="black")
            entry.grid(row=2+i, column=1, pady=2)
            self.entries[label] = entry
        
        self.btn_guardar = tk.Button(self.frame, text="Guardar cambios", width=22, bg="#43B581", fg="white", font=("Arial", 10, "bold"),
                                      command=self.guardar_cambios)
        self.btn_guardar.grid(row=8, column=0, columnspan=2, pady=10)
        
        if self.combis:
            self.combi_var.set(self.combis[0])
            self.cargar_datos_combi(self.combis[0])
        
    def cargar_combis(self):
        combis = []
        if os.path.exists("combi_info.txt"):
            with open("combi_info.txt", "r") as file:
                for line in file:
                    if line.startswith("Nombre: "):
                        combis.append(line.split(": ")[1].strip())
        return combis
        
    def cargar_datos_combi(self, combi_nombre):
        datos = {}
        with open("combi_info.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith("Nombre: ") and lines[i].strip().split(": ")[1] == combi_nombre:
                    datos["Nombre"] = combi_nombre
                    i += 1
                    while i < len(lines) and ": " in lines[i]:
                        key, value = lines[i].strip().split(": ", 1)
                        datos[key] = value
                        i += 1
                    break
                i += 1
        
        for key in self.entries:
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, datos.get(key, ""))
        
    def guardar_cambios(self):
        nombre_combi = self.combi_var.get()
        if not nombre_combi:
            messagebox.showerror("Error", "Seleccione una combi para editar.")
            return
        
        nuevos_datos = {k: v.get() for k, v in self.entries.items()}
        
        with open("combi_info.txt", "r") as file:
            lines = file.readlines()
        
        with open("combi_info.txt", "w") as file:
            i = 0
            while i < len(lines):
                if lines[i].startswith("Nombre: ") and lines[i].strip().split(": ")[1] == nombre_combi:
                    file.write(f"Nombre: {nombre_combi}\n")
                    for key, value in nuevos_datos.items():
                        file.write(f"{key}: {value}\n")
                    i += 1
                    while i < len(lines) and ": " in lines[i]:
                        i += 1
                else:
                    file.write(lines[i])
                    i += 1
        
        messagebox.showinfo("Éxito", "Combi actualizada correctamente.")
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = EditarCombiApp(root)
    root.mainloop()
