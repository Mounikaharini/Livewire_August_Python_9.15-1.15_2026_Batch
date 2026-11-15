import pymysql as sql
db = sql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prathika")
c = db.cursor()

def tableCreate(db, c):
    
    query = "create table upi(Name varchar(25),upiid varchar(50),amount int,date varchar(100))"
    try:
        c.execute(query)
        db.commit()
        print("Table Is Created")
    except Exception as e:
        print(e)
    db.close()
#tableCreate(db, c)

def accountCreation(db,c):
    import datetime as d
    date = d.datetime.now()
    query = "Insert into upi values('%s','%s','%d','%s')"%("Mounika","mounika@okaxis",1000,date)
    try:
        c.execute(query)
        db.commit()
        print("Data Is Inserted")
    except Exception as e:
        db.rollback()
        print(e)
    db.close()
#accountCreation(db,c)

def amountTransaction(db,c):
    upiid = input("Enter the upi id : ")
    selectquery = "select * from upi"
    c.execute(selectquery)
    a = c.fetchall()
    flag = False
    for i in a:
        if upiid in i:
            flag = True
    if flag:
        print("For Credit Amount : Enter 1 , For Debit Amount : Enter 2")
        option = int(input("Enter The Option : "))
        amountEntered = int(input("Enter The Amount : "))
        if option == 1:
            updatequery = "update upi set amount = amount + ('%d') where upiid = ('%s')"%(amountEntered,upiid)
        elif option == 2:
            updatequery = "update upi set amount = amount - ('%d') where upiid = ('%s')"%(amountEntered,upiid)
        else:
            print("Invalid Option")
    else:
        print("Invalid UPI Id")
    try:
        c.execute(updatequery)
        db.commit()
        print("Data Updated")
    except Exception as e:
        db.rollback()
    db.close()
    
amountTransaction(db,c)

#-----------------------------------------------------------------------------------------------------------------------------------------

import pymysql as sql
db = sql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prathika")
c = db.cursor()

def create(db,c):
    #print("Server Running .... ")
    create = "create table student(studentid int, studentname varchar(25), studentmailid varchar(50), studentpassword varchar(12))"
    c.execute(create)
    #print("Table student is created")
    db.close()

def insert(db,c):
    studentid = int(input("Enter the Student Id : "))
    studentname = input("Enter the Student Name : ")
    studentmailid = input("Enter the Student Mail id : ")
    studentpassword = input("Enter the Password : ")
    #insert = """insert into student values(1,"Mounika","mounika@gmail.com","mouni@1234")"""
    insert = "insert into student values('%d','%s','%s','%s')"%(studentid,studentname,studentmailid,studentpassword)
    try:
        c.execute(insert)
        db.commit()
        print("Data Inserted")
    except Exception as e:
        db.rollback()
        print(e)
    db.close()

def delete(db,c):
    studentiddata = int(input("Enter the id to delete (for eg : 1/2/3) : "))
    delete = "delete from student where studentid='%d'"%(studentiddata)
    try:
        c.execute(delete)
        db.commit()
        print("Data Deleted")
    except Exception as e:
        db.rollback()
    db.close()

def read(db,c):
    query = "select * from student"
    c.execute(query)
    a = c.fetchall()
    for i in a:
        print(i)
read(db,c)

def update(db,c):
    query = "update student set studentmailid=('%s') where studentid=1"%("m@gmail.com")
    try:
        c.execute(query)
        db.commit()
        print("Data Updated")
    except Exception as e:
        db.rollback()
    db.close()
update(db,c)




        




    
