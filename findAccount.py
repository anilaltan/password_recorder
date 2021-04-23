from tkinter import *
from tkinter import messagebox
import pymysql

mydatabase = "password_recorder"
con = pymysql.connect(host="192.168.1.20", user="root", database=mydatabase)
cur = con.cursor()

accountTable = "accounts"


def find():
    global labelFrame, lb1, inf1, qutiBtn, root, Canvas1

    root = Tk()
    root.title("Find Account")
    root.minsize(width=400, height=400)
    root.geometry("600x300")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12A4D9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=2)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Find Account",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Account Name : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.5, relwidth=0.62)

    findBtn = Button(root, text="Find", bg='#d1ccc0',
                     fg='black', command=findedAccount)
    findBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def findedAccount():
    root = Tk()
    root.title("Find Account")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12A4D9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=1)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Accounts",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg='black', bd=1)
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.6

    Label(LabelFrame, text="%-20s%-25s%-45s%-20s" % ('AccountName', 'Username',
                                                     'Email', 'Password'), bg='black', fg='white').place(relx=0.04, rely=0.4)
    Label(LabelFrame, text="----------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.04, rely=0.5)

    findAccountName = inf1.get()
    getAccount = "select * from "+accountTable + \
        " where accountname = '"+findAccountName+"'"

    try:
        cur.execute(getAccount)
        con.commit()

        for i in cur:
            Label(LabelFrame, text="%-15s%-50s%-30s%-20s" %
                  (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.04, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#F7F1E3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
