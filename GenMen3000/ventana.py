from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pyautogui as pt
import time
global i
root=Tk()
root.config(width=255,height=200)
root.resizable(False, False)
root.title("GenMen3000")
root.iconbitmap('C:\\Users\\gr321\\Downloads\\icono.ico')


Label(root,text="Número de Mensajes").place(relx=0.5, rely=0.1, anchor=CENTER)
entry=Entry(root, width=40)
entry=Entry(justify=CENTER)
entry.place(x=70, y=30)

Label(root,text="Mensaje").place(relx=0.5, rely=0.4, anchor=CENTER)
entry2 = Entry(root, width=40)
entry2=Entry(justify=CENTER)
entry2.place(x=70, y=90)


def generater():
   global entry,entry2
   limit = int(entry.get())
   message = str(entry2.get())

   print(limit)
   print(message)
   i=0
   time.sleep(3)
   while i < int(limit):
      pt.typewrite(message)
      pt.press("enter")
      i += 1
   
   print("ya acabe")


Button(root, text="Generar mensajes", command=generater).place(relx=0.5, rely=0.7, anchor=CENTER)

  
root.mainloop()