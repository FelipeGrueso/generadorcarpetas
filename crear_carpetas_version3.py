import os
import tkinter as tk

#identifico la carpeta actual
ruta = os.getcwd()


def generar_secuencia():
    try:
        inicio = int(entry_inicio.get())
        fin = int(entry_fin.get())
        resultado_label.config(text=f"Secuencia generada: 0{inicio} - 0{fin}")
    
##        ruta_label.config(text=f"ruta donde se generaron las carpetas {ruta}")

        for i in  range(inicio, fin + 1):

            os.mkdir(f"{ruta}\\0{i}")

        boton.config(text="Cerrar ventana", bg="blue", fg="white", command=ventana.destroy)


    except ValueError:
        resultado_label.config(text="Error: Ingresa valores válidos")

    except FileExistsError:
        resultado_label.config(text="Error: Al menos una carpeta ya existe")


    else:
        if inicio > fin:
            resultado_label.config(text="Error: El número de inicio debe ser menor")




# Crear la ventana principal
ventana = tk.Tk()
#ventana.title("Creador de caprpetas")

# Crear etiquetas y casillas de entrada
label_inicio = tk.Label(ventana, text="Carpeta inicial:")
label_inicio.pack()
entry_inicio = tk.Entry(ventana)
entry_inicio.pack()

label_fin = tk.Label(ventana, text="Carpeta final:")
label_fin.pack()
entry_fin = tk.Entry(ventana)
entry_fin.pack()

# Botón para generar la secuencia
boton = tk.Button(ventana, text="Generar Secuencia", command=generar_secuencia)
boton.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

#Etiqueta para mostrar la ruta
##ruta_label = tk.Label(ventana, text="")
##ruta_label.pack()



ventana.geometry("185x134")  # Establecer tamaño a 500x300 píxeles (ancho x alto)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

