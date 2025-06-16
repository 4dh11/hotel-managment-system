import pandas as pd
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='',database='thamanyas_resort')
c=con.cursor()
from tkinter import *
root=Tk()

def cust_signin():
    sign_fname=input('Enter your firstname: ')
    sign_lname=input('Enter your lastname: ')
    sign_age=int(input('Enter your age: '))
    sign_phone=int(input('Enter your phone number: '))
    sign_email=input('Enter your email: ')
    sign_pwd=input('Enter your password: ')
    while True:
        c_pwd=input('Re-Enter the password: ')
        if c_pwd==sign_pwd:
            print('Account has been created')
            break
        if c_pwd!=sign_pwd:
            print('Password entered is wrong')
    c.execute("INSERT INTO CUST_SIGNIN VALUES ('{}','{}',{},{},'{}','{}')".format(sign_fname,sign_lname,sign_age,sign_phone,sign_email,sign_pwd))
    con.commit()
    cust_rec=pd.read_sql("SELECT * FROM CUST_SIGNIN",con)
    cust_rec.to_csv(r'C:\Users\notne\Desktop\School stuff\ip project\Customer SignIn Details.csv',sep=',')

def cust_login():
    cust_rec=pd.read_sql("SELECT * FROM CUST_SIGNIN",con)
    while True:
        cust_email=input('Enter your email: ')
        cust_pwd=input('Enter your password: ')
        if cust_email in cust_rec.values and cust_pwd in cust_rec.values:
            print('Account has been accessed')
            break
        elif cust_email not in cust_rec.values or cust_pwd not in cust_rec.values:
            print('Re-enter your Email')

def emp_login():
    emp_rec=pd.read_csv(r'',sep=',')
    while True:
        emp_email=input('Enter your email: ')
        emp_pwd=input('Enter your password: ')
        if emp_email in emp_rec.values and emp_pwd in emp_rec.values:
            print('Account has been accessed')
            break
        elif emp_email not in emp_rec.values or emp_pwd not in emp_rec.values:
            print('Re-enter your Email(or)Password')

def room():
    room_type=input('Enter the type of room: ')
    nop=int(input('Enter the no. of people: '))
    ac_non=input('Enter whether ac is reqd or not: ')
    c.execute("INSERT INTO ROOM (TYPE,NOP,AC_NONAC) VALUES ('{}',{},'{}')".format(room_type,nop,ac_nonac))
    con.commit()

def booking_details():
    name=input('Enter your name: ')
    phone_no=int(input('Enter your phone no.: '))
    checkin=int(input('Enter the date of checkin: '))
    checkout=int(input('Enter the date of checkout: '))
    c.execute("INSERT INTO BOOKING_DETAILS (NAME,PHONENO,CHECKIN,CHECKOUT) VALUES ('{}',{},{},{})".format(name,phoneno,checkin,checkout))
    con.commit()
    book_rec=pd.read_sql("SELECT * FROM BOOKING_DETAILS",con)
    book_rec.to_csv(r'C:\Users\notne\Desktop\School stuff\ip project\Booking Details.csv',sep=',')
    
def room_service():
    book_rec=pd.read_sql("SELECT * FROM BOOKING DETAILS",con)
    while True:
        room_no=int(input('Enter room no: '))
        name=input('Enter your name: ')
        if room_no in book_rec.values and name in book_rec.values:
            break
        elif room_no not in book_rec.values or name not in book_rec.values:
            print('Re-enter you room no. or name')
    item_name=input('Enter the item name: ')
    qtty=int(input('Enter the quantity: '))
    c.execute("INSERT INTO ROOM_SERVICE (ROOM_NO,ITEM_NAME,QTTY) VALUES ({},'{}',{})".format(room_no,item_name,qtty))
    con.commit()
    serv=pd.read_sql("SELECT * FROM ROOM_SERVICE",con)
    serv.to_csv(r'C:\Users\notne\Desktop\School stuff\ip project\Room Service Details.csv',sep=',')


    
while True:
    print('''
          1. Customer signin
          2. Customer login
          3. Employee login
          4. Room
          5. Room Service
          6. Exit
          ''')
    i=int(input('Enter your choice: '))
    if i==1:
        cust_signin()
    if i==2:
        cust_login()
    if i==3:
        emp_login()
    if i==4:
        room()
    if i==5:
        room_service()
    if i==6:
        break
