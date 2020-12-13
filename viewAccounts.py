from tkinter import *
from tkinter import messagebox
import pymysql

mydatabase = "password_recorder"
con = pymysql.connect(host="192.168.1.22",
                      user="root", database=mydatabase)
cur = con.cursor()

accountTable = "accounts"


def View():
    root = Tk()
    root.title("Password recorder")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12A4D9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Accounts",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg='black')
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25
    Label(LabelFrame, text="%-15s%-50s%-30s%-20s" % ('AccountName ', '      username',
                                                     'email', 'password'), bg='black', fg='white').place(relx=0.09, rely=0.1)
    Label(LabelFrame, text="----------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    getAccounts = "select * from "+accountTable
    try:
        cur.execute(getAccounts)
        con.commit()

        for i in cur:
            Label(LabelFrame, text="%-15s%-50s%-30s%-20s" %
                  (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#F7F1E3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
