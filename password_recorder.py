from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from addAccount import *
from viewAccounts import *
from deleteAccount import *
from findAccount import *

mydatabase = "password_recorder"
con = pymysql.connect(host="192.168.1.20", user="root", database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Password recorder")
root.minsize(width=400, height=400)
root.geometry("600x500")

Canvas1 = Canvas(root)
Canvas1.config(bg='light blue')
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg='red', bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome \n Anıl Altan's account",
                     bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text='Add a new account',
              bg='black', fg='white', command=addAccount)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text='View Accounts',
              bg='black', fg='white', command=View)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Delete Account",
              bg='black', fg='white', command=delete)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Find Account",
              bg='black', fg='white', command=find)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

root.mainloop()
