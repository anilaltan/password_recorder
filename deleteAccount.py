from tkinter import *
from tkinter import messagebox
import pymysql

mydatabase = "password_recorder"
con = pymysql.connect(host="192.168.1.22",
                      user="root", database=mydatabase)
cur = con.cursor()

accountTable = "accounts"


def deleteAccount():
