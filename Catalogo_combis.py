import tkinter as tk
from tkinter import ttk

def centrar_ventana(ventana, ancho=600, alto=400):  # Ajusta el tamaño si es necesario
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"+{x}+{y}")

def abrir_catalogo():
    ventana = tk.Toplevel()
    ventana.title("Catálogo de Combis")
    ventana.geometry("600x400")  # Mantén las dimensiones fijas

    centrar_ventana(ventana)  # Centrar la ventana

    btn_atras = tk.Button(ventana, text="Atrás", command=ventana.destroy)
    btn_atras.pack(pady=10, padx=10, anchor="nw")

    titulo = tk.Label(ventana, text="CATÁLOGO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    frame_busqueda = tk.Frame(ventana)
    frame_busqueda.pack(pady=10)

    label_ruta = tk.Label(frame_busqueda, text="SELECCIONE RUTA:")
    label_ruta.grid(row=0, column=0, padx=5)

    rutas = ["Campeche - Hopelchén", "Campeche - Calkiní", "Campeche - Champotón"]
    combo_rutas = ttk.Combobox(frame_busqueda, values=rutas, state="readonly")
    combo_rutas.grid(row=0, column=1, padx=5)
    combo_rutas.current(0)

    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10)

    columns = ("Combi", "Hora de salida")
    tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")

    tabla.heading("Combi", text="Combi")
    tabla.heading("Hora de salida", text="Hora de Salida")

    tabla.column("Combi", width=100, anchor="center")
    tabla.column("Hora de salida", width=150, anchor="center")

    tabla.pack()

    def buscar():
        ruta_seleccionada = combo_rutas.get()
        datos = {
            "Campeche - Hopelchén": [("C9", "15:00 H"), ("D11", "15:45 H")],
            "Campeche - Calkiní": [("D12", "16:30 H"), ("D13", "17:00 H")],
            "Campeche - Champotón": [("C5", "14:00 H"), ("C6", "18:00 H")]
        }

        for row in tabla.get_children():
            tabla.delete(row)

        if ruta_seleccionada in datos:
            for combi, hora in datos[ruta_seleccionada]:
                tabla.insert("", "end", values=(combi, hora))

    btn_buscar = tk.Button(frame_busqueda, text="Consultar", command=buscar)
    btn_buscar.grid(row=0, column=2, padx=5)

# Si este archivo se ejecuta directamente, abrir la ventana
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Catálogo de Combis")
    root.geometry("400x300")

    btn_abrir_catalogo = tk.Button(root, text="Abrir Catálogo", command=abrir_catalogo)
    btn_abrir_catalogo.pack(pady=20)

    root.mainloop()

