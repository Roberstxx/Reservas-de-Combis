import tkinter as tk
from tkinter import simpledialog, messagebox, Canvas

class CombiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agrega tu combi")
        
        # Marco principal
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack()
        
        # Botón de regreso
        self.btn_atras = tk.Button(self.frame, text="Atrás", width=20)
        self.btn_atras.grid(row=0, column=0, sticky='w')
        
        # Título
        self.label_titulo = tk.Label(self.frame, text="Agrega tu combi", font=("Arial", 16, "bold"))
        self.label_titulo.grid(row=0, column=1, columnspan=2)
        
        # Label de combi
        self.label_combi = tk.Label(self.frame, text="Combi 1", font=("Arial", 12))
        self.label_combi.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Sección de imagen
        self.label_imagen = tk.Label(self.frame, text="[Imagen Combi Aquí]", width=20, height=5, bg="gray")
        self.label_imagen.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Formularios de información
        self.entries = {}
        info_labels = ["Rutas", "Horarios", "Placas", "Modelo", "Marca"]
        
        for i, label in enumerate(info_labels):
            lbl = tk.Label(self.frame, text=label, width=20)
            lbl.grid(row=3+i, column=0, pady=2)
            entry = tk.Entry(self.frame, width=22)
            entry.grid(row=3+i, column=1, pady=2)
            self.entries[label] = entry
        
        # Botón para agregar combi
        self.btn_agregar_combi = tk.Button(self.frame, text="Agregar combi", width=22)
        self.btn_agregar_combi.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Sección de asientos
        self.label_asientos = tk.Label(self.frame, text="Asientos 12", font=("Arial", 12))
        self.label_asientos.grid(row=1, column=2, padx=20)
        
        self.btn_agregar_asiento = tk.Button(self.frame, text="Agregar asientos", command=self.agregar_asientos, width=22)
        self.btn_agregar_asiento.grid(row=2, column=2, pady=10)
        
        self.canvas = Canvas(self.frame, width=300, height=300, bg="white")
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
                asiento = self.canvas.create_oval(x, y, x+30, y+30, fill="gray")
                self.canvas.create_text(x+15, y+15, text=str(i+1), fill="white")
                self.asientos.append(asiento)
            messagebox.showinfo("Éxito", f"Se agregaron {num_asientos} asientos correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombiApp(root)
    root.mainloop()
