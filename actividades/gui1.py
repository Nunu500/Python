# es recomendable importar asi
from tkinter import *
import os
def abrirCalculadora():
    os.system("Calc")
def abrirBlockNotas():
    os.system("notePad")
def cerrarVentana():
    ventana.destroy()
ventana = Tk()
ventana.title("Menu principal")
ventana.config(bg="brown")
ventana.geometry("520x480")
ventana.resizable(0,0)
botonCalc = Button(text = "calculadora", command=abrirCalculadora)
botonCalc.place(x=170,y=20)
botonNotas = Button(text = "Block de notas", command=abrirBlockNotas)
botonNotas.place(x=173,y=100)
botonCerrar = Button(text = "Autodestruccion", command=cerrarVentana)
botonCerrar.place(x=173,y=160)
ventana.mainloop()  