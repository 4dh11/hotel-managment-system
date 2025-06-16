import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sql

con = sql.connect(host='localhost', user='root', passwd='', database='thamanyas_resort')
c = con.cursor()
from tkinter import *
from tkcalendar import *
from datetime import datetime
from PIL import ImageTk, Image

root = Tk()

uname = StringVar()

days = 0

d2 = ''
d1 = ''

count = 0

i = 10
j = 8
k = 8
l = 4

i1 = 0
j1 = 0
k1 = 0
l1 = 0

nt1 = 0
nt2 = 0
nt3 = 0
nt4 = 0
nt5 = 0
nt6 = 0
nt7 = 0
nt8 = 0
nt9 = 0
nt10 = 0
nt11 = 0


def who():
    root.title('User Confirmation')
    root.geometry('250x165+590+250')
    root.configure(background='#FFE26F')

    root.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root, text='', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, columnspan=2, padx=30)
    row1 = Label(root, text='Welcome to', font='tkdefault 14 bold', bg='red')
    row1.grid(row=1, columnspan=2, padx=30)
    row2 = Label(root, text='Thamanyas Resort', font='tkdefault 14 bold', bg='red')
    row2.grid(row=2, columnspan=2, padx=30)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\who.png")
    bg_label = Label(root, image=bg)
    bg_label.place(x=-2, y=-2)

    cust = Button(root, text='Customer', command=cust_login, bg='#e09f3e', fg='#540b0e')
    cust.grid(row=3, column=0, padx=15, pady=14)
    emp = Button(root, text='Employee', command=emp_login, bg='#e09f3e', fg='#540b0e')
    emp.grid(row=3, column=1, padx=10, pady=14)

    root.mainloop()


