import tkinter as tk
from tkinter import simpledialog, messagebox, Canvas

class CombiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agrega tu combi")
        self.root.configure(bg="#2C2F33")  # Fondo oscuro
        
        # Marco principal
        self.frame = tk.Frame(root, padx=20, pady=20, bg="#2C2F33")
        self.frame.pack()
        
        # Botón de regreso
        self.btn_atras = tk.Button(self.frame, text="← Atrás", width=20, bg="#7289DA", fg="white", font=("Arial", 10, "bold"),
                                   command=self.root.quit)
        self.btn_atras.grid(row=0, column=0, sticky='w', pady=5)
        
        # Título
        self.label_titulo = tk.Label(self.frame, text="Agrega tu combi", font=("Arial", 16, "bold"), fg="white", bg="#2C2F33")
        self.label_titulo.grid(row=0, column=1, columnspan=2)
        
        # Nombre de la combi (editable)
        self.combi_nombre = tk.StringVar(value="Combi 1")
        self.entry_combi_nombre = tk.Entry(self.frame, textvariable=self.combi_nombre, font=("Arial", 12), width=22, bg="#99AAB5", fg="black")
        self.entry_combi_nombre.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Sección de imagen
        self.label_imagen = tk.Label(self.frame, text="[Imagen Combi Aquí]", width=20, height=5, bg="#4F545C", fg="white")
        self.label_imagen.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Formularios de información
        self.entries = {}
        info_labels = ["Rutas", "Horarios", "Placas", "Modelo", "Marca"]
        
        for i, label in enumerate(info_labels):
            lbl = tk.Label(self.frame, text=label, width=20, fg="white", bg="#2C2F33")
            lbl.grid(row=3+i, column=0, pady=2)
            entry = tk.Entry(self.frame, width=22, bg="#99AAB5", fg="black")
            entry.grid(row=3+i, column=1, pady=2)
            self.entries[label] = entry
        
        # Botón para agregar combi
        self.btn_agregar_combi = tk.Button(self.frame, text="Agregar combi", width=22, bg="#43B581", fg="white", font=("Arial", 10, "bold"),
                                           command=self.guardar_combi)
        self.btn_agregar_combi.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Sección de asientos
        
        self.asientos_count = tk.IntVar(value=0)

        self.label_asientos_texto = tk.Label(self.frame, text="Asientos", font=("Arial", 12), fg="white", bg="#2C2F33")
        self.label_asientos_numero = tk.Label(self.frame, textvariable=self.asientos_count, font=("Arial", 12), fg="white", bg="#2C2F33")

        self.label_asientos_texto.grid(row=1, column=2, sticky="w")
        self.label_asientos_numero.grid(row=1, column=2, sticky="e")


        self.btn_agregar_asiento = tk.Button(self.frame, text="Agregar asientos", command=self.agregar_asientos, width=22,
                                             bg="#7289DA", fg="white", font=("Arial", 10, "bold"))
        self.btn_agregar_asiento.grid(row=2, column=2, pady=10)
        
        self.canvas = Canvas(self.frame, width=300, height=300, bg="#23272A", highlightthickness=0)
        self.canvas.grid(row=3, column=2, rowspan=6, padx=20, pady=10)
        
        self.asientos = []
    
    def agregar_asientos(self):
        num_asientos = simpledialog.askinteger("Agregar asientos", "¿Cuántos asientos desea agregar?", minvalue=1, maxvalue=20)
        if num_asientos:
            self.asientos.clear()
            self.canvas.delete("all")
            for i in range(num_asientos):
                x = 50 + (i % 4) * 50
                y = 50 + (i // 4) * 50
                asiento = self.canvas.create_rectangle(x, y, x+30, y+30, fill="#7289DA", outline="white")
                self.canvas.create_text(x+15, y+15, text=str(i+1), fill="white")
                self.asientos.append(asiento)
            self.asientos_count.set(num_asientos)
            messagebox.showinfo("Éxito", f"Se agregaron {num_asientos} asientos correctamente.")

    def guardar_combi(self):
        datos = {k: v.get() for k, v in self.entries.items()}
        nombre_combi = self.combi_nombre.get()
        num_asientos = self.asientos_count.get()

        with open("combi_info.txt", "w") as file:
            file.write(f"Nombre: {nombre_combi}\n")
            file.write(f"Asientos: {num_asientos}\n")
            for key, value in datos.items():
                file.write(f"{key}: {value}\n")
        
        messagebox.showinfo("Guardado", "La información de la combi se ha guardado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombiApp(root)
    root.mainloop()
