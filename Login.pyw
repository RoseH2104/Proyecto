from tkinter import *

#ventana
root = Tk()
root.title("Login")
root.geometry("900x500+500+225")
root.resizable(False, False)

#Fondo
fondo1 = PhotoImage(file="Proyecto/img/fondo1.png")
label = Label(root, image=fondo1)
label.place(x=0, y=0, width=400, relheight=1)
fondo2 = Label(root, bg="white")
fondo2.place(x=400,y=0, width=500, relheight=1)

bnv = Label(root, text="Bienvenido", font=("Arial",16), bg="white")
bnv.place(x=500,y=25, width=300, height=80)

#Usuario
txt1 = Label(root, text="Usuario", bg="white")
txt1.place(x=550,y=100, width=200, height=30)
entrada1 = Entry(root, bg="white")
entrada1.place(x=550,y=125, width=200, height=30)

#Contraseña
txt2 = Label(root, text="Contraseña", bg="white")
txt2.place(x=550,y=175, width=200, height=30)
entrada2 = Entry(root, bg="white")
entrada2.place(x=550,y=200, width=200, height=30)

#Botones
btn2 = Button(root, text="Registrar", font=("Arial",8) )
btn2.place(x=560,y=300, width=80, height=25)
btn2 = Button(root, text="Iniciar Sesion", font=("Arial",8) )
btn2.place(x=660,y=300, width=80, height=25)


root.mainloop()
