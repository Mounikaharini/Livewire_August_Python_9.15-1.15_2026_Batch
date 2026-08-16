
#sequence control
print("-------- Welcome to our App --------")
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
print("------------------------------------")
print("Your Answer is :",a+b)
print("------------------------------------")

#selection control
#type -1 simple if
a = input("Is it raining ? (yes/no) :")
if a=="yes":
    print("Today class is postponded")

#type -2  if - else
a = input("Is it raining ? (yes/no) :")
if a=="yes" or a=="YES" or a=="Yes":
    print("Today class is postponded")
else:
    print("Come to class")

a = int(input("Enter a number :"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")

#type - 3 nested if 
ch = input("Enter a character : ")
if (ch>='a' and ch<='z'):
    vowel = ['a','e','i','o','u']
    if ch in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

#type - 4 elif

print("""
    Choose The payment Method
-----------------------------------
0.Exit
1.Phonepe
2.Gpay
3.AmazonPay
4.NetBanking
5.Cash on Delivery
------------------------------------
""")
ch = int(input("Enter the Choice (0/1/2/3/4/5) :"))
if ch==0:
    print("Thank You ! Visit Again")
elif ch==1:
    print("Thank you for choosing Phonepe")
elif ch==2:
    print("Thank you for choosing Gpay")
elif ch==3:
    print("Thank you for choosing AmazonPay")
elif ch==4:
    print("Thank you for choosing NetBanking")
elif ch==5:
    print("Thank you for choosing Cash on Delivery")
else:
    print("Invalid Choice !")
print("------------------------------------")


    
