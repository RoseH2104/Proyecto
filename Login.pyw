import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql

#Login
login = Tk()
login.title("Login")
login.geometry("900x500+500+225")
login.resizable(False, False)


def validar_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="usuario"
    )

    mcursor = bd.cursor()

    sql = "SELECT FROM login (usuario, contraseña) VALUES('{0}', '{1}')".format(entrada1.get(), entrada2.get()) 
    if mcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesion correcto", message="Usuario y contraseña correcta")
    else:
        messagebox.showinfo(title="Inicio de Sesion incorrecto", message="Usuario y contraseña incorrecta")
    bd.close()


#Fondo
fondo1 = PhotoImage(file="Prueba/img/fondo1.png")
label = Label(login, image=fondo1)
label.place(x=0, y=0, width=400, relheight=1)
fondo2 = Label(login, bg="white")
fondo2.place(x=400,y=0, width=500, relheight=1)

bnv = Label(login, text="Bienvenido", font=("Arial",16), bg="white")
bnv.place(x=500,y=25, width=300, height=80)

#Usuario
txt1 = Label(login, text="Usuario", bg="white")
txt1.place(x=550,y=100, width=200, height=30)
entrada1 = Entry(login, bg="white")
entrada1.place(x=550,y=125, width=200, height=30)

#Contraseña
txt2 = Label(login, text="Contraseña", bg="white")
txt2.place(x=550,y=175, width=200, height=30)
entrada2 = Entry(login, bg="white")
entrada2.place(x=550,y=200, width=200, height=30)

#Botones
btn1 = Button(login, text="Registrar", cursor="hand2", relief="flat", font=("Arial",8))
btn1.place(x=560,y=300, width=80, height=25)
btn2 = Button(login, text="Iniciar Sesion", cursor="hand2", relief="flat", font=("Arial",8), command=validar_datos)
btn2.place(x=660,y=300, width=80, height=25)


#Menu
def menu1():
    login.withdraw()
    menu = tk.Toplevel()
    menu.title("Menu Principal")
    menu.geometry("900x500+300+200")

    def cerrar():
        menu.withdraw()
        login.deiconify()

    btn3 = tk.Button(menu, text="Cerrar Sesion", cursor="hand2", relief="flat", font=("Arial",8), command=cerrar)
    btn3.place(x=800,y=30, width=80, height=25)

    menu.mainloop()

login.mainloop()
