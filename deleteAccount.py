from tkinter import *
from tkinter import messagebox
import pymysql

mydatabase = "password_recorder"
con = pymysql.connect(host="192.168.1.20",
                      user="root", database=mydatabase)
cur = con.cursor()

accountTable = "accounts"


def deleteAccount():
    accountName = accountInfo1.get()
    deleteSql = "delete from "+accountTable + \
        " where accountname = '"+accountName+"'"

    try:
        cur.execute(deleteSql)
        con.commit()

        messagebox.showinfo('Success', "Account Record Delete Successfully")
    except:
        messagebox.showinfo("Please Check Account Name")

    print(accountName)

    accountInfo1.delete(0, END)
    root.destroy()


def delete():
    global accountInfo1, Canvas1, con, cur, accountTable, root

    root = Tk()
    root.title("Account")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Account",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb2 = Label(labelFrame, text="Account Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    accountInfo1 = Entry(labelFrame)
    accountInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="SUBMIT", bg='#D1CCC0',
                       fg='black', command=deleteAccount)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
