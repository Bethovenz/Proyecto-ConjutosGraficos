# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:38:50 2019

@author: raagu
"""

import tkinter as ttk
import tkinter as tk
import itertools

ventana = ttk.Tk()
var1 = ttk.StringVar()
var2 = ttk.StringVar()
res = ttk.StringVar()
titulo = ttk.StringVar()
titulo.set("Resultados")

ventana.title("Conjuntos")
ventana.geometry("600x300")
ventana.configure(bg="antique white")
ventana.resizable(0,0)


def conj_a():
    a = set()
    var = var1.get()
    a.update(var.split()) #Ingreso de elementos a los conjuntos separados por espacios
    return res.set(a)


def conj_b():
    b = set()
    var = var2.get()
    b.update(var.split()) #Ingreso de elementos a los conjuntos separados por espacio
    return res.set(b)


def union():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = a | b
    t = "Unión"
    if not u:
        messag = "Intenta ingresar elementos"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)
        
    
            
    
def inter():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = a & b
    t = "Intersección" 
    if not u:
        messag = "No hay Intersección"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)
    
   
def difer_a():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = a - b
    t = "Diferencia a/b"
    if not u:
        messag = "No existe tal diferencia"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)

def difer_b():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = b - a
    t = "Diferencia b/a"
    if not u:
        messag = "No existe tal diferencia"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)

def diferSim():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = a ^ b
    t = "Diferencia simétrica"
    if not u:
        messag = "No existe tal diferencia"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)

def cartes():
    a = set()
    var = var1.get()
    a.update(var.split())
    b = set()
    varr = var2.get()
    b.update(varr.split())
    u = list(itertools.product((a),(b)))
    t = "Producto cartesiano"
    if not u:
        messag = "No puedo aplicar distributiva si no ingresas elementos"
        return res.set(messag)
    else:
        return res.set(u), titulo.set(t)
        
    


def borrar():
    a = set()
    var = var1.get()
    a.update(var.split()) #Ingreso de elementos a los conjuntos separados por espacios 
    entra_a.delete(0, len(var))

        
    

#boton_conj_a = ttk.Button(ventana, text='Conj a', command=conj_a, font="Times 10 bold").place(x=50, y=250)
titul_conj = ttk.Label(ventana, text="Conjuntos", font="Times 20 bold italic", fg="black", bg="antique white").place(x=300, y=20, anchor="center")

etiq_a = ttk.Label(ventana, text="Conjunto a:", bg="antique white", font="Times 10 bold italic")
etiq_a.place(x=30, y=60)
entra_a = ttk.Entry(ventana, textvariable=var1, width="30", font="Times 10 bold")
entra_a.place(x=100, y=60)

etiq_b = ttk.Label(ventana, text="Conjunto b:", bg="antique white", font="Times 10 bold italic")
etiq_b.place(x=30, y=90)
entra_b = ttk.Entry(ventana, textvariable=var2, width="30", font="Times 10 bold").place(x=100, y=90)

titul_res = ttk.Label(ventana, textvariable=titulo, font="Times 15 bold", fg="SpringGreen4", bg="antique white").place(x=300, y=160, anchor="center")
eti_res = ttk.Label(ventana, textvariable=res, width=80, height=3, bg='white', fg='blue', font="Times 10 bold")
eti_res.place(x=300, y=200, anchor="center")

boton_uni = ttk.Button(ventana, text='Unión', command=union, font="Times 10 bold", width="6", height="2").place(x=110, y=250)
boton_inter = ttk.Button(ventana, text='Inter', command=inter, font="Times 10 bold", width="6", height="2").place(x=170, y=250)
boton_dif_a = ttk.Button(ventana, text='Dif(a)', command=difer_a, font="Times 10 bold", width="6", height="2").place(x=230, y=250)
boton_dif_b = ttk.Button(ventana, text='Dif(b)', command=difer_b, font="Times 10 bold", width="6", height="2").place(x=290, y=250)
boton_difSim = ttk.Button(ventana, text='DifSim', command=diferSim, font="Times 10 bold", width="6", height="2").place(x=350, y=250)
boton_cartes = ttk.Button(ventana, text='Cartes', command=cartes, font="Times 10 bold", width="6", height="2").place(x=410, y=250)

logoutp = ttk.PhotoImage(file="descarga11.ppm")
etiq_logo = ttk.Label(ventana, image=logoutp).place(x=425, y=40)


#boton_borra = ttk.Button(ventana, text='Borrar', command=borrar, font="Times 10 bold").place(x=100, y=200)

ventana.mainloop()