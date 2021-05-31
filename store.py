from tkinter import *
import datetime
from tkinter.font import Font
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title("shivani phonebook")
root.iconbitmap('/Users/mac/Downloads/Tatice-Cristal-Intense-Apple-multicolor.ico')
root.geometry("400x400")

#databases
#create a database or connect to one

conn = sqlite3.connect('adress_book.db')
#create curser
c = conn.cursor()
#create table
'''
c.execute("""CREATE TABLE addresses(
        id text, 
        email text,
        age integer 
        )""")
'''

def submit():
    conn = sqlite3.connect('adress_book.db')
    #create curser
    c = conn.cursor()

    #insert table
    c.execute("INSERT INTO addresses VALUES (:f_name, :f_email, :f_age)",
            {
                'f_name':f_name.get(),
                'f_email':f_email.get(),
                'f_age':f_age.get()
            })
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    f_email.delete(0,END)
    f_age.delete(0,END)

    
def query():

    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=4,column=0,columnspan=2)
    

    conn.commit()
    conn.close()
     



f_name =Entry(root,width=30)
f_name.grid(row=1,column=0,padx=20)

f_email =Entry(root,width=30)
f_email.grid(row=1,column=1)

f_age =Entry(root,width=30)
f_age.grid(row=1,column=2)
#commit changes
conn.commit()

#create text box label
f_name_label = Label(root,text="First name")
f_name_label.grid(row=0,column=0)

f_email_label = Label(root,text="Email")
f_email_label.grid(row=0,column=1)

f_age_label = Label(root,text="age")
f_age_label.grid(row=0,column=2)

#create button
summit_btn = Button(root,text="Add Record to database",command=submit)
summit_btn.grid(row=2,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a query button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#close connection
conn.close()

root.mainloop()
