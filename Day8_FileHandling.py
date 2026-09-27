#read a file
'''
file = open("student.txt","r")
print(file.read())
print(file.read(2))
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()
'''
#write a file
#using write mode
'''
mouli = open("mouli.txt","w")
print("File Opened")
mouli.write("File")
mouli.close()
'''
#using append mode
'''
mouli = open("mouli.txt","a")
print("File Opened")
mouli.write("File\n")
mouli.close()
'''
-----------------------------

fruits = {1:["Apple",150],
          2:["Orange",120],
          3:["Mango",60],
          4:["Water-Apple",20]}
for i in fruits:
    print(i,". Fruit Name :",fruits[i][0],"-> Price :",fruits[i][1])
    
ch = int(input("Enter the choice : "))

product_name = fruits[ch][0]
product_price = fruits[ch][1]

quantity = int(input("Enter the Quantity : "))
amount = product_price * quantity

Customer_name = input("Enter Customer Name : ")
import time as d
bill =f"""
      Welcome to Fresh Fruit
***********************************

Date : {d.ctime()}
Name : {Customer_name}
-----------------------------------
Product Name        :{product_name}
Product Price (per) :{product_price}
Total Quantity      :{quantity}
-----------------------------------
Total Amount to Pay :{amount}

***********************************
      Thank You Visiting !!!
"""
print("Bill Created")

file = open("bill.txt","a")
file.write(bill)
file.close()
print("Bill Generated")









