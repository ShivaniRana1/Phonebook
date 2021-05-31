from tkinter import *
from tkinter import ttk
import sqlite3

def create_tables():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE customers (
        first_name text,
        adress_name text,
        email text,
        phoneNo integer    
    )""")
    conn.commit()
    conn.close()

def show_all():
    global win
    win = Tk()
    win.title("shivani phonebook")
    win.iconbitmap('/Users/mac/Downloads/Tatice-Cristal-Intense-Apple-multicolor.ico')
    win.geometry("400x400")
    l = Label(win,text="First Column are Row ID \n You can Delete contact using ROW ID",font=("Arial", 15),fg="hotpink",pady=5).pack()
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()
    c.execute("SELECT rowid, *FROM customers ORDER BY  first_name")
    items = c.fetchall()
    print_records = ''
    for item in items:
        print_records += str(item[0])+ " "+str(item[1])+" "+str(item[2]) + " "+str(item[3])+" "+str(item[4])+ "\n"

    query_label = Label(win,text=print_records)
    query_label.pack()
    button_contact_exit = Button(win,text='EXIT',command=win.destroy).pack()
    
    conn.commit()
    conn.close()

def add_one(Name,Address,Email,phoneNo):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?,?)",(Name,Address,Email,phoneNo))
    conn.commit()
    conn.close()

def delete_one(id):
    
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE  rowid =(?)",(id,))
    conn.commit()
    conn.close()
