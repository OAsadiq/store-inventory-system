import tkinter as tk
from tkinter  import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime
import time
import sys
import tempfile
import os
import random

#=========================================================================Window======================================================================================================================================================================================================
win = Tk()
win.title("Shopleft")
width = 800
height = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
win.geometry("%dx%d+%d+%d" % (width, height, x, y))
win.resizable(0,0)
win.configure(bg="white")
#======================================================================All Variables=========================================================================================================================================================================================================
FULLNAME=StringVar()
USERNAME=StringVar()
TEL=StringVar()
EMAIL=StringVar()
ADDRESS=StringVar()
PASSWORD=StringVar()
ROLE=StringVar()
PRODUCTNAME=StringVar()
PRODUCTCATEGORY=StringVar()
PRICE=StringVar()
SEARCH=StringVar()
PID=StringVar()
PNAME=StringVar()
PCATEGORY=StringVar()
PPRICE=StringVar()
DATE=StringVar()
QUANTITY=StringVar()
TOTAL=StringVar()
TOTAL.set("  ")
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))

global l
l=[]
#======================================================================Time=========================================================================================================================================================================================================
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    lbl_1.config(text=timeVar)
    lbl_1.after(200,get_time)
#======================================================================Photos=========================================================================================================================================================================================================
photo=PhotoImage(file = "login.png")
photo=photo.subsample(3,5)
photo1=PhotoImage(file = "login.png")
photo1=photo.subsample(8,8)
#======================================================================Back And Exit=========================================================================================================================================================================================================
def mainexit():
    result = messagebox.askquestion('',"Are you sure you want to exit")
    if result == 'yes':
        win.destroy()
        exit()
def login1_back():
    if 'login1' in globals():
        login1.destroy()
        win.deiconify()
def login2_back():
    if 'login2' in globals():
        login2.destroy()
        win.deiconify()
def login3_back():
    if 'login3' in globals():
        login3.destroy()
        win.deiconify()
def Add_product_back():
    if 'Add_product' in globals():
        Add_product.destroy()
def staff_reg_back():
    if 'staff_reg' in globals():
        staff_reg.destroy()
def staff_reg1_back():
    if 'staff_reg1' in globals():
        staff_reg1.destroy()
def staff_reg2_back():
    if 'staff_reg2' in globals():
        staff_reg2.destroy()
def staff_reg3_back():
    if 'staff_reg3' in globals():
        staff_reg3.destroy()
def Admin_win_back():
    if 'Admin_win' in globals():
        Admin_win.destroy()
def product_admin_back():
    if 'product_admin' in globals():
        product_admin.destroy()
def staff_admin_back():
    if 'staff_admin' in globals():
        staff_admin.destroy()
def sales_admin_back():
    if 'sales_admin' in globals():
        sales_admin.destroy()
def store_keeper_back():
    if 'store_keeper_win' in globals():
        store_keeper_win.destroy()
