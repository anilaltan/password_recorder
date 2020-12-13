from tkinter import *
from tkinter import messagebox
import pymysql


def accountRegister():
    accountname = accoountInfo1.get()
    username = accoountInfo2.get()
    email = accoountInfo3.get()
    password = accoountInfo4.get()

    insertAccounts = "insert into "+accountTable + \
        " values ('"+accountname+"','"+username+"','"+email+"','"+password+"')"
    try:
        cur.execute(insertAccounts)
        con.commit()
        messagebox.showinfo('Success', 'Account Added Successfully')
    except:
        messagebox.showinfo('Error', "Can't add data into database")

    root.destroy()


def addAccount():
    global accoountInfo1, accoountInfo2, accoountInfo3, accoountInfo4, Canvas1, con, cur, accountTable, RADIOBUTTON, root

    root = Tk()
    root.title("Password recorder")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mydatabase = "password_recorder"
    con = pymysql.connect(host="192.168.1.22",
                          user="root", database=mydatabase)
    cur = con.cursor()

    accountTable = "accounts"

    Canvas1 = Canvas(root)
    Canvas1.config(bg='orange')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg='#FFBB00', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headinglabel = Label(headingFrame1, text="Add Account",
                         bg='black', fg='white', font=('Courier', 15))
    headinglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg='black')
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = Label(LabelFrame, text="Account Name : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    accoountInfo1 = Entry(LabelFrame)
    accoountInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(LabelFrame, text="Username : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    accoountInfo2 = Entry(LabelFrame)
    accoountInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    lb3 = Label(LabelFrame, text="Email : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    accoountInfo3 = Entry(LabelFrame)
    accoountInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(LabelFrame, text="Password : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    accoountInfo4 = Entry(LabelFrame)
    accoountInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root, text="SUBMIT", bg='#d1CCC0',
                       fg='black', command=accountRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='#F7F1E3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
