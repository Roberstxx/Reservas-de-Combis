import tkinter as tk
from tkinter import ttk

def centrar_ventana(ventana, ancho=800, alto=450):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

class ReservaAsientosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservar Asiento")
        self.root.geometry("800x450")
        self.root.configure(bg="#2C2F33")  # Fondo de la ventana

        # Botón atrás
        self.btn_atras = tk.Button(self.root, text="← Atrás", font=("Arial", 10, "bold"), bg="#7289DA", fg="white", command=self.root.destroy)
        self.btn_atras.place(x=10, y=10, width=60, height=30)

        # Campo de nombre de usuario
        self.entry_usuario = tk.Entry(self.root, font=("Arial", 12), bg="#99AAB5", fg="black")
        self.entry_usuario.place(x=300, y=10, width=200, height=30)
        self.entry_usuario.insert(0, "Agregar usuario")  # Placeholder
        self.entry_usuario.bind("<FocusIn>", self.on_entry_click)
        self.entry_usuario.bind("<FocusOut>", self.on_focusout)

        # Etiqueta y combobox para combis
        self.combi_label = tk.Label(self.root, text="Seleccionar Combi:", font=("Arial", 10), bg="#2C2F33", fg="white")
        self.combi_label.place(x=50, y=70)
        self.combi_combobox = ttk.Combobox(self.root, values=["Combi 1", "Combi 2"], state="readonly")
        self.combi_combobox.place(x=200, y=70, width=150)
        self.combi_combobox.bind("<<ComboboxSelected>>", self.generar_asientos)

        # Etiqueta y combobox para rutas
        self.ruta_label = tk.Label(self.root, text="Seleccionar Ruta:", font=("Arial", 10), bg="#2C2F33", fg="white")
        self.ruta_label.place(x=50, y=110)
        self.ruta_combobox = ttk.Combobox(self.root, values=["Ruta A", "Ruta B"], state="readonly")
        self.ruta_combobox.place(x=200, y=110, width=150)

        # Etiqueta y combobox para horarios
        self.horario_label = tk.Label(self.root, text="Seleccionar Horario:", font=("Arial", 10), bg="#2C2F33", fg="white")
        self.horario_label.place(x=50, y=150)
        self.horario_combobox = ttk.Combobox(self.root, values=["08:00 AM", "10:00 AM"], state="readonly")
        self.horario_combobox.place(x=200, y=150, width=150)

        # Etiqueta y combobox para asientos
        self.asiento_label = tk.Label(self.root, text="Seleccionar Asiento:", font=("Arial", 10), bg="#2C2F33", fg="white")
        self.asiento_label.place(x=50, y=190)
        self.asiento_combobox = ttk.Combobox(self.root, state="readonly")
        self.asiento_combobox.place(x=200, y=190, width=150)

        # Botón de registrar
        self.btn_registrar = tk.Button(self.root, text="Registrar", font=("Arial", 12, "bold"), bg="#43B581", fg="white")
        self.btn_registrar.place(x=120, y=250, width=150, height=40)

        # Cuadro de asientos (Canvas)
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="#2C2F33", highlightthickness=1, highlightbackground="white")
        self.canvas.place(x=450, y=50)

        # Leyenda
        self.leyenda_frame = tk.Frame(self.root, bg="#2C2F33")
        self.leyenda_frame.place(x=450, y=370)
        colores = {"Disponible": "white", "Seleccionado": "orange", "Ocupado": "gray", "Deshabilitado": "darkgray"}
        for i, (estado, color) in enumerate(colores.items()):
            tk.Canvas(self.leyenda_frame, width=20, height=20, bg=color, highlightthickness=1).grid(row=i, column=0, padx=5, pady=2)
            tk.Label(self.leyenda_frame, text=estado, bg="#2C2F33", fg="white").grid(row=i, column=1, padx=5, pady=2)

        centrar_ventana(self.root)

    def on_entry_click(self, event):
        if self.entry_usuario.get() == "Agregar usuario":
            self.entry_usuario.delete(0, tk.END)

    def on_focusout(self, event):
        if not self.entry_usuario.get():
            self.entry_usuario.insert(0, "Agregar usuario")

    def generar_asientos(self, event):
        self.canvas.delete("all")
        combi_seleccionada = self.combi_combobox.get()
        asientos_por_combi = {"Combi 1": 12, "Combi 2": 15}
        ocupados = {"Combi 1": [5, 9], "Combi 2": [3, 7, 10]}
        num_asientos = asientos_por_combi.get(combi_seleccionada, 0)
        self.asiento_combobox["values"] = [str(i + 1) for i in range(num_asientos) if (i + 1) not in ocupados.get(combi_seleccionada, [])]

        for i in range(num_asientos):
            x, y = (i % 4) * 50 + 10, (i // 4) * 50 + 10
            color = "gray" if (i + 1) in ocupados.get(combi_seleccionada, []) else "white"
            self.canvas.create_rectangle(x, y, x + 40, y + 40, fill=color, outline="black")
            self.canvas.create_text(x + 20, y + 20, text=str(i + 1), font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservaAsientosApp(root)
    root.mainloop()
