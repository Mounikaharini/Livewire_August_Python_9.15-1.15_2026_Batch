def add():
    a = 10
    b = 20
    c = a + b
    print(c)
add()
add()
add()
add()
add()

def add(c,d): #parameter
    print(c+d)
add(2,4) #arguments
add(5,6)

def sub(c,d,e):
    print(c-d-e)
    return "hi"
# a=int(input("Enter value1"))
# b=int(input("Enter value2"))
# sub(a,b,5)
print(sub(5,5,5))

def action1():
    return "BATMAN" #return the data to main
print(action1())

#without return without parameter
def fun1():
    username="mounika@gmail.com"
    password="mouni@123"
    if username=="mounika@gmail.com" and password=="mouni@123":
        print("Login Successful!!!")
    else:
        print("Invalid Credentials!!!")
fun1()
        
#with return without parameter
def fun2():
    username="mounika@gmail.com"
    password="mouni@123"
    if username=="mounika@gmail.com" and password=="mouni@123":
        return "Login Successful!!!"
    else:
        return "Invalid Credentials!!!"
print(fun2())

#without return with parameter
def fun3(username,password):
    if username=="mounika@gmail.com" and password=="mouni@123":
        print("Login Successful!!!")
    else:
        print("Invalid Credentials!!!")
username="mounika@gmail.com"
password="mouni@123"
fun3(username,password)

#with return with parameter
def fun4(username,password):
    if username=="mounika@gmail.com" and password=="mouni@123":
        return "Login Successful!!!"
    else:
        return "Invalid Credentials!!!"
username="mounika@gmail.com"
password="mouni@123"
result = fun4(username,password)
print(result)

#default argument

def result(tamil=0,english=0,maths=0,science=0,social=0):
    print(tamil+english+maths+science+social)
result(90,90,90,90,90)
result(55,35,65,75)

#keyword argument

def result(tamil=0,english=0,maths=0,science=0,social=0):
    print(tamil+english+maths+science+social)
result(tamil=50,english=80,maths=58,social=50)

#variable length argument
#type I => Values only
def sorting(*a):
    # print(type(a))
    a=list(a)
    a.sort()
    print(a)
sorting(2,8,6,3,4,9,5,7,21,3,5,8,7)

#type II => Key and Value
def FoodList(**a):
    for i in a:
        print(i+" : "+a[i])
FoodList(food1="Dosa",food2="Briyani",food3="Fried Rice",food4="Noodles",food5="Chicken Rice")

#recursion function
def hi():
    print("hi")
    hi()
hi()

def login():
    username = input("Enter the Username :")
    password = input("Enter the Password :")
    if username=="mouni" and password=="1234":
        print("Login Successful")
    else:
        print("Invalid Username / Password")
        login()
login()

#Lambda FUnction
add = lambda a,b:a+b
sub = lambda a,b:a+b
print(sub(9,10))
print(add(9,9))

# map function

def cube(n):
    return n*n*n
a=[1,2,3,4,5,6,7,8,9,10]
print(tuple(map(cube,a)))

def cube(n):
    if n%2==0:
        return n*n*n
a=[1,2,3,4,5,6,7,8,9,10]
print(tuple(map(cube,a)))

#Filter function
def filtering(n):
    if n%2==0:
        return n
a=[1,2,3,4,5,6,7,8,9,10]
print(tuple(filter(filtering,a)))
