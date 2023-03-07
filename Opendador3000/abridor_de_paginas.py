import time
import webbrowser
from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk

ventana=Tk()

#Agregamos varibales para las imagenes
#photFacebook = PhotoImage(file='Facebook-logo.png')
#photWhatsapp = PhotoImage(file=)
#photYoutube = PhotoImage(file=)
#photMeet = PhotoImage(file=)



#Damos tamaño a la ventana y propiedades
ventana.title("Opendador3000")
ventana.geometry("300x130")
#ventana.resizable(False, False)
ventana.iconbitmap('C:\\Users\\gr321\\Documents\\VisualStudioCode\\imagenes opendador\\opendador.ico')

#Variables de los checkbox
valCheckFacebook = tk.IntVar(value=1)
valCheckWhatsapp = tk.IntVar(value=1)
valCheckYoutube = tk.IntVar(value=1)
valCheckMeet = tk.IntVar(value=1)


#Añadimos los checkBox en la ventana
chkF = tk.Checkbutton(ventana,text='Facebook',variable=valCheckFacebook).grid(row=1, sticky=W)
chkW = tk.Checkbutton(ventana,text='Whatsapp',variable=valCheckWhatsapp).grid(row=2, sticky=W)
chkY = tk.Checkbutton(ventana,text='Youtube',variable=valCheckYoutube).grid(row=3, sticky=W)
chkM = tk.Checkbutton(ventana,text='Meet',variable=valCheckMeet).grid(row=4, sticky=W)



#Metodo para checar si los checkbox estan marcados se abra la pagina corespondiente
def Abridor():
    if(valCheckFacebook.get()==1):
        webbrowser.open("https://www.facebook.com", new=2, autoraise=True)
        time.sleep(1)
    if(valCheckWhatsapp.get()==1):
        webbrowser.open("https://web.whatsapp.com", new=2, autoraise=True)
        time.sleep(1)
    if(valCheckYoutube.get()==1):
        webbrowser.open("https://www.youtube.com", new=2, autoraise=True)
        time.sleep(1)
    if(valCheckMeet.get()==1):
        webbrowser.open("https://meet.google.com/landing?authuser=2", new=2, autoraise=True)
        time.sleep(1)
    if(valCheckFacebook.get()==0 and valCheckWhatsapp.get()==0 and valCheckYoutube.get()==0 and valCheckMeet.get()==0):
        MessageBox.showinfo('ALERTA','No seas wey selecciona algo')       
        time.sleep(1)

#Añadimos el boton a la ventana
btnEjecutador = tk.Button(ventana,text='Abrir',command=Abridor).place(relx=0.5, rely=0.9, anchor=CENTER)

#webbrowser.open("https://www.facebook.com", new=2, autoraise=True)
#webbrowser.open("https://web.whatsapp.com", new=2, autoraise=True)
#webbrowser.open("https://www.youtube.com", new=2, autoraise=True)
#webbrowser.open("https://meet.google.com/landing?authuser=2", new=2, autoraise=True)

ventana.mainloop()