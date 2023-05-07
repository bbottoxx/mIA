from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Formulario")

marcoPrincipal= ttk.Frame(raiz, padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

datos = ttk.Frame(marcoPrincipal, padding="15 15 15 15", relief="raised")
datos.grid(column=0, row=0)

ttk.Label(datos,text="Nombre").grid(column=0, row=0)
ttk.Entry(datos).grid(column=1, row=0)
ttk.Label(datos,text="Paterno").grid(column=0, row=1)
ttk.Entry(datos).grid(column=1, row=1)
ttk.Label(datos,text="Materno").grid(column=0, row=2)
ttk.Entry(datos).grid(column=1, row=2)
ttk.Label(datos,text="Correo").grid(column=0, row=3)
ttk.Entry(datos).grid(column=1, row=3)
ttk.Label(datos,text="Celular").grid(column=0, row=4)
ttk.Entry(datos).grid(column=1, row=4)


for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

# Bloque de aficiones
aficiones = ttk.Frame(marcoPrincipal,padding="10 10 10 10", relief="raised")
aficiones.grid(column=0, row=1)

ttk.Label(aficiones, text="Aficiones").grid(column=0, row=0)

leer = StringVar()
chk1 = ttk.Checkbutton(aficiones, text="Lectura",  variable=leer, onvalue="si", offvalue="no")
chk1.grid(column=0, row=1)
musica = StringVar()
chk2 = ttk.Checkbutton(aficiones, text="Musica",  variable=musica, onvalue="si", offvalue="no")
chk1.grid(column=1, row=1)
video = StringVar()
chk3 = ttk.Checkbutton(aficiones, text="Video Juegos",  variable=video, onvalue="si", offvalue="no")
chk1.grid(column=2, row=1)

for hijo in aficiones.winfo_children():
    hijo.grid_configure(padx=10)

# Bloque de botones

botones = ttk.Frame(marcoPrincipal)
botones.grid(column=0, row=2)

btnSave = ttk.Button(botones, text="Guardar")
btnSave.grid(column=0,row=0)
btnCancelar = ttk.Button(botones, text="Cancelar")
btnCancelar.grid(column=1,row=0)

for hijo in botones.winfo_children():
    hijo.grid_configure(padx=20)

# Bloque tipo 
estatus = ttk.Frame(marcoPrincipal)
estatus.grid(column=1, row=0)

estudio=StringVar()
estudiante = ttk.Radiobutton(estatus, text="Estudiante", variable=estudio, value="Estudiante")
estudiante.grid(row=0, sticky="w")
empleo =StringVar()
empleado   = ttk.Radiobutton(estatus, text="Empleado", variable=empleo, value="Empleado")
empleado.grid(row=1, sticky="w")
desempleo =StringVar()
desempleado   = ttk.Radiobutton(estatus, text="Desempleado", variable=desempleo, value="Desempleado")
desempleado.grid(row=2, sticky="w")

comboBox = ttk.Frame(marcoPrincipal)
comboBox.grid(column=1, row=1)
estados=StringVar()
estados = ttk.Combobox(comboBox,textvariable=estados)
estados.grid()
estados['values']=("Jalisco", "Nayarit", "Colima", "Michoacan")

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

raiz.mainloop()