#======================================================================Database=================================================================================================================================================================================================================================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("Shopleft.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Staff_Admin` (STAFF_ID1 INTEGER PRIMARY KEY, STAFF_FULLNAME TEXT, STAFF_USERNAME TEXT, STAFF_TEL TEXT, STAFF_EMAIL TEXT, STAFF_ADDRESS TEXT, STAFF_PASSWORD TEXT, STAFF_ROLE TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `Staff_Sale_Rep` (STAFF_ID2 INTEGER PRIMARY KEY, STAFF_FULLNAME TEXT, STAFF_USERNAME TEXT, STAFF_TEL TEXT, STAFF_EMAIL TEXT, STAFF_ADDRESS TEXT, STAFF_PASSWORD TEXT, STAFF_ROLE TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `Staff_Store_Keeper` (STAFF_ID3 INTEGER PRIMARY KEY, STAFF_FULLNAME TEXT, STAFF_USERNAME TEXT, STAFF_TEL TEXT, STAFF_EMAIL TEXT, STAFF_ADDRESS TEXT, STAFF_PASSWORD TEXT, STAFF_ROLE TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `Products` (PRODUCT_ID INTEGER PRIMARY KEY, PRODUCT_NAME TEXT, PRODUCT_CATEGORY TEXT, PRODUCT_PRICE TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `Sales` (Sales_ID INTEGER PRIMARY KEY, SPRODUCT_ID TEXT, SPRODUCT_NAME TEXT, SPRODUCT_CATEGORY TEXT, SPRODUCT_PRICE TEXT, QUANTITY TEXT, DATE TEXT, TOTAL TEXT)")
#REGISTER FUNC
def Register1():
    win.withdraw()
    Database()
    if FULLNAME.get() =="" or USERNAME.get() =="" or TEL.get() =="" or EMAIL.get() =="" or ADDRESS.get() =="" or PASSWORD.get() =="" or ROLE.get() =="":
        messagebox.showinfo("error"," Please Fill All Fields ")
    else:
        cursor.execute("SELECT * FROM `Staff_Admin` WHERE `STAFF_USERNAME` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("error","Username Already Taken")
        else:
            cursor.execute("INSERT INTO `Staff_Admin` (STAFF_FULLNAME, STAFF_USERNAME, STAFF_TEL, STAFF_EMAIL, STAFF_ADDRESS, STAFF_PASSWORD, STAFF_ROLE)VALUES(?, ?, ?, ?, ?, ?, ?)", (str(FULLNAME.get()), str(USERNAME.get()), str(TEL.get()), str(EMAIL.get()), str(ADDRESS.get()), str(PASSWORD.get()), str(ROLE.get())))
            conn.commit()
            staff_reg1_result.config(text="Successful Registration", fg="green")
def Register2():
    win.withdraw()
    Database()
    if FULLNAME.get() =="" or USERNAME.get() =="" or TEL.get() =="" or EMAIL.get() =="" or ADDRESS.get() =="" or PASSWORD.get() =="" or ROLE.get() =="":
        messagebox.showinfo("error", " Please Fill All Fields ")
    else:
        cursor.execute("SELECT * FROM `Staff_Sale_Rep` WHERE `STAFF_USERNAME` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("error", "Username Already Taken")
        else:
            cursor.execute("INSERT INTO `Staff_Sale_Rep` (STAFF_FULLNAME, STAFF_USERNAME, STAFF_TEL, STAFF_EMAIL, STAFF_ADDRESS, STAFF_PASSWORD, STAFF_ROLE)VALUES(?, ?, ?, ?, ?, ?, ?)", (str(FULLNAME.get()), str(USERNAME.get()), str(TEL.get()), str(EMAIL.get()), str(ADDRESS.get()), str(PASSWORD.get()), str(ROLE.get())))
            conn.commit()
            staff_reg2_result.config(text="Successful Registration", fg="green")
def Register3():
    win.withdraw()
    Database()
    if FULLNAME.get() =="" or USERNAME.get() =="" or TEL.get() =="" or EMAIL.get() =="" or ADDRESS.get() =="" or PASSWORD.get() =="" or ROLE.get() =="":
        messagebox.showinfo("error", " Please Fill All Fields ")
    else:
        cursor.execute("SELECT * FROM `Staff_Store_keeper` WHERE `STAFF_USERNAME` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("error", "Username Already Taken")
        else:
            cursor.execute("INSERT INTO `Staff_Store_Keeper` (STAFF_FULLNAME, STAFF_USERNAME, STAFF_TEL, STAFF_EMAIL, STAFF_ADDRESS, STAFF_PASSWORD, STAFF_ROLE)VALUES(?, ?, ?, ?, ?, ?, ?)", (str(FULLNAME.get()), str(USERNAME.get()), str(TEL.get()), str(EMAIL.get()), str(ADDRESS.get()), str(PASSWORD.get()), str(ROLE.get())))
            conn.commit()
            staff_reg3_result.config(text="Successful Registration", fg="green")
#LOGINS FUNC
def Login_Admin():
    win.withdraw()
    Database()
    if USERNAME.get() =="" or PASSWORD.get() =="":
        messagebox.showinfo("", "Please Fill The Required Field", icon="warning")
    else:
        cursor.execute("SELECT * FROM `Staff_Admin` WHERE `STAFF_USERNAME` = ? and `STAFF_PASSWORD` = ?", (USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            admin_logresult.config(text="Successfully Logged In", fg="green")
            Admin_win()
        else:
            admin_logresult.config(text="Invalid Username or Password", fg="red")
def Login_Sales():
    win.withdraw()
    Database()
    if USERNAME.get() =="" or PASSWORD.get() =="":
        messagebox.showinfo("", "Please Fill The Required Field", icon="warning")
    else:
        cursor.execute("SELECT * FROM `Staff_Sale_Rep` WHERE `STAFF_USERNAME` = ? and `STAFF_PASSWORD` = ?", (USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            salerep_logresult.config(text="Successfully Logged In", fg="green")
            Sales()
        else:
            salerep_logresult.config(text="Invalid Username or Password", fg="red")
def Login_Store():
    win.withdraw()
    Database()
    if USERNAME.get() =="" or PASSWORD.get() =="":
        messagebox.showinfo("", "Please Fill The Required Field", icon="warning")
    else:
        cursor.execute("SELECT * FROM `Staff_Store_keeper` WHERE `STAFF_USERNAME` = ? and `STAFF_PASSWORD` = ?", (USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            storekeeper_logresult.config(text="Successfully Logged In", fg="green")
            store_keeper_win()
        else:
            storekeeper_logresult.config(text="Invalid Username or Password", fg="red")
#SHOW SALES FUNC
def show():
    cursor.execute("SELECT * FROM `Sales` ")
    fetch = cursor.fetchall()
    for data in fetch:
        tree_view2.insert("", tk.END, values=data)
    cursor.close()
    conn.commit()
    conn.close()
#ADD PRODUCT FUNC
def Add_productdb():
    win.withdraw()
    Database()
    if PRODUCTNAME.get() =="" or PRODUCTCATEGORY.get() =="" or PRICE.get() =="":
        result = messagebox.showinfo("error", " Please Fill All Fields ")
    else:
        cursor.execute("SELECT * FROM `Products` WHERE `PRODUCT_NAME` = ?", (PRODUCTNAME.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("error", "Product Name Already Taken")
        else:
            cursor.execute("INSERT INTO `Products` (PRODUCT_NAME, PRODUCT_CATEGORY, PRODUCT_PRICE)VALUES(?, ?, ?)", (str(PRODUCTNAME.get()), str(PRODUCTCATEGORY.get()), str(PRICE.get())))
            conn.commit()
            conn.close()
            Add_product_result.config(text="Successfully Added", fg="green")
#ADD SALES To DATABASE
def Add_to():
    Database()
    if PID.get() =="" or PNAME.get() =="" or PCATEGORY.get() =="" or PPRICE.get() =="" or QUANTITY.get() =="" or DATE.get() =="" or TOTAL.get() =="":
        messagebox.showinfo("error", "Please Fill All Fields", icon="warning")
    else:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Sales` (SPRODUCT_ID, SPRODUCT_NAME, SPRODUCT_CATEGORY, SPRODUCT_PRICE, QUANTITY, DATE, TOTAL)VALUES(?, ?, ?, ?, ?, ?, ?)", (str(PID.get()), str(PNAME.get()), str(PCATEGORY.get()), str(PPRICE.get()), str(QUANTITY.get()), str(DATE.get()), str(TOTAL.get())))
        conn.commit()
        conn.close()
#======================================================================Views, Search, And Others=================================================================================================================================================================================================================================================
def total_price():
    no1 = int(PPRICE.get())
    no2 = int(QUANTITY.get())
    no3 = no1*no2
    TOTAL.set( str(no3) + " NGN")
def display_product(event):
    PID.get()
    PNAME.get()
    PCATEGORY.get()
    PPRICE.get()
    identify = treeview_2.identify_row(event.y)
    item = treeview_2.item(treeview_2.focus())
    PID.set(item['values'][0])
    PNAME.set(item['values'][1])
    PCATEGORY.set(item['values'][2])
    PPRICE.set(item['values'][3])
def Update(row_1):
    treeview_2.delete(*treeview_2.get_children())
    for n in row_1:
     treeview_2.insert('', 'end', values=n)
def Searching():
    global row_1
    Database()
    SRH = SEARCH.get()
    if SEARCH.get() =="":
        messagebox.showinfo("", "No Product Found")
    else:
        cursor.execute("SELECT * FROM `Products` WHERE `PRODUCT_NAME` LIKE '%"+SRH+"%' ")
        if cursor.fetchone() is None:
            row_1 = cursor.fetchall()
            treeview_2.delete(*treeview_2.get_children())
            messagebox.showinfo("error", "No Product Found")
        else:
            cursor.execute("SELECT * FROM `Products` WHERE `PRODUCT_NAME` LIKE '%"+SRH+"%' ")
            row_1 = cursor.fetchall()
            Update(row_1)
def view_product():
    tree_view.delete(*tree_view.get_children())
    conn = sqlite3.connect("Shopleft.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    row_2 = cursor.fetchall()
    for row in row_2:
        tree_view.insert("", tk.END, values=row)
    conn.close()
def view_staff1():
    tree_view1.delete(*tree_view1.get_children())
    conn = sqlite3.connect("Shopleft.db")
    cursor = conn.cursor()
    cursor.execute("SELECT STAFF_ID1, STAFF_FULLNAME, STAFF_USERNAME, STAFF_ROLE FROM `Staff_Admin` ")
    row_2 = cursor.fetchall()
    for row in row_2:
        tree_view1.insert("", tk.END, values=row)
    conn.close()
def view_staff2():
    tree_view1.delete(*tree_view1.get_children())
    conn = sqlite3.connect("Shopleft.db")
    cursor = conn.cursor()
    cursor.execute("SELECT STAFF_ID2, STAFF_FULLNAME, STAFF_USERNAME, STAFF_ROLE FROM `Staff_Sale_Rep` ")
    row_2 = cursor.fetchall()
    for row in row_2:
        tree_view1.insert("", tk.END, values=row)
    conn.close()
def view_staff3():
    tree_view1.delete(*tree_view1.get_children())
    conn = sqlite3.connect("Shopleft.db")
    cursor = conn.cursor()
    cursor.execute("SELECT STAFF_ID3, STAFF_FULLNAME, STAFF_USERNAME, STAFF_ROLE FROM `Staff_Store_Keeper` ")
    row_2 = cursor.fetchall()
    for row in row_2:
        tree_view1.insert("", tk.END, values=row)
    conn.close()
def delete_data1():
    if not tree_view1.selection():
        result = messagebox.showwarning("", "Please Select Something First", icon="warning")
    else:
        result = messagebox.askquestion("", "Are You Want To Delete From This Record?", icon="warning")
        if result == 'yes':
            curItem = tree_view1.focus()
            contents = (tree_view1.item(curItem))
            selecteditem = contents['values']
            tree_view1.delete(curItem)
            conn = sqlite3.connect("Shopleft.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Staff_Admin` WHERE `STAFF_ID1` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def delete_data2():
    if not tree_view1.selection():
        result = messagebox.showwarning("", "Please Select Something First", icon="warning")
    else:
        result = messagebox.askquestion("", "Are You Want To Delete From This Record?", icon="warning")
        if result == 'yes':
            curItem = tree_view1.focus()
            contents = (tree_view1.item(curItem))
            selecteditem = contents['values']
            tree_view1.delete(curItem)
            conn = sqlite3.connect("Shopleft.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Staff_Sale_Rep` WHERE `STAFF_ID2` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def delete_data3():
    if not tree_view1.selection():
        result = messagebox.showwarning("", "Please Select Something First", icon="warning")
    else:
        result = messagebox.askquestion("", "Are You Want To Delete From This Record?", icon="warning")
        if result == 'yes':
            curItem = tree_view1.focus()
            contents = (tree_view1.item(curItem))
            selecteditem = contents['values']
            tree_view1.delete(curItem)
            conn = sqlite3.connect("Shopleft.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Staff_Store_Keeper` WHERE `STAFF_ID3` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def delete_data4():
    if not tree_view.selection():
        result = messagebox.showwarning("", "Please Select Something First", icon="warning")
    else:
        result = messagebox.askquestion("", "Are You Want To Delete From This Record?", icon="warning")
        if result == 'yes':
            curItem = tree_view.focus()
            contents = (tree_view.item(curItem))
            selecteditem = contents['values']
            tree_view.delete(curItem)
            conn = sqlite3.connect("Shopleft.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Products` WHERE `PRODUCT_ID` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
#======================================================================Sales Window====================================================================================================================================================================================================================================================

def clear():
    PID.set('')
    PNAME.set('')
    PCATEGORY.set('')
    PPRICE.set(0)
    QUANTITY.set(0)
    TOTAL.set('')

def exit():
    op=messagebox.askyesno('Exit','Do you really want to exit')
    if op>0:
        win.destroy()

def Sales():

    def welcome():
        textarea.delete(1.0,END)
        textarea.insert(END,"\t Welcome Shopleft")
        textarea.insert(END,f'\n\nBill Number:\t\t{bill_no.get()}')
        textarea.insert(END,f'\nCustomer Number:\t\t{bill_no.get()}')
        textarea.insert(END,f"\n\n=========================================")
        textarea.insert(END,'\nProduct\t\tQTY\t\tPrice')
        textarea.insert(END,f"\n=========================================\n")
        textarea.configure(font=("Times New Roman",10,"bold"))
    
    def additm():
        n=int(PPRICE.get())
        m=int(QUANTITY.get())*n
        l.append(m)
        if PNAME.get()=='':
            messagebox.showerror('Error','Please Enter the product')
        else:
            textarea.insert((10.0+float(len(l)-1)),f"{PNAME.get()}\t\t{QUANTITY.get()}\t\t{ m}\n")

    def gbill():
        tex=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END,tex)
        textarea.insert(END,f"\n=========================================")
        textarea.insert(END,f"\nTotal Paybill Amount :\t{sum(l)}")
        textarea.insert(END,f"\n\n=========================================")
        printbill()

    def printbill():
        q = textarea.get("1.0", "end-1c")
        op=messagebox.askyesno('Print bill','Do you want to print the bill')
        if op>0:
            temp_file = tempfile.mktemp('.txt')
            open (temp_file, 'w').write(q)
            os.startfile(temp_file,"print")

    global Sales, treeview_1, treeview_2
    Sales =Toplevel()
    Sales.title("Staff Main Window")
    width=1200
    height=600
    screen_width = Sales.winfo_screenwidth()
    screen_height = Sales.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Sales.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Sales.resizable(0,0)
    Sales.configure(bg="white")

    Sales_title = Label(Sales, text="                              SHOPLEFT                                   ", bg="red", width="100", height="1", font=("TImes New Roman",17,"bold"))
    Sales_title.pack()
    Sales_title1 = Label(Sales, text="                            BILLING SYSTEM                                   ", bg="red", width="100", height="1", font=("TImes New Roman",17,"bold"))
    Sales_title1.pack()

    wrapper1 = LabelFrame(Sales, text="CUSTOMER CART", bg="grey")
    wrapper1.pack(fill="both", side=TOP, padx=20, pady=10)

    wrapper2 = LabelFrame(Sales, text="SEARCH", bg="grey")
    wrapper2.pack(fill="both", side=LEFT, padx=20, pady=10)

    wrapper3 = LabelFrame(Sales, text="BILLER", bg="grey")
    wrapper3.pack(fill="both", side=LEFT, padx=20, pady=10)

    wrapper4 = LabelFrame(Sales, text="", bg="grey")
    wrapper4.pack(fill="both", side=LEFT, padx=20, pady=10)

    space = Label(wrapper1, text="", height="1", bg="grey").grid(row=0, column=0)

    cname= Label(wrapper1, text="Customer Name", bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=1, column=0, padx=8, pady=3)
    cname_entry= Entry(wrapper1, textvariable=FULLNAME, width="30", border="5").grid(row=1, column=1, padx=8)

    cphone= Label(wrapper1, text="Phone NO.", bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=1, column=2, padx=8, pady=3)
    cphone_entry= Entry(wrapper1, textvariable=TEL, width="30", border="5").grid(row=1, column=3, padx=8)

    space = Label(wrapper1, text="", width="50", bg="grey").grid(row=1, column=4)
    Button(wrapper1, text="EXIT", width=17, bg="red", fg="black",border="5", font=("Times New Roman",10,"bold"), command=exit).grid(row=1, column=5, padx=6, pady=3)

    space1 = Label(wrapper1, text="", height="2", bg="grey").grid(row=2, column=0)

    #WRAPPER2
    Entry(wrapper2, width="34", border="5", textvariable=SEARCH).grid(row=0, column=0, padx=8)
    Button(wrapper2, text="SEARCH", width="25", bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=Searching).grid(row=1, column=0, padx=8, pady=6)
    treeview_2 = ttk.Treeview(wrapper2, columns=(1,2), show='headings', height="5")
    treeview_2.heading(1, text="Product ID")
    treeview_2.heading(2, text="Product Name")
    treeview_2.column('1',width="200")
    treeview_2.column('2',width="200")
    treeview_2.grid(padx=20, pady=10)
    treeview_2.bind('<Double 1>', display_product)
    #WRAPPER3
    slbl_1= Label(wrapper3, text="Product ID",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=0, column=0, padx=5, pady=3)
    slbl_1_entry= Entry(wrapper3, textvariable=PID, width="20", border="5").grid(row=0, column=1, padx=5, pady=3)

    lbl_2= Label(wrapper3, text="Product Name",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=1, column=0, padx=5, pady=3)
    lbl_2_entry= Entry(wrapper3, textvariable=PNAME, width="20", border="5").grid(row=1, column=1, padx=5, pady=3)

    lbl_3= Label(wrapper3, text="Product Category",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=2, column=0, padx=5, pady=3)
    lbl_3_entry= Entry(wrapper3, textvariable=PCATEGORY, width="20", border="5").grid(row=2, column=1, padx=5, pady=3)

    lbl_4= Label(wrapper3, text="Price(#)",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=3, column=0, padx=5, pady=3)
    lbl_4_entry= Entry(wrapper3, textvariable=PPRICE, width="20", border="5").grid(row=3, column=1, padx=5, pady=3)

    lbl_5= Label(wrapper3, text="Quantity",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=4, column=0, padx=5, pady=3)
    lbl_5_entry= Entry(wrapper3, textvariable=QUANTITY, width="20", border="5").grid(row=4, column=1, padx=5, pady=3)

    lbl_6= Label(wrapper3, text="Date",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=5, column=0, padx=5, pady=3)
    cal = DateEntry(wrapper3, textvariable=DATE, width="20", border="5")
    cal.grid(row=5, column=1, padx=5, pady=3)

    lbl_7= Label(wrapper3, text="Total(#)",bg="grey", fg="white", font=('Time New Roman',10,'bold')).grid(row=6, column=0, padx=5, pady=3)
    lbl_7_entry= Entry(wrapper3, textvariable=TOTAL, width="20", border="5").grid(row=6, column=1, padx=5, pady=3)

    Button(wrapper3, text="CALCULATE", width=15, bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=total_price).grid(row=7,column=0, padx=6, pady=3)
    Button(wrapper3, text="ADD TO CART", width=15, bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=additm).grid(row=7,column=1, padx=6, pady=3)
    Button(wrapper3, text="GENERATE RECIEPT", bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=lambda:[Add_to(), gbill()]).grid(row=8, column=0, padx=6, pady=3)
    Button(wrapper3, text="CLEAR", width=17, bg="red", fg="black",border="5", font=("Times New Roman",10,"bold"), command=clear).grid(row=8, column=1, padx=6, pady=3)
    #WRAPPER4
    bill_title=Label(wrapper4,text='RECEIPT',font=("Times New Roman",10,"bold")).pack(fill=X)
    scroll_y=Scrollbar(wrapper4, orient=VERTICAL)
    textarea=Text(wrapper4,yscrollcommand=scroll_y)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=textarea.yview)
    textarea.pack()

    welcome()

#======================================================================Login====================================================================================================================================================================================================================================================
def login1():
    global login1, admin_logresult
    login1= Toplevel(win)
    login1.title("Admin Login")
    width=800
    height=500
    screen_width = login1.winfo_screenwidth()
    screen_height = login1.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    login1.resizable(0,0)
    login1.configure(bg="white")

    admin_lbl = Label(login1, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    admin_lbl.place(x=0, y=0)

    admin_pic = Label(login1, image=photo,compound=TOP, text="Login ", bg="white", width="250", height="110", font=("Times New Roman", 17)) 
    admin_pic.place(x=250, y=100)
    
    username_label = Label(login1, image=photo1,compound=LEFT,text="USERNAME",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    username_label.place(x=100, y=250)

    username_entry = Entry(login1, font=("arial", 20), textvariable=USERNAME, border="5")
    username_entry.place(x=260, y=240)

    password_label = Label(login1, image=photo1,compound=LEFT,text="PASSWORD",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    password_label.place(x=100, y=335)

    password_entry = Entry(login1, font=("arial", 20), textvariable=PASSWORD, border="5", show="*")
    password_entry.place(x=260, y=325)

    admin_btn = Button(login1, text="SIGN IN", bg="yellow",fg="black", height="1", width="10", border="5", font=("Times New Roman",17,"bold"), command=Login_Admin)
    admin_btn.place(x=300, y=420)

    admin_back_btn = Button(login1, text="BACK", bg="RED",fg="black", height="2", width="10", border="5", font=("Times New Roman",10,"bold"), command=login1_back)
    admin_back_btn.place(x=700, y=100)

    admin_logresult = Label(login1, text="", bg="white", height="2")
    admin_logresult.place(x=300, y=375)

def login2():
    global login2, salerep_logresult
    login2= Toplevel(win)
    login2.title("Sale Rep Login")
    width=800
    height=500
    screen_width = login2.winfo_screenwidth()
    screen_height = login2.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    login2.resizable(0,0)
    login2.configure(bg="white")

    salerep_lbl = Label(login2, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New ROman",17,"bold"))
    salerep_lbl.place(x=0, y=0)

    salerep_pic = Label(login2, image=photo,compound=TOP, text="Login ", bg="white", width="250", height="110", font=("Times New Roman", 17)) 
    salerep_pic.place(x=250, y=100)
    
    username_label = Label(login2, image=photo1,compound=LEFT,text="USERNAME",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    username_label.place(x=100, y=250)

    username_entry = Entry(login2, font=("arial", 20), textvariable=USERNAME, border="5")
    username_entry.place(x=260, y=240)

    password_label = Label(login2, image=photo1,compound=LEFT,text="PASSWORD",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    password_label.place(x=100, y=335)

    password_entry = Entry(login2, font=("arial", 20), textvariable=PASSWORD, border="5", show="*")
    password_entry.place(x=260, y=325)

    salerep_btn = Button(login2, text="SIGN IN", bg="yellow",fg="black", height="1", width="10", border="5", font=("Times New Roman",17,"bold"), command=Login_Sales)
    salerep_btn.place(x=300, y=420)

    salerep_back_btn = Button(login2, text="BACK", bg="RED",fg="black", height="2", width="10", border="5", font=("Times New Roman",10,"bold"), command=login2_back)
    salerep_back_btn.place(x=700, y=100)

    salerep_logresult = Label(login2, text="", bg="white", height="2")
    salerep_logresult.place(x=300, y=375)

def login3():
    global login3, storekeeper_logresult
    login3= Toplevel(win)
    login3.title("Store Keeper Login")
    width=800
    height=500
    screen_width = login3.winfo_screenwidth()
    screen_height = login3.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    login3.resizable(0,0)
    login3.configure(bg="white")

    storekeeper_lbl = Label(login3, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New ROman",17,"bold"))
    storekeeper_lbl.place(x=0, y=0)

    storekeeper_pic = Label(login3, image=photo,compound=TOP, text="Login ", bg="white", width="250", height="110", font=("Times New Roman", 17)) 
    storekeeper_pic.place(x=250, y=100)
    
    username_label = Label(login3, image=photo1,compound=LEFT,text="USERNAME",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    username_label.place(x=100, y=250)

    username_entry = Entry(login3, font=("arial", 20), textvariable=USERNAME, border="5")
    username_entry.place(x=260, y=240)

    password_label = Label(login3, image=photo1,compound=LEFT,text="PASSWORD",bg="white", height="2", border="5", font=("Time New Roman",12,"bold"))
    password_label.place(x=100, y=335)

    password_entry = Entry(login3, font=("arial", 20), textvariable=PASSWORD, border="5", show="*")
    password_entry.place(x=260, y=325)

    storekeeper_btn = Button(login3, text="SIGN IN", bg="yellow",fg="black", height="1", width="10", border="5", font=("Times New Roman",17,"bold"), command=Login_Store)
    storekeeper_btn.place(x=300, y=420)

    storekeeper_back_btn = Button(login3, text="BACK", bg="RED",fg="black", height="2", width="10", border="5", font=("Times New Roman",10,"bold"), command=login3_back)
    storekeeper_back_btn.place(x=700, y=100)

    storekeeper_logresult = Label(login3, text="", bg="white", height="2")
    storekeeper_logresult.place(x=300, y=375)
#======================================================================Add Product======================================================================================================================================================================================================
def Add_product():
    global Add_product, Add_product_result
    Add_product =Toplevel()
    Add_product.title("Staff Main Window")
    width=800
    height=500
    screen_width = Add_product.winfo_screenwidth()
    screen_height = Add_product.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Add_product.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Add_product.resizable(0,0)
    Add_product.configure(bg="white")

    Add_product_title = Label(Add_product, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    Add_product_title.place(x=0, y=0)

    Add_product_head = Label(Add_product, text="ADD NEW PRODUCT", height="1", font=('Times New Roman',17,'bold'))
    Add_product_head.place(x=250, y=80)

    Add_product_btn1 = Button(Add_product, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=Add_product_back)
    Add_product_btn1.place(x=700, y=50)

    productname_lbl = Label(Add_product, text="PRODUCT NAME",bg="white", height="1", font=("Time New Roman",12, "bold"))
    productname_lbl.place(x=50, y=150)

    productname_ety = Entry(Add_product, font=(10), textvariable=PRODUCTNAME, width="25", border="5")
    productname_ety.place(x=200, y=150)

    productcategory_lbl = Label(Add_product, text="CATEGORY",bg="white", height="1", font=("Time New Roman",12, "bold"))
    productcategory_lbl.place(x=50, y=250)

    list1=['Clothes', 'Food', 'Groceries', 'Tolietries', 'Appliances', 'Stationary', 'Household Materials', 'Cosmetics', 'Others'];
    droplist=OptionMenu(Add_product,PRODUCTCATEGORY, *list1)
    droplist.config(width="20")
    PRODUCTCATEGORY.set('Select Category')
    droplist.place(x=200, y=250)

    price_lbl = Label(Add_product, text="PRICE(#)",bg="white", height="1", font=("Time New Roman", 12, "bold"))
    price_lbl.place(x=50, y=350)

    price_ety = Entry(Add_product, font=(10), textvariable=PRICE, width="25", border="5")
    price_ety.place(x=200, y=350)

    Add_product_btn2 = Button(Add_product, text="ADD",bg="yellow", width="10", height="1", border="5", font=("Time New Roman",12,"bold"), command=Add_productdb)
    Add_product_btn2.place(x=150, y=450)

    Add_product_result = Label(Add_product, text="", height="2", bg="white")
    Add_product_result.place(x=300, y=450)

#======================================================================Staff Registration======================================================================================================================================================================================================
def staff_reg():
    global staff_reg
    staff_reg =Toplevel()
    staff_reg.title("Staff Main Window")
    width=800
    height=500
    screen_width = staff_reg.winfo_screenwidth()
    screen_height = staff_reg.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    staff_reg.geometry("%dx%d+%d+%d" % (width, height, x, y))
    staff_reg.resizable(0,0)
    staff_reg.configure(bg="white")

    staff_reg_title = Label(staff_reg, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    staff_reg_title.place(x=0, y=0)

    staff_reg_head = Label(staff_reg, text="REGISTER NEW AS", height="1", font=('Times New Roman',17,'bold'))
    staff_reg_head.place(x=250, y=80)

    staff_reg_btn1 = Button(staff_reg, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=staff_reg_back)
    staff_reg_btn1.place(x=700, y=50)

    staff_reg_btn2 = Button(staff_reg, text="ADMIN", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',12,'bold'), command=staff_reg1)
    staff_reg_btn2.place(x=200, y=160)
    
    staff_reg_btn3 = Button(staff_reg, text="SALE REP", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',12,'bold'), command=staff_reg2)
    staff_reg_btn3.place(x=200, y=260)
    
    staff_reg_btn4 = Button(staff_reg, text="STORE KEEPER", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',12,'bold'), command=staff_reg3)
    staff_reg_btn4.place(x=200, y=360)

def staff_reg1():
    global staff_reg1, staff_reg1_result
    staff_reg1 =Toplevel()
    staff_reg1.title("Admin Staff")
    width=800
    height=500
    screen_width = staff_reg1.winfo_screenwidth()
    screen_height = staff_reg1.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    staff_reg1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    staff_reg1.resizable(0,0)
    staff_reg1.configure(bg="white")

    staff_reg1_title = Label(staff_reg1, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    staff_reg1_title.place(x=0, y=0)

    staff_reg1_head = Label(staff_reg1, text="REGISTER NEW ADMIN", height="1", font=('Times New Roman',17,'bold'))
    staff_reg1_head.place(x=250, y=40)

    staff_reg1_btn = Button(staff_reg1, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=staff_reg1_back)
    staff_reg1_btn.place(x=700, y=40)

    fullname1_lbl = Label(staff_reg1, text="FULLNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    fullname1_lbl.place(x=50, y=100)

    fullname1_ety = Entry(staff_reg1, font=(10), textvariable=FULLNAME, width="25", border="5")
    fullname1_ety.place(x=150, y=100)

    username1_lbl = Label(staff_reg1, text="USERNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    username1_lbl.place(x=50, y=150)

    username1_ety = Entry(staff_reg1, font=(10), textvariable=USERNAME, width="25", border="5")
    username1_ety.place(x=150, y=150)

    contact1_lbl = Label(staff_reg1, text="TEL. PHONE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    contact1_lbl.place(x=50, y=200)

    contact1_ety = Entry(staff_reg1, font=(10), textvariable=TEL, width="25", border="5")
    contact1_ety.place(x=150, y=200)

    email1_lbl = Label(staff_reg1, text="EMAIL",bg="white", height="1", font=("Time New Roman",12,"bold"))
    email1_lbl.place(x=50, y=250)

    email1_ety = Entry(staff_reg1, font=(10), textvariable=EMAIL, width="25", border="5")
    email1_ety.place(x=150, y=250)

    address1_lbl = Label(staff_reg1, text="ADDRESS",bg="white", height="1", font=("Time New Roman",12,"bold"))
    address1_lbl.place(x=50, y=300)

    address1_ety = Entry(staff_reg1, font=(10), textvariable=ADDRESS, width="25", border="5")
    address1_ety.place(x=150, y=300)

    password1_lbl = Label(staff_reg1, text="PASSWORD",bg="white", height="1", font=("Time New Roman",12,"bold"))
    password1_lbl.place(x=50, y=350)

    password1_ety = Entry(staff_reg1, font=(10), textvariable=PASSWORD, width="25", border="5")
    password1_ety.place(x=150, y=350)

    role1_lbl = Label(staff_reg1, text="ROLE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    role1_lbl.place(x=50, y=400)

    list1=['Admin', 'Manager'];
    droplist=OptionMenu(staff_reg1,ROLE, *list1)
    droplist.config(width="20")
    ROLE.set('Select Role')
    droplist.place(x=150, y=400)

    staff_reg1_btn = Button(staff_reg1, text="REGISTER",bg="yellow", width="10", height="1", border="5", font=("Time New Roman",12,"bold"), command=Register1)
    staff_reg1_btn.place(x=100, y=450)

    staff_reg1_result = Label(staff_reg1, text="", height="2")
    staff_reg1_result.place(x=250, y=450)

def staff_reg2():
    global staff_reg2, staff_reg2_result
    staff_reg2 =Toplevel()
    staff_reg2.title("Sales Rep Staff")
    width=800
    height=500
    screen_width = staff_reg2.winfo_screenwidth()
    screen_height = staff_reg2.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    staff_reg2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    staff_reg2.resizable(0,0)
    staff_reg2.configure(bg="white")

    staff_reg2_title = Label(staff_reg2, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    staff_reg2_title.place(x=0, y=0)

    staff_reg2_head = Label(staff_reg2, text="REGISTER NEW SALE REP", height="1", font=('Times New Roman',17,'bold'))
    staff_reg2_head.place(x=250, y=40)

    staff_reg2_btn = Button(staff_reg2, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=staff_reg2_back)
    staff_reg2_btn.place(x=700, y=40)

    fullname2_lbl = Label(staff_reg2, text="FULLNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    fullname2_lbl.place(x=50, y=100)

    fullname2_ety = Entry(staff_reg2, font=(10), textvariable=FULLNAME, width="25", border="5")
    fullname2_ety.place(x=150, y=100)

    username2_lbl = Label(staff_reg2, text="USERNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    username2_lbl.place(x=50, y=150)

    username2_ety = Entry(staff_reg2, font=(10), textvariable=USERNAME, width="25", border="5")
    username2_ety.place(x=150, y=150)

    contact2_lbl = Label(staff_reg2, text="TEL. PHONE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    contact2_lbl.place(x=50, y=200)

    contact2_ety = Entry(staff_reg2, font=(10), textvariable=TEL, width="25", border="5")
    contact2_ety.place(x=150, y=200)

    email2_lbl = Label(staff_reg2, text="EMAIL",bg="white", height="1", font=("Time New Roman",12,"bold"))
    email2_lbl.place(x=50, y=250)

    email2_ety = Entry(staff_reg2, font=(10), textvariable=EMAIL, width="25", border="5")
    email2_ety.place(x=150, y=250)

    address2_lbl = Label(staff_reg2, text="ADDRESS",bg="white", height="1", font=("Time New Roman",12,"bold"))
    address2_lbl.place(x=50, y=300)

    address2_ety = Entry(staff_reg2, font=(10), textvariable=ADDRESS, width="25", border="5")
    address2_ety.place(x=150, y=300)

    password2_lbl = Label(staff_reg2, text="PASSWORD",bg="white", height="1", font=("Time New Roman",12,"bold"))
    password2_lbl.place(x=50, y=350)

    password2_ety = Entry(staff_reg2, font=(10), textvariable=PASSWORD, width="25", border="5")
    password2_ety.place(x=150, y=350)

    role2_lbl = Label(staff_reg2, text="ROLE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    role2_lbl.place(x=50, y=400)

    list1=['Sales Rep'];
    droplist=OptionMenu(staff_reg2,ROLE, *list1)
    droplist.config(width="20")
    ROLE.set('Select Role')
    droplist.place(x=150, y=400)

    staff_reg2_btn = Button(staff_reg2, text="REGISTER",bg="yellow", width="10", height="1", border="5", font=("Time New Roman",12,"bold"), command=Register2)
    staff_reg2_btn.place(x=100, y=450)

    staff_reg2_result = Label(staff_reg2, text="", height="2")
    staff_reg2_result.place(x=250, y=450)

def staff_reg3():
    global staff_reg3, staff_reg3_result
    staff_reg3 =Toplevel()
    staff_reg3.title("Store Keeper Staff")
    width=800
    height=500
    screen_width = staff_reg3.winfo_screenwidth()
    screen_height = staff_reg3.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    staff_reg3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    staff_reg3.resizable(0,0)
    staff_reg3.configure(bg="white")

    staff_reg3_title = Label(staff_reg3, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    staff_reg3_title.place(x=0, y=0)

    staff_reg3_head = Label(staff_reg3, text="REGISTER NEW STORE KEEPER", height="1", font=('Times New Roman',17,'bold'))
    staff_reg3_head.place(x=250, y=40)

    staff_reg3_btn = Button(staff_reg3, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=staff_reg3_back)
    staff_reg3_btn.place(x=700, y=40)

    fullname3_lbl = Label(staff_reg3, text="FULLNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    fullname3_lbl.place(x=50, y=100)

    fullname3_ety = Entry(staff_reg3, font=(10), textvariable=FULLNAME, width="25", border="5")
    fullname3_ety.place(x=150, y=100)

    username3_lbl = Label(staff_reg3, text="USERNAME",bg="white", height="1", font=("Time New Roman",12,"bold"))
    username3_lbl.place(x=50, y=150)

    username3_ety = Entry(staff_reg3, font=(10), textvariable=USERNAME, width="25", border="5")
    username3_ety.place(x=150, y=150)

    contact3_lbl = Label(staff_reg3, text="TEL. PHONE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    contact3_lbl.place(x=50, y=200)

    contact3_ety = Entry(staff_reg3, font=(10), textvariable=TEL, width="25", border="5")
    contact3_ety.place(x=150, y=200)

    email3_lbl = Label(staff_reg3, text="EMAIL",bg="white", height="1", font=("Time New Roman",12,"bold"))
    email3_lbl.place(x=50, y=250)

    email3_ety = Entry(staff_reg3, font=(10), textvariable=EMAIL, width="25", border="5")
    email3_ety.place(x=150, y=250)

    address3_lbl = Label(staff_reg3, text="ADDRESS",bg="white", height="1", font=("Time New Roman",12,"bold"))
    address3_lbl.place(x=50, y=300)

    address3_ety = Entry(staff_reg3, font=(10), textvariable=ADDRESS, width="25", border="5")
    address3_ety.place(x=150, y=300)

    password3_lbl = Label(staff_reg3, text="PASSWORD",bg="white", height="1", font=("Time New Roman",12,"bold"))
    password3_lbl.place(x=50, y=350)

    password3_ety = Entry(staff_reg3, font=(10), textvariable=PASSWORD, width="25", border="5")
    password3_ety.place(x=150, y=350)

    role3_lbl = Label(staff_reg3, text="ROLE",bg="white", height="1", font=("Time New Roman",12,"bold"))
    role3_lbl.place(x=50, y=400)

    list1=['Store Keeper'];
    droplist=OptionMenu(staff_reg3,ROLE, *list1)
    droplist.config(width="20")
    ROLE.set('Select Role')
    droplist.place(x=150, y=400)

    staff_reg3_btn = Button(staff_reg3, text="REGISTER",bg="yellow", width="10", height="1", border="5", font=("Time New Roman",12,"bold"), command=Register3)
    staff_reg3_btn.place(x=100, y=450)

    staff_reg3_result = Label(staff_reg3, text="", height="2")
    staff_reg3_result.place(x=250, y=450)
#======================================================================Store Keeper Window======================================================================================================================================================================================================
def store_keeper_win():
    global store_keeper_win
    store_keeper_win=Toplevel()
    store_keeper_win.title("Store Keeper Main Window")
    width=800
    height=500
    screen_width = store_keeper_win.winfo_screenwidth()
    screen_height = store_keeper_win.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    store_keeper_win.geometry("%dx%d+%d+%d" % (width, height, x, y))
    store_keeper_win.resizable(0,0)
    store_keeper_win.configure(bg="white")
    
    store_keeper_win_title = Label(store_keeper_win, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    store_keeper_win_title.place(x=0, y=0)

    store_keeper_win_btn1 = Button(store_keeper_win, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=store_keeper_back)
    store_keeper_win_btn1.place(x=700, y=50)

    store_keeper_win_btn2 = Button(store_keeper_win, text="PRODUCTS", bg="yellow", width="40", height="3", border="5", font=('Time New Roman',12,'bold'), command=product_admin)
    store_keeper_win_btn2.place(x=200, y=160)
    
    store_keeper_win_btn3 = Button(store_keeper_win, text="SALES", bg="yellow", width="40", height="3", border="5", font=('Time New Roman',12,'bold'), command=sales_admin)
    store_keeper_win_btn3.place(x=200, y=260)
#======================================================================Admin Window======================================================================================================================================================================================================
def Admin_win():
    global Admin_win
    Admin_win=Toplevel()
    Admin_win.title("Admin Main Window")
    width=800
    height=500
    screen_width = Admin_win.winfo_screenwidth()
    screen_height = Admin_win.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Admin_win.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Admin_win.resizable(0,0)
    Admin_win.configure(bg="white")
    
    Admin_win_title = Label(Admin_win, text="SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    Admin_win_title.place(x=0, y=0)

    Admin_win_btn1 = Button(Admin_win, text=" BACK ", bg="red", width="10", height="2", border="5", font=("Times New Roman",10,'bold'), command=Admin_win_back)
    Admin_win_btn1.place(x=700, y=50)

    Admin_win_btn2 = Button(Admin_win, text="PRODUCTS", bg="yellow", width="40", height="3", border="5", font=('Time New Roman',12,'bold'), command=product_admin)
    Admin_win_btn2.place(x=200, y=160)
    
    Admin_win_btn3 = Button(Admin_win, text="STAFF", bg="yellow", width="40", height="3", border="5", font=('Time New Roman',12,'bold'), command=staff_admin)
    Admin_win_btn3.place(x=200, y=260)
    
    Admin_win_btn4 = Button(Admin_win, text="SALES", bg="yellow", width="40", height="3", border="5", font=('Time New Roman',12,'bold'), command=sales_admin)
    Admin_win_btn4.place(x=200, y=360)

def product_admin():
    global product_admin, tree_view
    product_admin=Toplevel()
    product_admin.title("Admin Product Management")
    width=800
    height=500
    screen_width = product_admin.winfo_screenwidth()
    screen_height = product_admin.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    product_admin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    product_admin.resizable(0,0)
    product_admin.configure(bg="white")

    product_admin_title = Label(product_admin, text="                              SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New ROman",17,"bold"))
    product_admin_title.pack()

    Mid = Frame(product_admin, width=700, bg="white")
    Mid.pack(side=TOP)

    MidLeft = Frame(Mid, width=700, bg="white")
    MidLeft.pack(side=LEFT, pady=10)

    MidLeftPadding = Frame(Mid, width=400, bg="white")
    MidLeftPadding.pack(side=LEFT)

    MidRight = Frame(Mid, width=100, bg="white")
    MidRight.pack(side=RIGHT, pady=10)
    
    wrapper1 = LabelFrame(product_admin, text="PRODUCTS", bg="grey")
    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

    wrapper2 = LabelFrame(product_admin, text="MODIFICATION", bg="grey")
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

#WRAPPER1
    tree_view = ttk.Treeview(wrapper1, columns=(1,2,3,4), show='headings', height="10")
    tree_view.heading(1, text="Product ID")
    tree_view.heading(2, text="Product Name")
    tree_view.heading(3, text="Product Category")
    tree_view.heading(4, text="Product Price(#)")
    tree_view.column(1, width="150")
    tree_view.column(2, width="150")
    tree_view.column(3, width="150")
    tree_view.column(4, width="150")
    tree_view.pack()
    
    Button(wrapper1, text="VIEW ALL PRODUCT", bg="yellow", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=view_product).pack()

#WRAPPER2
    Button(wrapper2, text="ADD NEW PRODUCT", bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=Add_product).grid(row=1,column=1, padx=6, pady=3)
    Button(wrapper2, text="DELETE", bg="red", fg="black",border="5", font=('Time New Roman',10,'bold'), command=delete_data4).grid(row=1,column=3, padx=6, pady=3)
    Button(wrapper2, text="BACK", bg="red", fg="black", width="8", height="1", border="5", font=("Times New Roman",10,"bold"), command=product_admin_back).grid(row=1, column=5, padx=6, pady=3)

def staff_admin():
    global staff_admin, tree_view1
    staff_admin=Toplevel()
    staff_admin.title("Admin Staff Management")
    width=800
    height=500
    screen_width = staff_admin.winfo_screenwidth()
    screen_height = staff_admin.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    staff_admin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    staff_admin.resizable(0,0)
    staff_admin.configure(bg="white")

    staff_admin_title = Label(staff_admin, text="                              SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New ROman",17,"bold"))
    staff_admin_title.pack()

    Mid = Frame(staff_admin, width=700, bg="white")
    Mid.pack(side=TOP)

    MidLeft = Frame(Mid, width=700, bg="white")
    MidLeft.pack(side=LEFT, pady=10)

    MidLeftPadding = Frame(Mid, width=400, bg="white")
    MidLeftPadding.pack(side=LEFT)

    MidRight = Frame(Mid, width=100, bg="white")
    MidRight.pack(side=RIGHT, pady=10)
    
    wrapper1 = LabelFrame(staff_admin, text="STAFFS", bg="grey")
    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

    wrapper2 = LabelFrame(staff_admin, text="MODIFICATION", bg="grey")
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

#WRAPPER1
    tree_view1 = ttk.Treeview(wrapper1, columns=(1,2,3,4), show='headings', height="10")
    tree_view1.heading(1, text="Staff ID")
    tree_view1.heading(2, text="Staff Name")
    tree_view1.heading(3, text="Staff Username")
    tree_view1.heading(4, text="Staff Role")
    tree_view1.column(1, width="150")
    tree_view1.column(2, width="150")
    tree_view1.column(3, width="150")
    tree_view1.column(4, width="150")
    tree_view1.pack()
    
    Button(wrapper1, text="VIEW ADMINS", bg="yellow", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=view_staff1).pack(side=tk.LEFT, padx=6)
    Button(wrapper1, text="VIEW SALE REPS", bg="yellow", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=view_staff2).pack(side=tk.LEFT, padx=6)
    Button(wrapper1, text="VIEW STORE KEEPERS", bg="yellow", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=view_staff3).pack(side=tk.LEFT, padx=6)

#WRAPPER2
    Button(wrapper2, text="ADD NEW STAFF", bg="yellow", fg="black",border="5", font=('Time New Roman',10,'bold'), command=staff_reg).grid(row=1,column=1, padx=6, pady=3)
    Button(wrapper2, text="DELETE ADMINS", bg="red", fg="black",border="5", font=('Time New Roman',10,'bold'), command=delete_data1).grid(row=1,column=3, padx=6, pady=3)
    Button(wrapper2, text="DELETE SALES REPS", bg="red", fg="black",border="5", font=('Time New Roman',10,'bold'), command=delete_data2).grid(row=1,column=5, padx=6, pady=3)
    Button(wrapper2, text="DELETE STORE KEEPERS", bg="red", fg="black",border="5", font=('Time New Roman',10,'bold'), command=delete_data3).grid(row=1,column=7, padx=6, pady=3)
    Button(wrapper2, text="BACK", bg="red", fg="black", width="8", height="1", border="5", font=("Times New Roman",10,"bold"), command=staff_admin_back).grid(row=1, column=9, padx=6, pady=3)

def sales_admin():
    global sales_admin, tree_view2
    sales_admin=Toplevel()
    sales_admin.title("Admin Sales Management")
    width=850
    height=500
    screen_width = sales_admin.winfo_screenwidth()
    screen_height = sales_admin.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    sales_admin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    sales_admin.resizable(0,0)
    sales_admin.configure(bg="grey")

    sales_admin_title = Label(sales_admin, text="                              SHOPLEFT                                   ", bg="red", width="70", height="1", font=("TImes New Roman",17,"bold"))
    sales_admin_title.pack()
    sales_admin_title = Label(sales_admin, text=" ", bg="grey", width="70", height="2")
    sales_admin_title.pack() 

    sales_frame = Frame(sales_admin)
    sales_frame.pack()

    scrollbarx = Scrollbar(sales_frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(sales_frame, orient=VERTICAL)

    tree_view2 = ttk.Treeview(sales_frame, columns=(1,2,3,4,5,6,7,8), show='headings', height="17", selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree_view2.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree_view2.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree_view2.heading(1, text="S/N")
    tree_view2.heading(2, text="Product ID")
    tree_view2.heading(3, text="Product Name")
    tree_view2.heading(4, text="Product Category")
    tree_view2.heading(5, text="Price(#)")
    tree_view2.heading(6, text="Quantity")
    tree_view2.heading(7, text="Date")
    tree_view2.heading(8, text="Total(#)")
    
    tree_view2.column('1',width="70")
    tree_view2.column('2',width="100")
    tree_view2.column('3',width="100")
    tree_view2.column('4',width="130")
    tree_view2.column('5',width="80")
    tree_view2.column('6',width="100")
    tree_view2.column('7',width="80")
    tree_view2.column('8',width="100")
    tree_view2.pack()

    Button(sales_admin, text="VIEW ALL SALES", bg="yellow", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=show).pack(side=tk.LEFT, padx=6)
    Button(sales_admin, text="BACK", bg="RED", fg="black", height="1", border="5", font=('Time New Roman',10,'bold'), command=sales_admin_back).pack(side=tk.LEFT, padx=6)
#======================================================================Front page======================================================================================================================================================================================================
global lbl_1, lbl_2   
lbl_title = Label(win, text="   SHOPLEFT                                   ", bg="red", width="65", height="1", font=('Times New Roman', 17,'bold'))
lbl_title.place(x=0, y=0)
lbl_head = Label(win, text="SIGN IN AS", height="1", font=('Times New Roman',17,'bold'))
lbl_head.place(x=265, y=80)
btn_signin_1 = Button(win, text="ADMIN/MANAGER", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',10,'bold'), command=login1)
btn_signin_1.place(x=200, y=160)
btn_signin_2 = Button(win, text="SALE REP", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',10,'bold'), command=login2)
btn_signin_2.place(x=200, y=220)
btn_signin_3 = Button(win, text="STORE KEPPER", bg="yellow", width="30", height="2", border="5", font=('Time New Roman',10,'bold'), command=login3)
btn_signin_3.place(x=200, y=280)
btn_exit = Button(win, text="EXIT", bg="red", height="2", width="10", border="5", font=('Times New Roman',10,'bold'), command=mainexit)
btn_exit.place(x=690, y=50)
lbl_1 = Label(win, text="", bg="yellow", width="10", font=('caliibri',10,'bold'))
lbl_1.place(x=690, y=100)
x = datetime.datetime.now()
format_date = f"{x:%d- %m -%Y}"
lbl_2 = Label(win, text=format_date, bg="yellow", width="10", font=('caliibri',10,'bold'))
lbl_2.place(x=690, y=125)

get_time()
win.mainloop()

