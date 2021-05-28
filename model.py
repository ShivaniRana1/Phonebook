from os import EX_TEMPFAIL, name
from tkinter import *
from typing import Sized
from PIL import Image,ImageTk
import tkinter.font as font

root = Tk()
root.title("PHONEBOOK")


frame = LabelFrame(root,padx=200,pady=200)
frame.pack(padx=5,pady=5)

my_label = Label(frame,text="WELCOME TO PHONEBOOK")
my_image = ImageTk.PhotoImage(Image.open("phonebook.png"))
im = Label(frame,image=my_image)

def button_clear():
    root.quit()

def show():
    global msg
    global user

    name.grid_forget()
    address.grid_forget()
    email.grid_forget()
    phoneNo.grid_forget()
    b.grid_forget()
    
    msg = Label(frame,text="Account of {} is Created".format(name.get()))
    msg.grid(row=0,column=0)
    user = name.get()
    user=Label(frame,text=user)
    user.grid(row=1,column=0)




    button_quit = Button(frame,text="Clear",command = button_clear)
    button_quit.grid(row=2,column=1,columnspan=2)


    
    


def create():
    my_label.grid_forget()
    user_button.grid_forget()
    im.grid_forget()

    global name
    global address
    global email
    global phoneNo
    global b

    name = Entry(frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    name.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
    name.insert(0,"Enter you name")
    
    address = Entry(frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    address.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
    address.insert(0,"Enter you address")

    email = Entry(frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    email.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
    email.insert(0,"Enter you email adress")

    phoneNo = Entry(frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    phoneNo.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
    phoneNo.insert(0,"Enter you Phone Number")

    l = Label(frame,text=" ")
    l.grid(row=6,column=0)
    

    myFont = font.Font(family='Arial', size=20, weight='bold')
    b = Button(frame,text="Create New contact",fg="red",command=show)
    b['font'] = myFont
    b.grid(row=7,column=0,columnspan=3)

im.grid(row=0,column=0,columnspan=3)
my_label.grid(row=0,column=6)

#creating button
user_button = Button(frame,text="New contact",fg="Black",command=create)
user_button.grid(row=1,column=6)




root.mainloop()