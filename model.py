from tkinter import *
import datetime
from tkinter.font import Font
from PIL import Image,ImageTk
import header as m

root = Tk()
root.title("shivani phonebook")
root.iconbitmap('Photos/color.png')
root.geometry("400x400")

my_img = ImageTk.PhotoImage(Image.open("Photos/phonebook.png"))
my_label = Label(image=my_img,pady=10)
my_label.pack()

label=Label(root,text='Today is {}/{}/{}'.format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day),fg="blue").pack()
label=Label(root,text=" Welcome to Shivani's phonebook",font=("Arial", 25),fg="hotpink").pack()
     
def home():
    
    hide_all_frames()

def show():
    m.show_all()
        
def create(name,address,email,contact):
    if name =='' or name=='Enter you name':
        l = Label(file_new_frame,text="You have to fill all entry").grid(row=4,column=0)
    elif address=='' or address=="Enter you address":
        l = Label(file_new_frame,text="You have to fill all entry").grid(row=4,column=0)
    elif  email=='' or email=="Enter your email adress":
        l = Label(file_new_frame,text="You have to fill all entry").grid(row=4,column=0)
    elif contact =='' or contact =="Enter your Phone Number":
        l = Label(file_new_frame,text="You have to fill all entry").grid(row=4,column=0)
    else:       
        hide_all_frames()
        global msg
        file_create_frame.pack(fill="both",expand=1)
        msg = Label(file_create_frame,text="Your contact has been created",font=("Arial", 25),fg="hotpink",pady=5).pack()
        msg = Label(file_create_frame,text="Name: {}".format(name)).pack()
        msg = Label(file_create_frame,text="Address: {}".format(address)).pack()
        msg = Label(file_create_frame,text="Email: {}".format(email)).pack()
        msg = Label(file_create_frame,text="Phone Number: {}".format(contact)).pack()
        button_save = Button(file_create_frame,text="Save to Database",command=lambda:m.add_one(name,address,email,contact)).pack()
        

def click(event):
    name.config(state=NORMAL)
    name.delete(0,END) 
    
def click1(event):
    address.config(state=NORMAL)
    address.delete(0,END)

def click2(event):
    email.config(state=NORMAL)
    email.delete(0,END)

def click3(event):
    phoneNo.config(state=NORMAL)
    phoneNo.delete(0,END)
    label = Label(file_new_frame,text="Please check again!!!\n Are you sure you want to create",fg="RED").grid(row=6,column=0,columnspan=3,padx=5,pady=5)


def get_detail():
    hide_all_frames()
    global name
    global address
    global email
    global phoneNo
    
    file_new_frame.pack(fill="both",expand=1)
    name = Entry(file_new_frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    name.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
    name.insert(0,"Enter your name")
    name.config(state=DISABLED)
    name.bind("<Button-1>",click)
        
    address = Entry(file_new_frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    address.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
    address.insert(0,"Enter your address")
    address.config(state=DISABLED)
    address.bind("<Button-1>",click1)

    email = Entry(file_new_frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    email.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
    email.insert(0,"Enter your email adress")
    email.config(state=DISABLED)
    email.bind("<Button-1>",click2)

    phoneNo = Entry(file_new_frame,width = 35,borderwidth=5,bg="pink",fg="blue")
    phoneNo.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
    phoneNo.insert(0,"Enter your Phone Number")
    phoneNo.config(state=DISABLED)
    phoneNo.bind("<Button-1>",click3)

    #showing details
    button_create = Button(file_new_frame,text="CREATE",padx=5,pady=5,fg="black",command=lambda:create(name.get(),address.get(),email.get(),phoneNo.get())).grid(row=5,column=0)

def much(entry):
    #hide_all_frames()
    #file_delete_frame.pack(fill="both",expand=1)
    m.delete_one(entry)
    

def delete_contact():
    hide_all_frames()
    global entry
    file_delete_frame.pack(fill="both",expand=1)
    entry = Entry(file_delete_frame,width=35,borderwidth=5,bg="pink",fg="blue")
    entry.grid(row=6,column=0,columnspan=3,padx=5,pady=5)
    entry.insert(0,"Enter Id")
    
    b = Button(file_delete_frame,text="REMOVE TEXT",command=lambda:entry.delete(0,END)).grid(row=7,column=1)
    b = Button(file_delete_frame,text="CONFIRM",command=lambda:much(entry.get())).grid(row=7,column=0)
    

def hide_all_frames():
    file_new_frame.pack_forget()
    file_create_frame.pack_forget()
    file_delete_frame.pack_forget()
    
    
      
file_new_frame = Frame(root,width=400,height=400) 
file_create_frame = Frame(root,width=400,height=400)
file_delete_frame = Frame(root,width=400,height=400)
    
  
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="FILE",menu=file_menu,command=get_detail)
file_menu.add_command(label="HOME",command=home)
file_menu.add_command(label="NEW",command=get_detail)
file_menu.add_command(label="ALL CONTACT",command=show)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="EDIT",menu=file_menu,command=root.destroy)
file_menu.add_command(label="EXIT",command=root.destroy)
file_menu.add_command(label="REMOVE CONTACT",command=delete_contact)

root.mainloop()
