#function overloading / compile time polymorphism

class calc:
    def add(a=0,b=0,c=0):
        print(a+b+c)
    def add1(*a):
        s=0
        for i in a:
            s=s+i
        print(s)
c = calc
c.add(1,5)
c.add1(1,2,3,4,5,6,7,8,9)

#function overiding / run time polymorphism
#credit card ->
#Axis card -> 5%,
#HDFC card -> 2.5%,
#SBI Card  -> 8%,
#ICICI card -> 4%
class creditCard:
    def userDetails(self,name,amt):
        print("Customer Name :",name)
        print("Amount for Purchasing : ",amt)
    def finalAmount(self,amt):
        print("Card Fee : 0")
        print("Amount To Pay : ",amt)
class AXISCard(creditCard):
    def finalAmount(self,amt):
        print("Card Fee : ",(amt//100*5))
        print("Amount To Pay : ",amt+(amt//100*5))
class HDFCCard(creditCard):
    def finalAmount(self,amt):
        print("Card Fee : ",(amt//100*2.5))
        print("Amount To Pay : ",amt+(amt//100*2.5))
class SBICard(creditCard):
    def finalAmount(self,amt):
        print("Card Fee : ",(amt//100*8))
        print("Amount To Pay : ",amt+(amt//100*8))
class ICICICard(creditCard):
    def finalAmount(self,amt):
        print("Card Fee : ",(amt//100*4))
        print("Amount To Pay : ",amt+(amt//100*4))    
name = input("Enter the Name : ")
amt = int(input("Enter the Amount : "))
print("""Card Payment Availability
-----------------------------
1.Axis card -> 5%
2.HDFC card -> 2.5%
3.SBI Card  -> 8%
4.ICICI card -> 4%
5.No Card -> 0 %
""")
ch = int(input("Enter the choice (1/2/3/4/5) : "))

if ch==1:
    obj = AXISCard()
    obj.userDetails(name,amt)
    obj.finalAmount(amt)
elif ch==2:
    obj = HDFCCard()
    obj.userDetails(name,amt)
    obj.finalAmount(amt)
elif ch==3:
    obj = SBICard()
    obj.userDetails(name,amt)
    obj.finalAmount(amt)
elif ch==4:
    obj = ICICICard()
    obj.userDetails(name,amt)
    obj.finalAmount(amt)
else:
    obj = creditCard()
    obj.userDetails(name,amt)
    obj.finalAmount(amt)

#Abstraction
from abc import ABC , abstractmethod
class Validation(ABC):
    @abstractmethod
    def emailValidation(self,email):
        pass
    @abstractmethod
    def phoneNumberValidation(self,ph):
        pass
class Validator1(Validation):
    def emailValidation(self,email):
        print(email.endswith("@gmail.com"))
    def phoneNumberValidation(self,ph):
        print(ph.startswith("+91"))
        
v = Validator1()
v.emailValidation("mounika@gmail.com")
v.phoneNumberValidation("+919326547801")

#Encapsulation

class emailValidation:
    def __init__(self,mailId,password):
        self.mailId = mailId
        self.__password = password
    def getMailId(self):
        print("Your Mail Id : ",self.mailId)
    def getPassword(self):
        print("Your Password : ",self.__password)
        
e = emailValidation("m@gmail.com","1258mou")
e.getMailId()
e.getPassword()

#constructor chaining
class ParentClass:
    def __init__(self):
        print(f"Parent constructor")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print(f"Child constructor")
child_obj = ChildClass()








