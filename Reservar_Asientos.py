import tkinter as tk
from tkinter import ttk

def centrar_ventana(ventana, ancho=800, alto=450):  # Ajusta el tamaño si es necesario
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"+{x}+{y}")

class ReservaAsientosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservar Asiento")
        self.root.geometry("800x450")
        self.root.configure(bg="white")

        # Botón atrás
        self.btn_atras = tk.Button(self.root, text="← Atrás", font=("Arial", 10, "bold"), bg="lightgray", command=self.root.destroy)
        self.btn_atras.place(x=10, y=10, width=60, height=30)

        # Nombre de usuario
        self.entry_usuario = tk.Entry(root, font=("Arial", 12))
        self.entry_usuario.place(x=300, y=20, width=200, height=30)

        # Menús desplegables
        self.combi_label = tk.Label(root, text="Seleccionar Combi:", font=("Arial", 10), bg="white")
        self.combi_label.place(x=50, y=70)
        self.combi_combobox = ttk.Combobox(root, values=["Combi 1", "Combi 2"], state="readonly")
        self.combi_combobox.place(x=200, y=70, width=150)
        self.combi_combobox.bind("<<ComboboxSelected>>", self.generar_asientos)

        self.ruta_label = tk.Label(root, text="Seleccionar Ruta:", font=("Arial", 10), bg="white")
        self.ruta_label.place(x=50, y=110)
        self.ruta_combobox = ttk.Combobox(root, values=["Ruta A", "Ruta B"], state="readonly")
        self.ruta_combobox.place(x=200, y=110, width=150)

        self.horario_label = tk.Label(root, text="Seleccionar Horario:", font=("Arial", 10), bg="white")
        self.horario_label.place(x=50, y=150)
        self.horario_combobox = ttk.Combobox(root, values=["08:00 AM", "10:00 AM"], state="readonly")
        self.horario_combobox.place(x=200, y=150, width=150)

        self.asiento_label = tk.Label(root, text="Seleccionar Asiento:", font=("Arial", 10), bg="white")
        self.asiento_label.place(x=50, y=190)
        self.asiento_combobox = ttk.Combobox(root, state="readonly")
        self.asiento_combobox.place(x=200, y=190, width=150)

        # Botón de registrar
        self.btn_registrar = tk.Button(root, text="Registrar", font=("Arial", 12, "bold"), bg="lightgray")
        self.btn_registrar.place(x=120, y=250, width=150, height=40)

        # Cuadro interactivo de asientos
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.place(x=450, y=50)

        # Leyenda de asientos
        self.leyenda_frame = tk.Frame(root, bg="white")
        self.leyenda_frame.place(x=450, y=370)

        colores = {"Disponible": "white", "Seleccionado": "orange", "Ocupado": "gray", "Deshabilitado": "darkgray"}
        for i, (estado, color) in enumerate(colores.items()):
            tk.Canvas(self.leyenda_frame, width=20, height=20, bg=color, highlightthickness=1).grid(row=i, column=0, padx=5, pady=2)
            tk.Label(self.leyenda_frame, text=estado, bg="white").grid(row=i, column=1, padx=5, pady=2)

        centrar_ventana(self.root) #Centrar la ventana

    def generar_asientos(self, event):
        self.canvas.delete("all")  # Limpiar el área de asientos
        combi_seleccionada = self.combi_combobox.get()
        asientos_por_combi = {"Combi 1": 12, "Combi 2": 15}  # Simulación de datos
        ocupados = {"Combi 1": [5, 9], "Combi 2": [3, 7, 10]}  # Asientos ocupados

        num_asientos = asientos_por_combi.get(combi_seleccionada, 0)
        self.asiento_combobox["values"] = [str(i+1) for i in range(num_asientos) if (i+1) not in ocupados.get(combi_seleccionada, [])]

        for i in range(num_asientos):
            x, y = (i % 4) * 50 + 10, (i // 4) * 50 + 10
            color = "gray" if (i+1) in ocupados.get(combi_seleccionada, []) else "white"
            self.canvas.create_rectangle(x, y, x+40, y+40, fill=color, outline="black")
            self.canvas.create_text(x+20, y+20, text=str(i+1), font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservaAsientosApp(root)
    root.mainloop()
