import tkinter as tk
from tkinter import ttk

def buscar():
    # Aquí se cargarían los datos de combis disponibles según la ruta seleccionada
    ruta_seleccionada = combo_rutas.get()
    # Datos de ejemplo (esto debería venir de una base de datos o archivo)
    datos = {
        "Campeche - Hopelchén": [("C9", "15:00 H"), ("D11", "15:45 H")],
        "Campeche - Calkiní": [("D12", "16:30 H"), ("D13", "17:00 H")],
        "Campeche - Champotón": [("C5", "14:00 H"), ("C6", "18:00 H")]
    }
    
    # Limpiar la tabla antes de insertar nuevos datos
    for row in tabla.get_children():
        tabla.delete(row)
    
    # Insertar datos filtrados si la ruta existe en el diccionario
    if ruta_seleccionada in datos:
        for combi, hora in datos[ruta_seleccionada]:
            tabla.insert("", "end", values=(combi, hora))

# Crear ventana principal
root = tk.Tk()
root.title("Catálogo de Combis")
root.geometry("600x400")

# Botón atrás en la parte superior izquierda
btn_atras = tk.Button(root, text="Atrás", command=root.destroy)
btn_atras.pack(pady=10, padx=10, anchor="nw")

# Título
titulo = tk.Label(root, text="CATÁLOGO", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Marco de selección de ruta
frame_busqueda = tk.Frame(root)
frame_busqueda.pack(pady=10)

label_ruta = tk.Label(frame_busqueda, text="SELECCIONE RUTA:")
label_ruta.grid(row=0, column=0, padx=5)

# Menú desplegable con rutas disponibles
rutas = ["Campeche - Hopelchén", "Campeche - Calkiní", "Campeche - Champotón"]
combo_rutas = ttk.Combobox(frame_busqueda, values=rutas, state="readonly")
combo_rutas.grid(row=0, column=1, padx=5)
combo_rutas.current(0)  # Seleccionar la primera opción por defecto

btn_buscar = tk.Button(frame_busqueda, text="Consultar", command=buscar)
btn_buscar.grid(row=0, column=2, padx=5)

# Tabla de combis disponibles
frame_tabla = tk.Frame(root)
frame_tabla.pack(pady=10)

columns = ("Combi", "Hora de salida")
tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")

# Definir encabezados de la tabla
tabla.heading("Combi", text="Combi")
tabla.heading("Hora de salida", text="Hora de Salida")

# Ajustar tamaño de columnas
tabla.column("Combi", width=100, anchor="center")
tabla.column("Hora de salida", width=150, anchor="center")

tabla.pack()

root.mainloop()
