from tkinter import *
import tkinter as tk
from math import *



#CREACION DE LA VENTANA
ventana = Tk()
ventana.title('CALCULADORA CIENTIFICA')
ventana.geometry('380x595')
ventana.resizable(0,0)


#DIMENSION TECLAS
ancho = 10
alto = 2

#VARIABLE PARA MOSTRAR RESULTADO EN PANTALLA
resultado=tk.StringVar()


operacion = ''

#ALMACENAMIENTO DE CLICKS
def click(tecla):
    global operacion
    operacion = operacion + tecla
    resultado.set(operacion)

#LIMPIEZA DEL CALCULO
def limpieza():
    global operacion
    resultado.set('0') 
    operacion = ''   


#BORRAR
def borrar(): #123456789 [1,2,3,4,5,6,7,8] -> 1234
    global operacion
    lista = []
    #LISTA CON VALORES DE LAS OPERACIONES
    for i in range(len(operacion)):
        lista.append(operacion[i])
    #BORRAR ULTIMO CARACTER
    lista =  lista [:-1] 
    operacion =  ''.join(lista)
    #MOSTRAR LA CADENA
    resultado.set(operacion)

#IGUAL
def operativa():
    global operacion
    try:
        total = str(eval(operacion))
    except Exception:
        limpieza()
        total = 'ERROR' 
    resultado.set(total)
    operacion = total

def suma():
    return '+'

def resta():
    return '-'

def multiplicacion():
    return '*'

def division():
    return '/'

def resto():
    return '%'

def seno():
    return 'sin('

def coseno():
    return 'cos('

def tangente():
    return 'tan('

def ln():
    return 'log('

def raiz():
    return 'sqrt('

def exponente():
    return '**'

def opfactorial():
    return 'factorial('

def lg():
    return 'log10('

#PANTALLA DE LOS CALCULOS
pantallacal = Entry(ventana,font = ('arial',15,'bold'), width= 30,bd= 15, bg = 'light grey', justify = 'right', state = tk.DISABLED,textvariable= resultado)
pantallacal.place(x = 10, y= 30)

#FILA 1
botonsin = Button(ventana, text='sin', width=ancho, height=alto,bg='white', command=lambda:click(seno())).place(x=17,y=120)
botoncos =Button(ventana, text='cos', width=ancho, height=alto,bg='white', command=lambda:click(coseno())).place(x=107,y=120)
botontan = Button(ventana, text='tan', width=ancho, height=alto,bg='white', command=lambda:click(tangente())).place(x=197,y=120)
botonln = Button(ventana, text='ln', width=ancho, height=alto,bg='white', command=lambda:click(ln())).place(x=287,y=120)

#FILA 2 
boton_raiz = Button(ventana,text='√', width=ancho, height=alto,bg='white', command=lambda:click(raiz())).place(x=17,y=180)
boton_potencia = Button(ventana,text='EXP', width=ancho, height=alto,bg='white', command=lambda:click(exponente())).place(x=107,y=180)
boton_factorial = Button(ventana,text='!', width=ancho, height=alto,bg='white', command=lambda:click(opfactorial())).place(x=197,y=180)
botonlog = Button(ventana, text='log', width=ancho, height=alto,bg='white', command=lambda:click(lg())).place(x=287,y=180)

#FILA 3
boton1 = Button(ventana, text='1', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('1')).place(x=17, y=240)
boton2 = Button(ventana,text='2', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('2')).place(x=107, y=240),
boton3 = Button(ventana,text='3', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('3')).place(x=197, y=240)
boton_suma = Button(ventana,text='+', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(suma())).place(x=287, y=240)

#FILA 4
boton4 = Button(ventana,text='4', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('4')).place(x=17, y=300)
boton5 = Button(ventana,text='5', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('5')).place(x=107, y=300)
boton6 = Button(ventana,text='6', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('6')).place(x=197, y=300)
boton_resta = Button(ventana,text='-', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(resta())).place(x=287, y=300)

#FILA 5
boton7 = Button(ventana,text='7', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('7')).place(x=17, y=360)
boton8 = Button(ventana,text='8', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('8')).place(x=107, y=360)
boton9 = Button(ventana,text='9', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('9')).place(x=197, y=360)
boton_por = Button(ventana,text='x', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(multiplicacion())).place(x=287, y=360)

#FILA 6
boton_par_izq = Button(ventana,text='(', width=ancho, height=alto, bg='#a499aa', command=lambda:click('(')).place(x=17, y=420)
boton0 = Button(ventana,text='0', width=ancho, height=alto, bg='#EED0C6', command=lambda:click('0')).place(x=107, y=420)
boton_par_der = Button(ventana,text=')', width=ancho, height=alto, bg='#a499aa', command=lambda:click(')')).place(x=197, y=420)
boton_division = Button(ventana,text='/', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(division())).place(x=287, y=420)

#FILA 7
boton_borrar = Button(ventana,text='<-', width=ancho, height=alto, bg='#D2BEBF', command=borrar).place(x=17, y=480)
boton_coma = Button(ventana,text='.', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click('.')).place(x=107, y=480)
boton_pi = Button(ventana,text='π', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(str(pi))).place(x=197, y=480)
boton_reciduo = tk.Button(ventana,text='%', width=ancho, height=alto, bg='#D2BEBF', command=lambda:click(resto())).place(x=287, y=480)

#FILA 8
boton_igual = Button(ventana,text='=', width=ancho, height=alto, bg='yellow', command=operativa).place(x=287, y=540)
boton_limpiar = Button(ventana,text='C', width=ancho, height=alto, bg='#ce8c69', command=limpieza).place(x=197, y=540)


ventana.mainloop()
