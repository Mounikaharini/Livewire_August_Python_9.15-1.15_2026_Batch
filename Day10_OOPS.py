#Python is a interpreted language or not ? 
#Difference between and , or operator where it use?
#For all situation we can use for loop or while loop?
#What is meant by Selection control why , where it is used ? and give its pros
#When we have to use a user defined - function?
#Is a module can be directly executed in another file without imporing it?
#Difference Between List and Tuple.
#What are the modes in File handling?
#Explain the use case of exception handling.
#Pillars of oops , explain its each advantages.

'''
#Hierarchical inheritance

class message:
    def messageFeature():
        print("Text msg is to be send for saved contact or unknown contact")

class whatsapp(message):
    def whatsappFeature():
        print("We can also send audio , video , files - upto 2GB , make status , customized profile , payment through upi")

class instagram(message):
    def instagramFeature():
        print("We can also send audio , reels , post , Make instants")

class telegram(message):
    def telegramFeature():
        print("Transmit large size files through block chain")

m = message
m.messageFeature()

w = whatsapp
w.messageFeature()
w.whatsappFeature()

i = instagram
i.messageFeature()
i.instagramFeature()

t = telegram
t.messageFeature()
t.telegramFeature()

#multilevel inheritance
class telephone:
    def telephoneFeature():
        print("Contact a person through phone number")

class buttonPhone(telephone):
    def buttonPhoneFeature():
        print("Easy to carry and transport , Make everyones daily use")

class smartPhone(buttonPhone):
    def smartPhoneFeature():
        print("Easy Navigation , Customized App Usage")
        
t = telephone
t.telephoneFeature()

b = buttonPhone
b.telephoneFeature()
b.buttonPhoneFeature()

s = smartPhone
s.telephoneFeature()
s.buttonPhoneFeature()
s.smartPhoneFeature()
'''

#Hybrid Inheritance
class A:
    def A():
        pass
class B(A):
    def B():
        pass
class C(A):
    def C():
        pass
class D(B,C):
    def D():
        pass