def cust_signin():
    global uname
    signup = Toplevel()

    def back1():
        signup.destroy()
        cust_login()

    def submit():
        rec1 = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Customer SignIn Details.csv', sep=',')
        if name.get() in rec1.values:
            answer.config(text='Username already taken')
            name.delete(0, END)
        elif name.get() not in rec1.values:
            if conpwd.get() != pwd.get():
                answer.config(text='Re-enter password')
                pwd.delete(0, END)
                conpwd.delete(0, END)
            elif conpwd.get() == pwd.get():
                c.execute(
                    "INSERT INTO CUST_SIGNIN VALUES ('{}',{},{},'{}','{}')".format(name.get(), age.get(), phone.get(),
                                                                                   email.get(), pwd.get()))
                con.commit()
                rec = pd.read_sql("SELECT * FROM CUST_SIGNIN", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Customer SignIn Details.csv', sep=',')
                signup.destroy()
                homepg()

    signup.title('Sign In')
    signup.geometry('390x330+520+180')
    signup.configure(background='#FFE26F')

    signup.wm_attributes('-transparentcolor', 'red')
    row0 = Label(signup, text='Sign In', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, columnspan=2, padx=20, pady=20)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\cust_signin.png")
    bg_label = Label(signup, image=bg)
    bg_label.place(x=-2, y=-2)

    name = Entry(signup, textvariable=uname, width=30)
    name.grid(row=1, column=1, padx=20, pady=5)
    age = Entry(signup, width=30)
    age.grid(row=2, column=1, padx=20, pady=5)
    phone = Entry(signup, width=30)
    phone.grid(row=3, column=1, padx=20, pady=5)
    email = Entry(signup, width=30)
    email.grid(row=4, column=1, padx=20, pady=5)
    pwd = Entry(signup, width=30)
    pwd.grid(row=5, column=1, padx=20, pady=5)
    conpwd = Entry(signup, width=30)
    conpwd.grid(row=6, column=1, padx=20, pady=5)

    uname_label = Label(signup, text='Username', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    uname_label.grid(row=1, column=0, padx=20)
    age_label = Label(signup, text='Age', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    age_label.grid(row=2, column=0, padx=20)
    phone_label = Label(signup, text='Phone no.', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    phone_label.grid(row=3, column=0, padx=20)
    email_label = Label(signup, text='EmaiID', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    email_label.grid(row=4, column=0, padx=20)
    pwd_label = Label(signup, text='Password', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    pwd_label.grid(row=5, column=0, padx=20)
    conpwd_label = Label(signup, text='Confirm Password', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    conpwd_label.grid(row=6, column=0, padx=20)

    signin = Button(signup, text='Sign In', command=submit, bg='#e09f3e', fg='#540b0e')
    signin.grid(row=7, columnspan=2, pady=10, padx=10, ipadx=50)
    answer = Label(signup, text='', bg='#FFE26F', fg='#540b0e')
    answer.grid(row=8, columnspan=2)
    back = Button(signup, text='<<', command=back1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    signup.mainloop()


def cust_login():
    global uname
    log1 = Toplevel()

    def signup():
        log1.destroy()
        cust_signin()

    def submit():
        rec = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Customer SignIn Details.csv', sep=',')
        if name.get() not in rec.values:
            answer.config(text='Incorrect Username')
            name.delete(0, END)
        elif email.get() not in rec.values:
            answer.config(text='Incorrect EmailID')
            email.delete(0, END)
        elif pwd.get() not in rec.values:
            answer.config(text='Incorrect Password')
            pwd.delete(0, END)
        elif name.get() in rec.values and email.get() in rec.values and pwd.get() in rec.values:
            log1.destroy()
            homepg()

    log1.title('Log In')
    log1.geometry('360x280+530+200')
    log1.configure(background='#FFE26F')

    log1.wm_attributes('-transparentcolor', 'red')
    row0 = Label(log1, text='Log In', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, columnspan=2, padx=20, pady=20)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\cust_login.png")
    bg_label = Label(log1, image=bg)
    bg_label.place(x=-2, y=-2)

    name = Entry(log1, textvariable=uname, width=30)
    name.grid(row=1, column=1, padx=20, pady=5)
    email = Entry(log1, width=30)
    email.grid(row=2, column=1, padx=20, pady=5)
    pwd = Entry(log1, width=30)
    pwd.grid(row=3, column=1, padx=20, pady=5)

    uname_label = Label(log1, text='Username', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    uname_label.grid(row=1, column=0, padx=30)
    email_label = Label(log1, text='EmaiID', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    email_label.grid(row=2, column=0, padx=30)
    pwd_label = Label(log1, text='Password', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    pwd_label.grid(row=3, column=0, padx=30)

    signin = Button(log1, text='Log In', command=submit, bg='#e09f3e', fg='#540b0e')
    signin.grid(row=4, columnspan=2, pady=5, padx=10, ipadx=50)
    answer = Label(log1, text='', bg='#FFE26F', fg='#540b0e')
    answer.grid(row=5, pady=5, columnspan=2)
    signin = Button(log1, text='Sign Up', command=signup, bg='#e09f3e', fg='#540b0e')
    signin.grid(row=6, column=1, padx=20, pady=10, sticky=E)

    log1.mainloop()


def emp_login():
    log2 = Toplevel()

    def submit():
        rec = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Employee LogIn Details.csv', sep=',')
        if email.get() not in rec.values or pwd.get() not in rec.values:
            answer.config(text='Re-enter Email(or)password')
            email.delete(0, END)
            pwd.delete(0, END)
        elif email.get() in rec.values and pwd.get() in rec.values:
            answer.config(text='Account has been accessed')
            log2.destroy()
            emphome()

    log2.title('Log In')
    log2.geometry('370x220+530+230')
    log2.configure(background='#FFE26F')

    log2.wm_attributes('-transparentcolor', 'red')
    row0 = Label(log2, text='Log In', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, columnspan=2, padx=20, pady=20)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\emp_login.png")
    bg_label = Label(log2, image=bg)
    bg_label.place(x=-2, y=-2)

    email = Entry(log2, width=30)
    email.grid(row=1, column=1, padx=20, pady=5)
    pwd = Entry(log2, width=30)
    pwd.grid(row=2, column=1, padx=20, pady=5)

    email_label = Label(log2, text='EmaiID', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    email_label.grid(row=1, column=0, padx=30)
    pwd_label = Label(log2, text='Password', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    pwd_label.grid(row=2, column=0, padx=30)

    signin = Button(log2, text='Log In', command=submit, bg='#e09f3e', fg='#540b0e')
    signin.grid(row=3, columnspan=2, pady=5, padx=10, ipadx=50)
    answer = Label(log2, text='', bg='#FFE26F', fg='#540b0e')
    answer.grid(row=4, pady=5, columnspan=2)

    log2.mainloop()


def room():
    global d2
    global d1
    global uname
    global days
    global i
    global j
    global k
    global l
    global i1
    global j1
    global k1
    global l1
    
    root1 = Toplevel()
    root1.title('Room Booking')
    root1.geometry('880x540+250+60')
    root1.configure(background='#FFE26F')

    root1.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root1, text='Room Booking', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=3, pady=20)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\room.png")
    bg_label = Label(root1, image=bg)
    bg_label.place(x=-2, y=-2)

    def submit():
        global uname
        global i
        global j
        global k
        global l
        global i1
        global j1
        global k1
        global l1

        d2 = checkout.get_date()
        d1 = checkin.get_date()
        d1 = datetime.strptime(d1, '%m/%d/%y')
        d2 = datetime.strptime(d2, '%m/%d/%y')
        delta = d2 - d1
        days = delta.days

        if var1.get():
            i = i - i1
            if room1nor.cget('text') > 0:
                c.execute(
                    "INSERT INTO ROOM(NAME,TYPE,NOR,CHECKIN,CHECKOUT,ROOM_COST) VALUES ('{}','{}',{},'{}','{}',{})".format(
                        uname.get(), room1.cget('text'), room1nor.cget('text'), checkin.get_date(), checkout.get_date(),
                        (float(room1nor.cget('text')) * (float(room1cost.cget('text'))) * float(days))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room.csv', sep=',')
            if room1nora.cget('text') == 0:
                room1.deselect()
                room1.config(state='disabled')

        if var2.get():
            j = j - j1
            if room2nor.cget('text') > 0:
                c.execute(
                    "INSERT INTO ROOM(NAME,TYPE,NOR,CHECKIN,CHECKOUT,ROOM_COST) VALUES ('{}','{}',{},'{}','{}',{})".format(
                        uname.get(), room2.cget('text'), room2nor.cget('text'), checkin.get_date(), checkout.get_date(),
                        (float(room2nor.cget('text')) * (float(room2cost.cget('text'))) * float(days))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room.csv', sep=',')
            if room2nora.cget('text') == 0:
                room2.deselect()
                room2.config(state='disabled')

        if var3.get():
            k = k - k1
            if room3nor.cget('text') > 0:
                c.execute(
                    "INSERT INTO ROOM(NAME,TYPE,NOR,CHECKIN,CHECKOUT,ROOM_COST) VALUES ('{}','{}',{},'{}','{}',{})".format(
                        uname.get(), room3.cget('text'), room3nor.cget('text'), checkin.get_date(), checkout.get_date(),
                        (float(room3nor.cget('text')) * (float(room3cost.cget('text'))) * float(days))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room.csv', sep=',')
            if room3nora.cget('text') == 0:
                room3.deselect()
                room3.config(state='disabled')

        if var4.get():
            l = l - l1
            if room4nor.cget('text') > 0:
                c.execute(
                    "INSERT INTO ROOM(NAME,TYPE,NOR,CHECKIN,CHECKOUT,ROOM_COST) VALUES ('{}','{}',{},'{}','{}',{})".format(
                        uname.get(), room4.cget('text'), room4nor.cget('text'), checkin.get_date(), checkout.get_date(),
                        (float(room4nor.cget('text')) * (float(room4cost.cget('text'))) * float(days))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room.csv', sep=',')
            if room4nora.cget('text') == 0:
                room4.deselect()
                room4.config(state='disabled')

        c.execute(
            "INSERT INTO ADMIN_DETAILS(TYPE,NAME,CHECKIN,CHECKOUT,ROOM_COST) SELECT TYPE,NAME,CHECKIN,CHECKOUT,SUM(ROOM_COST) FROM ROOM GROUP BY TYPE,CHECKIN,NAME")
        con.commit()
        room1nora.config(text=i)
        room2nora.config(text=j)
        room3nora.config(text=k)
        room4nora.config(text=l)
        i1 = 0
        j1 = 0
        k1 = 0
        l1 = 0
        root1.destroy()

    room = Label(root1, text='Rooms Available', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    room.grid(row=1, column=0, padx=20)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    room1 = Checkbutton(root1, text='Single Bedroom', variable=var1, onvalue='Single Bedroom', offvalue='',
                        bg='#FFE26F', fg='#540b0e')
    room1.grid(row=2, column=0, padx=20, pady=5, sticky=W)
    room2 = Checkbutton(root1, text='Double Bedroom', variable=var2, onvalue='Double Bedroom', offvalue='',
                        bg='#FFE26F', fg='#540b0e')
    room2.grid(row=3, column=0, padx=20, pady=5, sticky=W)
    room3 = Checkbutton(root1, text='Double-Double Bedroom', variable=var3, onvalue='Double-Double Bedroom',
                        offvalue='', bg='#FFE26F', fg='#540b0e')
    room3.grid(row=4, column=0, padx=20, pady=5, sticky=W)
    room4 = Checkbutton(root1, text='Suite', variable=var4, onvalue='Suite', offvalue='', bg='#FFE26F', fg='#540b0e')
    room4.grid(row=5, column=0, padx=20, pady=5, sticky=W)

    nop = Label(root1, text='No. of People', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    nop.grid(row=1, column=1, padx=20)
    room1nop = Label(root1, text='1', bg='#FFE26F', fg='#540b0e')
    room1nop.grid(row=2, column=1)
    room2nop = Label(root1, text='2', bg='#FFE26F', fg='#540b0e')
    room2nop.grid(row=3, column=1)
    room3nop = Label(root1, text='4', bg='#FFE26F', fg='#540b0e')
    room3nop.grid(row=4, column=1)
    room4nop = Label(root1, text='6', bg='#FFE26F', fg='#540b0e')
    room4nop.grid(row=5, column=1)

    def add1():
        if var1.get():
            global i
            global i1
            if i1==i:
                plus1.config(state='disabled')
                plus1.config(state='normal')
            else:
                i1 = i1 + 1
                room1nor.config(text=i1)
                plus2.config(state='disabled')
                plus3.config(state='disabled')
                plus4.config(state='disabled')
                plus2.config(state='normal')
                plus3.config(state='normal')
                plus4.config(state='normal')

    def add2():
        if var2.get():
            global j
            global j1
            if j1==j:
                plus2.config(state='disabled')
                plus2.config(state='normal')
            else:
                j1 = j1 + 1
                room2nor.config(text=j1)
                plus1.config(state='disabled')
                plus3.config(state='disabled')
                plus4.config(state='disabled')
                plus1.config(state='normal')
                plus3.config(state='normal')
                plus4.config(state='normal')

    def add3():
        if var3.get():
            global k
            global k1
            if k1==k:
                plus3.config(state='disabled')
                plus3.config(state='normal')
            else:
                k1 = k1 + 1
                room3nor.config(text=k1)
                plus1.config(state='disabled')
                plus2.config(state='disabled')
                plus4.config(state='disabled')
                plus1.config(state='normal')
                plus2.config(state='normal')
                plus4.config(state='normal')

    def add4():
        if var4.get():
            global l
            global l1
            if l1==l:
                plus4.config(state='disabled')
                plus4.config(state='normal')
            else:
                l1 = l1 + 1
                room4nor.config(text=l1)
                plus1.config(state='disabled')
                plus2.config(state='disabled')
                plus3.config(state='disabled')
                plus1.config(state='normal')
                plus2.config(state='normal')
                plus3.config(state='normal')

    def rem1():
        global i1
        if i1 == 0:
            minus1.config(state='disabled')
            minus1.config(state='normal')
        else:
            minus1.config(state='normal')
            i1 = i1 - 1
            room1nor.config(text=i1)

    def rem2():
        global j1
        if j1 == 0:
            minus2.config(state='disabled')
            minus2.config(state='normal')
        else:
            minus2.config(state='normal')
            j1 = j1 - 1
            room2nor.config(text=j1)

    def rem3():
        global k1
        if k1 == 0:
            minus3.config(state='disabled')
            minus3.config(state='normal')
        else:
            minus3.config(state='normal')
            k1 = k1 - 1
            room3nor.config(text=k1)

    def rem4():
        global l1
        if l1 == 0:
            minus4.config(state='disabled')
            minus4.config(state='normal')
        else:
            minus4.config(state='normal')
            l1 = l1 - 1
            room4nor.config(text=l1)

    nor = Label(root1, text='No. of Rooms', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    nor.grid(row=1, column=2, columnspan=3, padx=20)
    room1nor = Label(root1, text=i1, bg='#FFE26F', fg='#540b0e')
    room1nor.grid(row=2, column=3)
    room2nor = Label(root1, text=j1, bg='#FFE26F', fg='#540b0e')
    room2nor.grid(row=3, column=3)
    room3nor = Label(root1, text=k1, bg='#FFE26F', fg='#540b0e')
    room3nor.grid(row=4, column=3)
    room4nor = Label(root1, text=l1, bg='#FFE26F', fg='#540b0e')
    room4nor.grid(row=5, column=3)

    plus1 = Button(root1, text='+', command=add1, bg='#e09f3e', fg='#540b0e')
    plus1.grid(row=2, column=4, padx=5)
    plus2 = Button(root1, text='+', command=add2, bg='#e09f3e', fg='#540b0e')
    plus2.grid(row=3, column=4, padx=5)
    plus3 = Button(root1, text='+', command=add3, bg='#e09f3e', fg='#540b0e')
    plus3.grid(row=4, column=4, padx=5)
    plus4 = Button(root1, text='+', command=add4, bg='#e09f3e', fg='#540b0e')
    plus4.grid(row=5, column=4, padx=5)

    minus1 = Button(root1, text='-', command=rem1, bg='#e09f3e', fg='#540b0e')
    minus1.grid(row=2, column=2, padx=10)
    minus2 = Button(root1, text='-', command=rem2, bg='#e09f3e', fg='#540b0e')
    minus2.grid(row=3, column=2, padx=10)
    minus3 = Button(root1, text='-', command=rem3, bg='#e09f3e', fg='#540b0e')
    minus3.grid(row=4, column=2, padx=10)
    minus4 = Button(root1, text='-', command=rem4, bg='#e09f3e', fg='#540b0e')
    minus4.grid(row=5, column=2, padx=10)

    nora = Label(root1, text='No. of Rooms Available', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    nora.grid(row=1, column=6, padx=20)
    room1nora: Label = Label(root1, text=i, bg='#FFE26F', fg='#540b0e')
    room1nora.grid(row=2, column=6)
    room2nora = Label(root1, text=j, bg='#FFE26F', fg='#540b0e')
    room2nora.grid(row=3, column=6)
    room3nora = Label(root1, text=k, bg='#FFE26F', fg='#540b0e')
    room3nora.grid(row=4, column=6)
    room4nora = Label(root1, text=l, bg='#FFE26F', fg='#540b0e')
    room4nora.grid(row=5, column=6)

    cost = Label(root1, text='Room Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    cost.grid(row=1, column=7, padx=20)
    room1cost = Label(root1, text='1000', bg='#FFE26F', fg='#540b0e')
    room1cost.grid(row=2, column=7)
    room2cost = Label(root1, text='2000', bg='#FFE26F', fg='#540b0e')
    room2cost.grid(row=3, column=7)
    room3cost = Label(root1, text='4000', bg='#FFE26F', fg='#540b0e')
    room3cost.grid(row=4, column=7)
    room4cost = Label(root1, text='8000', bg='#FFE26F', fg='#540b0e')
    room4cost.grid(row=5, column=7)

    checkin = Calendar(root1, selectmode='day', year=2022, month=12)
    checkin.grid(row=9, column=0, columnspan=3, pady=10)
    checkin_label = Label(root1, text='CheckIn Date', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    checkin_label.grid(row=8, column=0, columnspan=2, pady=10)
    checkout = Calendar(root1, selectmode='day', year=2022, month=12)
    checkout.grid(row=9, column=4, columnspan=4, padx=20, pady=10)
    checkout_label = Label(root1, text='CheckOut Date', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    checkout_label.grid(row=8, column=6, columnspan=2, pady=10)

    def back1():
        global i1
        global j1
        global k1
        global l1
        i1 = 0
        j1 = 0
        k1 = 0
        l1 = 0
        root1.destroy()

    book = Button(root1, text='Book', width=15, command=submit, bg='#e09f3e', fg='#540b0e')
    book.grid(row=10, column=3, pady=10)
    back = Button(root1, text='<<', command=back1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    root1.mainloop()


def room_service():
    root2 = Toplevel()
    root2.title('Room Service')
    root2.geometry('540x590+430+30')
    root2.configure(background='#FFE26F')

    root2.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root2, text='Room Service', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=3, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\room_service.png")
    bg_label = Label(root2, image=bg)
    bg_label.place(x=-2, y=-2)

    def order():
        global uname
        global count
        global nt1
        global nt2
        global nt3
        global nt4
        global nt5
        global nt6
        global nt7
        global nt8
        global nt9
        global nt10
        global nt11

        if var1.get():
            if qtty1.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item1.cget('text'), qtty1.cget('text'),
                        (float(qtty1.cget('text')) * float(cost1.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty2.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item2.cget('text'), qtty2.cget('text'),
                        (float(qtty2.cget('text')) * float(cost2.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty3.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item3.cget('text'), qtty3.cget('text'),
                        (float(qtty3.cget('text')) * float(cost3.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty4.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item4.cget('text'), qtty4.cget('text'),
                        (float(qtty4.cget('text')) * float(cost4.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty5.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item5.cget('text'), qtty5.cget('text'),
                        (float(qtty5.cget('text')) * float(cost5.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty6.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item6.cget('text'), qtty6.cget('text'),
                        (float(qtty6.cget('text')) * float(cost6.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty7.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item7.cget('text'), qtty7.cget('text'),
                        (float(qtty7.cget('text')) * float(cost7.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty8.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item8.cget('text'), qtty8.cget('text'),
                        (float(qtty8.cget('text')) * float(cost8.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty9.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item9.cget('text'), qtty9.cget('text'),
                        (float(qtty9.cget('text')) * float(cost9.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty10.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item10.cget('text'), qtty10.cget('text'),
                        (float(qtty10.cget('text')) * float(cost10.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty11.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var1.get(), item11.cget('text'), qtty11.cget('text'),
                        (float(qtty11.cget('text')) * float(cost11.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            c.execute(
                "UPDATE ADMIN_DETAILS SET SERVICE_COST=(SELECT SUM(ITEM_PRICE) FROM ROOM_SERVICE WHERE NAME='{}' AND TYPE='{}') WHERE NAME='{}' AND TYPE='{}'".format(
                    uname.get(), var1.get(), uname.get(), var1.get()))
            con.commit()

        if var2.get():
            if qtty1.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item1.cget('text'), qtty1.cget('text'),
                        (float(qtty1.cget('text')) * float(cost1.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty2.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item2.cget('text'), qtty2.cget('text'),
                        (float(qtty2.cget('text')) * float(cost2.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty3.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item3.cget('text'), qtty3.cget('text'),
                        (float(qtty3.cget('text')) * float(cost3.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty4.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item4.cget('text'), qtty4.cget('text'),
                        (float(qtty4.cget('text')) * float(cost4.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty5.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item5.cget('text'), qtty5.cget('text'),
                        (float(qtty5.cget('text')) * float(cost5.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty6.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item6.cget('text'), qtty6.cget('text'),
                        (float(qtty6.cget('text')) * float(cost6.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty7.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item7.cget('text'), qtty7.cget('text'),
                        (float(qtty7.cget('text')) * float(cost7.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty8.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item8.cget('text'), qtty8.cget('text'),
                        (float(qtty8.cget('text')) * float(cost8.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty9.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item9.cget('text'), qtty9.cget('text'),
                        (float(qtty9.cget('text')) * float(cost9.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty10.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item10.cget('text'), qtty10.cget('text'),
                        (float(qtty10.cget('text')) * float(cost10.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty11.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var2.get(), item11.cget('text'), qtty11.cget('text'),
                        (float(qtty11.cget('text')) * float(cost11.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            c.execute(
                "UPDATE ADMIN_DETAILS SET SERVICE_COST=(SELECT SUM(ITEM_PRICE) FROM ROOM_SERVICE WHERE NAME='{}' AND TYPE='{}') WHERE NAME='{}' AND TYPE='{}'".format(
                    uname.get(), var2.get(), uname.get(), var2.get()))
            con.commit()

        if var3.get():
            if qtty1.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item1.cget('text'), qtty1.cget('text'),
                        (float(qtty1.cget('text')) * float(cost1.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty2.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item2.cget('text'), qtty2.cget('text'),
                        (float(qtty2.cget('text')) * float(cost2.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty3.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item3.cget('text'), qtty3.cget('text'),
                        (float(qtty3.cget('text')) * float(cost3.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty4.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item4.cget('text'), qtty4.cget('text'),
                        (float(qtty4.cget('text')) * float(cost4.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty5.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item5.cget('text'), qtty5.cget('text'),
                        (float(qtty5.cget('text')) * float(cost5.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty6.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item6.cget('text'), qtty6.cget('text'),
                        (float(qtty6.cget('text')) * float(cost6.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty7.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item7.cget('text'), qtty7.cget('text'),
                        (float(qtty7.cget('text')) * float(cost7.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty8.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item8.cget('text'), qtty8.cget('text'),
                        (float(qtty8.cget('text')) * float(cost8.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty9.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item9.cget('text'), qtty9.cget('text'),
                        (float(qtty9.cget('text')) * float(cost9.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty10.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item10.cget('text'), qtty10.cget('text'),
                        (float(qtty10.cget('text')) * float(cost10.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty11.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var3.get(), item11.cget('text'), qtty11.cget('text'),
                        (float(qtty11.cget('text')) * float(cost11.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            c.execute(
                "UPDATE ADMIN_DETAILS SET SERVICE_COST=(SELECT SUM(ITEM_PRICE) FROM ROOM_SERVICE WHERE NAME='{}' AND TYPE='{}') WHERE NAME='{}' AND TYPE='{}'".format(
                    uname.get(), var3.get(), uname.get(), var3.get()))
            con.commit()

        if var4.get():
            if qtty1.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item1.cget('text'), qtty1.cget('text'),
                        (float(qtty1.cget('text')) * float(cost1.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty2.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item2.cget('text'), qtty2.cget('text'),
                        (float(qtty2.cget('text')) * float(cost2.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty3.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item3.cget('text'), qtty3.cget('text'),
                        (float(qtty3.cget('text')) * float(cost3.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty4.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item4.cget('text'), qtty4.cget('text'),
                        (float(qtty4.cget('text')) * float(cost4.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty5.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item5.cget('text'), qtty5.cget('text'),
                        (float(qtty5.cget('text')) * float(cost5.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty6.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item6.cget('text'), qtty6.cget('text'),
                        (float(qtty6.cget('text')) * float(cost6.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty7.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item7.cget('text'), qtty7.cget('text'),
                        (float(qtty7.cget('text')) * float(cost7.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty8.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item8.cget('text'), qtty8.cget('text'),
                        (float(qtty8.cget('text')) * float(cost8.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty9.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item9.cget('text'), qtty9.cget('text'),
                        (float(qtty9.cget('text')) * float(cost9.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty10.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item10.cget('text'), qtty10.cget('text'),
                        (float(qtty10.cget('text')) * float(cost10.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            if qtty11.cget('text') > 0:
                count = count + 1
                c.execute(
                    "INSERT INTO ROOM_SERVICE(NAME,TYPE,ITEM_NAME,QTTY,ITEM_PRICE) VALUES ('{}','{}','{}',{},{})".format(
                        uname.get(), var4.get(), item11.cget('text'), qtty11.cget('text'),
                        (float(qtty11.cget('text')) * float(cost11.cget('text')))))
                con.commit()
                rec = pd.read_sql("SELECT * FROM ROOM_SERVICE GROUP BY NAME,TYPE", con)
                rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Room Service.csv', sep=',')
            c.execute(
                "UPDATE ADMIN_DETAILS SET SERVICE_COST=(SELECT SUM(ITEM_PRICE) FROM ROOM_SERVICE WHERE NAME='{}' AND TYPE='{}') WHERE NAME='{}' AND TYPE='{}'".format(
                    uname.get(), var4.get(), uname.get(), var4.get()))
            con.commit()
        nt1 = 0
        nt2 = 0
        nt3 = 0
        nt4 = 0
        nt5 = 0
        nt6 = 0
        nt7 = 0
        nt8 = 0
        nt9 = 0
        nt10 = 0
        nt11 = 0
        root2.destroy()
        ur_order()

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    room = Label(root2, text='Room type', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    room.grid(row=2, column=0)

    room1 = Checkbutton(root2, text='Single Bedroom', variable=var1, onvalue='Single Bedroom', offvalue='',
                        bg='#FFE26F', fg='#540b0e')
    room1.grid(row=2, column=1, columnspan=3, padx=20, pady=5)
    room2 = Checkbutton(root2, text='Double Bedroom', variable=var2, onvalue='Double Bedroom', offvalue='',
                        bg='#FFE26F', fg='#540b0e')
    room2.grid(row=3, column=1, columnspan=3, padx=20, pady=5)
    room3 = Checkbutton(root2, text='Double-Double Bedroom', variable=var3, onvalue='Double-Double Bedroom',
                        offvalue='', bg='#FFE26F', fg='#540b0e')
    room3.grid(row=2, column=4, columnspan=2, pady=5)
    room4 = Checkbutton(root2, text='Suite', variable=var4, onvalue='Suite', offvalue='', bg='#FFE26F', fg='#540b0e')
    room4.grid(row=3, column=4, columnspan=2, pady=5)

    menu = Label(root2, text='Menu', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    menu.grid(row=4, column=0, padx=20, pady=10)

    item1 = Label(root2, text='Manchow Soup', bg='#FFE26F', fg='#540b0e')
    item1.grid(row=5, column=0, padx=20, pady=5)
    item2 = Label(root2, text='Paneer Tikka', bg='#FFE26F', fg='#540b0e')
    item2.grid(row=6, column=0, padx=20, pady=5)
    item3 = Label(root2, text='Cheese Corn Nuggets', bg='#FFE26F', fg='#540b0e')
    item3.grid(row=7, column=0, padx=20, pady=5)
    item4 = Label(root2, text='Naan', bg='#FFE26F', fg='#540b0e')
    item4.grid(row=8, column=0, padx=20, pady=5)
    item5 = Label(root2, text='Butter Naan', bg='#FFE26F', fg='#540b0e')
    item5.grid(row=9, column=0, padx=20, pady=5)
    item6 = Label(root2, text='Veg Fried Rice', bg='#FFE26F', fg='#540b0e')
    item6.grid(row=10, column=0, padx=20, pady=5)
    item7 = Label(root2, text='Veg Noodles', bg='#FFE26F', fg='#540b0e')
    item7.grid(row=11, column=0, padx=20, pady=5)
    item8 = Label(root2, text='Chettinad Panner Gravy', bg='#FFE26F', fg='#540b0e')
    item8.grid(row=12, column=0, padx=20, pady=5)
    item9 = Label(root2, text='Pallipalayam Panner', bg='#FFE26F', fg='#540b0e')
    item9.grid(row=13, column=0, padx=20, pady=5)
    item10 = Label(root2, text='Gulab Jamun', bg='#FFE26F', fg='#540b0e')
    item10.grid(row=14, column=0, padx=20, pady=5)
    item11 = Label(root2, text='Kulfi', bg='#FFE26F', fg='#540b0e')
    item11.grid(row=15, column=0, padx=20, pady=5)

    qtty = Label(root2, text='Quantity', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    qtty.grid(row=4, column=2, columnspan=3, padx=10, pady=10)

    def add1():
        global nt1
        nt1 = nt1 + 1
        qtty1.config(text=nt1)

    def add2():
        global nt2
        nt2 = nt2 + 1
        qtty2.config(text=nt2)

    def add3():
        global nt3
        nt3 = nt3 + 1
        qtty3.config(text=nt3)

    def add4():
        global nt4
        nt4 = nt4 + 1
        qtty4.config(text=nt4)

    def add5():
        global nt5
        nt5 = nt5 + 1
        qtty5.config(text=nt5)

    def add6():
        global nt6
        nt6 = nt6 + 1
        qtty6.config(text=nt6)

    def add7():
        global nt7
        nt7 = nt7 + 1
        qtty7.config(text=nt7)

    def add8():
        global nt8
        nt8 = nt8 + 1
        qtty8.config(text=nt8)

    def add9():
        global nt9
        nt9 = nt9 + 1
        qtty9.config(text=nt9)

    def add10():
        global nt10
        nt10 = nt10 + 1
        qtty10.config(text=nt10)

    def add11():
        global nt11
        nt11 = nt11 + 1
        qtty11.config(text=nt11)

    def rem1():
        global nt1
        if nt1 == 0:
            minus1.config(state='disabled')
            minus1.config(state='normal')
        else:
            minus1.config(state='normal')
            nt1 = nt1 - 1
            qtty1.config(text=nt1)

    def rem2():
        global nt2
        if nt2 == 0:
            minus2.config(state='disabled')
            minus2.config(state='normal')
        else:
            minus2.config(state='normal')
            nt2 = nt2 - 1
            qtty2.config(text=nt2)

    def rem3():
        global nt3
        if nt3 == 0:
            minus3.config(state='disabled')
            minus3.config(state='normal')
        else:
            minus3.config(state='normal')
            nt3 = nt3 - 1
            qtty3.config(text=nt3)

    def rem4():
        global nt4
        if nt4 == 0:
            minus4.config(state='disabled')
            minus4.config(state='normal')
        else:
            minus4.config(state='normal')
            nt4 = nt4 - 1
            qtty4.config(text=nt4)

    def rem5():
        global nt5
        if nt5 == 0:
            minus5.config(state='disabled')
            minus5.config(state='normal')
        else:
            minus5.config(state='normal')
            nt5 = nt5 - 1
            qtty5.config(text=nt5)

    def rem6():
        global nt6
        if nt6 == 0:
            minus6.config(state='disabled')
            minus6.config(state='normal')
        else:
            minus6.config(state='normal')
            nt6 = nt6 - 1
            qtty6.config(text=nt6)

    def rem7():
        global nt7
        if nt7 == 0:
            minus7.config(state='disabled')
            minus7.config(state='normal')
        else:
            minus7.config(state='normal')
            nt7 = nt7 - 1
            qtty7.config(text=nt7)

    def rem8():
        global nt8
        if nt8 == 0:
            minus8.config(state='disabled')
            minus8.config(state='normal')
        else:
            minus8.config(state='normal')
            nt8 = nt8 - 1
            qtty8.config(text=nt8)

    def rem9():
        global nt9
        if nt9 == 0:
            minus9.config(state='disabled')
            minus9.config(state='normal')
        else:
            minus9.config(state='normal')
            nt9 = nt9 - 1
            qtty9.config(text=nt9)

    def rem10():
        global nt10
        if nt10 == 0:
            minus10.config(state='disabled')
            minus10.config(state='normal')
        else:
            minus10.config(state='normal')
            nt10 = nt10 - 1
            qtty10.config(text=nt10)

    def rem11():
        global nt11
        if nt11 == 0:
            minus11.config(state='disabled')
            minus11.config(state='normal')
        else:
            minus11.config(state='normal')
            nt11 = nt11 - 1
            qtty11.config(text=nt11)

    qtty1 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty1.grid(row=5, column=3)
    qtty2 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty2.grid(row=6, column=3)
    qtty3 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty3.grid(row=7, column=3)
    qtty4 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty4.grid(row=8, column=3)
    qtty5 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty5.grid(row=9, column=3)
    qtty6 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty6.grid(row=10, column=3)
    qtty7 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty7.grid(row=11, column=3)
    qtty8 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty8.grid(row=12, column=3)
    qtty9 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty9.grid(row=13, column=3)
    qtty10 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty10.grid(row=14, column=3)
    qtty11 = Label(root2, text=0, bg='#FFE26F', fg='#540b0e')
    qtty11.grid(row=15, column=3)

    plus1 = Button(root2, text='+', command=add1, bg='#e09f3e', fg='#540b0e')
    plus1.grid(row=5, column=4)
    plus2 = Button(root2, text='+', command=add2, bg='#e09f3e', fg='#540b0e')
    plus2.grid(row=6, column=4)
    plus3 = Button(root2, text='+', command=add3, bg='#e09f3e', fg='#540b0e')
    plus3.grid(row=7, column=4)
    plus4 = Button(root2, text='+', command=add4, bg='#e09f3e', fg='#540b0e')
    plus4.grid(row=8, column=4)
    plus5 = Button(root2, text='+', command=add5, bg='#e09f3e', fg='#540b0e')
    plus5.grid(row=9, column=4)
    plus6 = Button(root2, text='+', command=add6, bg='#e09f3e', fg='#540b0e')
    plus6.grid(row=10, column=4)
    plus7 = Button(root2, text='+', command=add7, bg='#e09f3e', fg='#540b0e')
    plus7.grid(row=11, column=4)
    plus8 = Button(root2, text='+', command=add8, bg='#e09f3e', fg='#540b0e')
    plus8.grid(row=12, column=4)
    plus9 = Button(root2, text='+', command=add9, bg='#e09f3e', fg='#540b0e')
    plus9.grid(row=13, column=4)
    plus10 = Button(root2, text='+', command=add10, bg='#e09f3e', fg='#540b0e')
    plus10.grid(row=14, column=4)
    plus11 = Button(root2, text='+', command=add11, bg='#e09f3e', fg='#540b0e')
    plus11.grid(row=15, column=4)

    minus1 = Button(root2, text='-', command=rem1, bg='#e09f3e', fg='#540b0e')
    minus1.grid(row=5, column=2, padx=20)
    minus2 = Button(root2, text='-', command=rem2, bg='#e09f3e', fg='#540b0e')
    minus2.grid(row=6, column=2, padx=20)
    minus3 = Button(root2, text='-', command=rem3, bg='#e09f3e', fg='#540b0e')
    minus3.grid(row=7, column=2, padx=20)
    minus4 = Button(root2, text='-', command=rem4, bg='#e09f3e', fg='#540b0e')
    minus4.grid(row=8, column=2, padx=20)
    minus5 = Button(root2, text='-', command=rem5, bg='#e09f3e', fg='#540b0e')
    minus5.grid(row=9, column=2, padx=20)
    minus6 = Button(root2, text='-', command=rem6, bg='#e09f3e', fg='#540b0e')
    minus6.grid(row=10, column=2, padx=20)
    minus7 = Button(root2, text='-', command=rem7, bg='#e09f3e', fg='#540b0e')
    minus7.grid(row=11, column=2, padx=20)
    minus8 = Button(root2, text='-', command=rem8, bg='#e09f3e', fg='#540b0e')
    minus8.grid(row=12, column=2, padx=20)
    minus9 = Button(root2, text='-', command=rem9, bg='#e09f3e', fg='#540b0e')
    minus9.grid(row=13, column=2, padx=20)
    minus10 = Button(root2, text='-', command=rem10, bg='#e09f3e', fg='#540b0e')
    minus10.grid(row=14, column=2, padx=20)
    minus11 = Button(root2, text='-', command=rem11, bg='#e09f3e', fg='#540b0e')
    minus11.grid(row=15, column=2, padx=20)

    cost = Label(root2, text='Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#9e2a2b')
    cost.grid(row=4, column=5, padx=20, pady=10)

    cost1 = Label(root2, text=80, bg='#FFE26F', fg='#540b0e')
    cost1.grid(row=5, column=5, padx=20)
    cost2 = Label(root2, text=120, bg='#FFE26F', fg='#540b0e')
    cost2.grid(row=6, column=5, padx=20)
    cost3 = Label(root2, text=170, bg='#FFE26F', fg='#540b0e')
    cost3.grid(row=7, column=5, padx=20)
    cost4 = Label(root2, text=50, bg='#FFE26F', fg='#540b0e')
    cost4.grid(row=8, column=5, padx=20)
    cost5 = Label(root2, text=70, bg='#FFE26F', fg='#540b0e')
    cost5.grid(row=9, column=5, padx=20)
    cost6 = Label(root2, text=200, bg='#FFE26F', fg='#540b0e')
    cost6.grid(row=10, column=5, padx=20)
    cost7 = Label(root2, text=200, bg='#FFE26F', fg='#540b0e')
    cost7.grid(row=11, column=5, padx=20)
    cost8 = Label(root2, text=250, bg='#FFE26F', fg='#540b0e')
    cost8.grid(row=12, column=5, padx=20)
    cost9 = Label(root2, text=300, bg='#FFE26F', fg='#540b0e')
    cost9.grid(row=13, column=5, padx=20)
    cost10 = Label(root2, text=100, bg='#FFE26F', fg='#540b0e')
    cost10.grid(row=14, column=5, padx=20)
    cost11 = Label(root2, text=100, bg='#FFE26F', fg='#540b0e')
    cost11.grid(row=15, column=5, padx=20)

    def back1():
        global nt1
        global nt2
        global nt3
        global nt4
        global nt5
        global nt6
        global nt7
        global nt8
        global nt9
        global nt10
        global nt11
        nt1 = 0
        nt2 = 0
        nt3 = 0
        nt4 = 0
        nt5 = 0
        nt6 = 0
        nt7 = 0
        nt8 = 0
        nt9 = 0
        nt10 = 0
        nt11 = 0
        root2.destroy()

    order = Button(root2, text='Order Now', width=10, command=order, font='tkdefault 10 bold', bg='#e09f3e',
                   fg='#540b0e')
    order.grid(row=16, column=2, columnspan=2, pady=20)
    back = Button(root2, text='<<', command=back1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    root2.mainloop()


def ur_order():
    global count
    urorder = Toplevel()
    urorder.title('Your Order')
    urorder.geometry('390x360+510+110')
    urorder.configure(background='#FFE26F')

    urorder.wm_attributes('-transparentcolor', 'red')
    row0 = Label(urorder, text='Your Order', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=1, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\ur_order.png")
    bg_label = Label(urorder, image=bg)
    bg_label.place(x=-2, y=-2)

    c.execute("SELECT ITEM_NAME,QTTY,ITEM_PRICE FROM ROOM_SERVICE ORDER BY SNO DESC LIMIT {}".format(count))
    item = Label(urorder, text='Item Name', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    item.grid(row=1, column=0, padx=50, pady=5)
    qtty = Label(urorder, text='Quantity', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    qtty.grid(row=1, column=1, padx=20, pady=5)
    cost = Label(urorder, text='Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    cost.grid(row=1, column=2, padx=30, pady=5)

    back = Button(urorder, text='<<', command=urorder.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    i = 2
    for rec in c:
        for j in range(len(rec)):
            e = Label(urorder, text=rec[j], bg='#FFE26F', fg='#540b0e')
            e.grid(row=i, column=j, padx=10)
        i = i + 1

    count = 0

    urorder.mainloop()


def ur_bookings():
    global uname
    global d2
    global d1

    root4 = Toplevel()
    root4.title('Previous Bookings')
    root4.geometry('560x410+450+100')
    root4.configure(background='#FFE26F')

    root4.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root4, text='Your Bookings', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=1, columnspan=3, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\ur_bookings.png")
    bg_label = Label(root4, image=bg)
    bg_label.place(x=-2, y=-2)

    c.execute("SELECT TYPE,NOR,CHECKIN,CHECKOUT,ROOM_COST FROM ROOM WHERE NAME='{}'".format(uname.get()))

    rtype = Label(root4, text='Room Type', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    rtype.grid(row=1, column=0, padx=50, pady=5)
    nor = Label(root4, text='No. of Rooms', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    nor.grid(row=1, column=1, padx=10, pady=5)
    checkin = Label(root4, text='CheckIn', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    checkin.grid(row=1, column=2, padx=10, pady=5)
    checkout = Label(root4, text='CheckOut', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    checkout.grid(row=1, column=3, padx=10, pady=5)
    room_cost = Label(root4, text='Room Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    room_cost.grid(row=1, column=4, padx=10, pady=5)

    back = Button(root4, text='<<', command=root4.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=25, pady=20, sticky=W)

    i = 2
    for rec in c:
        for j in range(len(rec)):
            e = Label(root4, text=rec[j], bg='#FFE26F', fg='#540b0e')
            e.grid(row=i, column=j)
        i = i + 1

    root4.mainloop()


def homepg():
    home = Toplevel()
    home.title('Home Page')
    home.geometry('340x330+540+180')
    home.configure(background='#FFE26F')

    def log_out():
        global uname
        uname = StringVar()
        home.destroy()
        cust_login()

    home.wm_attributes('-transparentcolor', 'red')
    row0 = Label(home, text='Thamanyas Resort', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=1, pady=20)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\homepg.png")
    bg_label = Label(home, image=bg)
    bg_label.place(x=-2, y=-2)

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\notne\Desktop\hotel managment\images\hotel logo.png"))
    img_label = Label(home, image=img, bg='#FFE26F')
    img_label.grid(row=0, column=0, pady=20, padx=30)

    room_button = Button(home, text='Room Booking', command=room, width=20, bg='#e09f3e', fg='#540b0e')
    room_button.grid(row=1, column=0, columnspan=2, padx=30, pady=10)
    roomservice_button = Button(home, text='Room Service', command=room_service, width=20, bg='#e09f3e', fg='#540b0e')
    roomservice_button.grid(row=2, column=0, columnspan=2, padx=30, pady=10)
    urbookings_button = Button(home, text='Your Bookings', command=ur_bookings, width=20, bg='#e09f3e', fg='#540b0e')
    urbookings_button.grid(row=3, column=0, columnspan=2, padx=30, pady=10)

    logout = Button(home, text='Log Out', command=log_out, bg='#e09f3e', fg='#540b0e')
    logout.grid(row=4, column=1, padx=10, pady=10, sticky=E)

    home.mainloop()


def emphome():
    ehome = Toplevel()
    ehome.title('Home Page')
    ehome.geometry('340x290+540+180')
    ehome.configure(background='#FFE26F')

    def log_out():
        ehome.destroy()
        emp_login()

    ehome.wm_attributes('-transparentcolor', 'red')
    row0 = Label(ehome, text='Thamanyas Resort', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=1, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\emphome.png")
    bg_label = Label(ehome, image=bg)
    bg_label.place(x=-2, y=-2)

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\notne\Desktop\hotel managment\images\hotel logo.png"))
    img_label = Label(ehome, image=img, bg='#FFE26F')
    img_label.grid(row=0, column=0, pady=20, padx=30)

    admn_details = Button(ehome, text='Admin Details', command=admin_details, width=20, bg='#e09f3e', fg='#540b0e')
    admn_details.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
    stat = Button(ehome, text='Statistics', command=food, width=20, bg='#e09f3e', fg='#540b0e')
    stat.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    logout = Button(ehome, text='Log Out', command=log_out, bg='#e09f3e', fg='#540b0e')
    logout.grid(row=3, column=1, padx=20, pady=20, sticky=E)

    ehome.mainloop()


def food():
    root5 = Toplevel()
    root5.title('Statistics')
    root5.geometry('690x590+350+40')
    root5.configure(background='#FFE26F')

    def front1():
        root5.destroy()
        book()

    root5.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root5, text='Most Liked Food', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=0, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\food.png")
    bg_label = Label(root5, image=bg)
    bg_label.place(x=-2, y=-2)

    rec = pd.read_sql("SELECT ITEM_NAME AS 'Item Name',SUM(QTTY) AS 'Quantity' FROM ROOM_SERVICE GROUP BY ITEM_NAME",
                      con)
    rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Best Seller.csv', sep=',')
    df = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Best Seller.csv', sep=',')

    df.plot.barh(x='Item Name', y='Quantity')
    plt.tight_layout()
    plt.savefig(r'C:\Users\notne\Desktop\hotel managment\images\Food Stats.png')

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\notne\Desktop\hotel managment\images\Food Stats.png"))
    img_label = Label(root5, image=img, bg='#FFE26F')
    img_label.grid(row=1, column=0, pady=10, padx=20)

    back = Button(root5, text='<<', command=root5.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    front = Button(root5, text='>>', command=front1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    front.grid(row=1, column=0, padx=9, sticky=E)

    root5.mainloop()


def book():
    root6 = Toplevel()
    root6.title('Statistics')
    root6.geometry('690x590+350+40')
    root6.configure(background='#FFE26F')

    def front1():
        root6.destroy()
        most_room()

    def prev1():
        root6.destroy()
        food()

    root6.wm_attributes('-transparentcolor', 'red')
    row0 = Label(root6, text='Most Bookings', font='tkdefault 14 bold', bg='red')
    row0.grid(row=0, column=0, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\book.png")
    bg_label = Label(root6, image=bg)
    bg_label.place(x=-2, y=-2)

    rec = pd.read_sql(
        "SELECT MONTHNAME(STR_TO_DATE(LEFT(CHECKIN,2), '%m')) AS 'Month Name',COUNT(*) AS 'No. of Months' FROM ROOM GROUP BY LEFT(CHECKIN,2)",
        con)
    rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Most Bookings.csv', sep=',')
    df = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Most Bookings.csv', sep=',')

    df.plot.barh(x='Month Name', y='No. of Months')
    plt.tight_layout()
    plt.savefig(r'C:\Users\notne\Desktop\hotel managment\images\Bookings Stats.png')

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\notne\Desktop\hotel managment\images\Bookings Stats.png"))
    img_label = Label(root6, image=img, bg='#FFE26F')
    img_label.grid(row=1, column=0, pady=10, padx=20)

    back = Button(root6, text='<<', command=root6.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    prev = Button(root6, text='<<', command=prev1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    prev.grid(row=1, column=0, padx=9, sticky=W)
    front = Button(root6, text='>>', command=front1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    front.grid(row=1, column=0, padx=9, sticky=E)

    root6.mainloop()


def most_room():
    root7 = Toplevel()
    root7.title('Statistics')
    root7.geometry('690x590+350+40')
    root7.configure(background='#FFE26F')

    def prev1():
        root7.destroy()
        book()

    root7.wm_attributes('-transparentcolor', 'red')
    title = Label(root7, text='Best Selling Room', font='tkdefault 14 bold', bg='red')
    title.grid(row=0, column=0, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\most_room.png")
    bg_label = Label(root7, image=bg)
    bg_label.place(x=-2, y=-2)

    rec = pd.read_sql("SELECT TYPE AS 'Room',COUNT(TYPE) AS 'No. of Rooms' FROM ROOM GROUP BY TYPE", con)
    rec.to_csv(r'C:\Users\notne\Desktop\hotel managment\Best Selling Room.csv', sep=',')
    df = pd.read_csv(r'C:\Users\notne\Desktop\hotel managment\Best Selling Room.csv', sep=',')

    df.plot.barh(x='Room', y='No. of Rooms')
    plt.tight_layout()
    plt.savefig(r'C:\Users\notne\Desktop\hotel managment\images\Popular Room.png')

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\notne\Desktop\hotel managment\images\Popular Room.png"))
    img_label = Label(root7, image=img, bg='#FFE26F')
    img_label.grid(row=1, column=0, pady=10, padx=20)

    back = Button(root7, text='<<', command=root7.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    prev = Button(root7, text='<<', command=prev1, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    prev.grid(row=1, column=0, padx=9, sticky=W)

    root7.mainloop()


def admin_details():
    root3 = Toplevel()
    root3.title('Admin Details')
    root3.geometry('720x500+420+80')
    root3.configure(background='#FFE26F')

    root3.wm_attributes('-transparentcolor', 'red')
    title = Label(root3, text='Admin Details', font='tkdefault 14 bold', bg='#FFE26F', fg='#9e2a2b')
    title.grid(row=0, column=2, columnspan=2, pady=15)

    bg = PhotoImage(file=r"C:\Users\notne\Desktop\hotel managment\images\admin_details.png")
    bg_label = Label(root3, image=bg)
    bg_label.place(x=-2, y=-2)

    c.execute("UPDATE ADMIN_DETAILS SET SERVICE_COST=0 WHERE SERVICE_COST IS NULL")
    c.execute(
        "DELETE FROM admin_details WHERE SNO NOT IN (SELECT * FROM(SELECT MAX(SNO) FROM admin_details GROUP BY TYPE,CHECKIN,NAME)AS t) AND SERVICE_COST IS NULL")
    c.execute(
        "SELECT TYPE,NAME,CHECKIN,CHECKOUT,SUM(ROOM_COST),SERVICE_COST,SUM(ROOM_COST)+SERVICE_COST AS 'TOTAL' FROM ADMIN_DETAILS GROUP BY TYPE,CHECKIN,NAME")

    type = Label(root3, text='Room Type', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    type.grid(row=1, column=0, padx=50, pady=5)
    name = Label(root3, text='Username', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    name.grid(row=1, column=1, padx=10, pady=5)
    checkin = Label(root3, text='CheckIn', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    checkin.grid(row=1, column=2, padx=10, pady=5)
    checkout = Label(root3, text='CheckOut', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    checkout.grid(row=1, column=3, padx=10, pady=5)
    room_cost = Label(root3, text='Room Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    room_cost.grid(row=1, column=4, padx=10, pady=5)
    service_cost = Label(root3, text='Serivce Cost', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    service_cost.grid(row=1, column=5, padx=10, pady=5)
    total = Label(root3, text='Total', font='tkdefault 10 bold', bg='#FFE26F', fg='#540b0e')
    total.grid(row=1, column=6, padx=10, pady=5)

    back = Button(root3, text='<<', command=root3.destroy, font='tkdefault 10 bold', bg='#e09f3e', fg='#540b0e')
    back.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    i = 2
    for rec in c:
        for j in range(len(rec)):
            e = Label(root3, text=rec[j], bg='#FFE26F', fg='#540b0e')
            e.grid(row=i, column=j)
        i = i + 1

    root3.mainloop()

who()
