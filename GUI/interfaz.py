from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Inicio de sesion")

marcoPrincipal = ttk.Frame(raiz,padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

usuario= StringVar()
contrasenia = StringVar()

ttk.Label(marcoPrincipal,text="Usuario").grid(column=1, row=0)
ttk.Label(marcoPrincipal,text="Contrasenia ").grid(column=1, row=1)

txtUsuario=ttk.Entry(marcoPrincipal, width=7, textvariable=usuario)
txtUsuario.grid(column=2, row=0)

txtContrasenia=ttk.Entry(marcoPrincipal, width=7, textvariable=contrasenia)
txtContrasenia.grid(column=2, row=1)



raiz.mainloop()