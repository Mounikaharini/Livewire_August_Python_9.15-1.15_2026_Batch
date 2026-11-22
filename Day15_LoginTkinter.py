
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql as sql
a = tk.Tk()
a.title("Welcome to login")
a.geometry("1600x1000")
a.config(bg="black")
title = Label(a, text="Welcome To Login Page",font=("Script MT Bold", 40),bg="black",fg="white")
title.pack()

username = Label(a, text="Username",font=("Calibri", 20),bg="black",fg="white")
username.place(x=450,y=200)
usernameEntry = Entry(a,font=("Calibri", 20),bg="black",fg="white")
usernameEntry.place(x=600,y=200)
password = Label(a, text="Password",font=("Calibri", 20),bg="black",fg="white")
password.place(x=450,y=300)
passwordEntry = Entry(a,font=("Calibri", 20),bg="black",fg="white",show="*")
passwordEntry.place(x=600,y=300)
def submit():
    u = usernameEntry.get()
    p = passwordEntry.get()
    if u=="" or p=="":
        messagebox.showwarning("Message","Fill All The Details")
    elif u=="admin" and p=="1234":
        import datetime as d
        date = str(d.datetime.now())
        db = sql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="mounika"
            )
        c = db.cursor()
        query = "insert into loginDetails values('%s','%s','%s')"%(u,p,date)
        try:
            c.execute(query)
            db.commit()
            messagebox.showinfo("Message","Logged In Successfully")
            import register
        except Exception as e:
            messagebox.showinfo("Message","Login Failed! Try Again!!")
        db.close()
    else:
        messagebox.showerror("Message","Incorrect Username or Password")

submit = Button(a, width=31,text="Submit Login",font=("Calibri", 20),bg="black",fg="white",command=submit)
submit.place(x=450,y=400)
a.mainloop()
