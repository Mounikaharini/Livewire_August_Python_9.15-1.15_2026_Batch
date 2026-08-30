'''
a = 'mounika'
print(a)
a = "+919384542020"
print(a)

mail="livewiremounika@gmail.com"

a = "hello world"
print(a[0:5])
print(a[3:9])
print(a[10])
print(a[-1])
print(a[0:11])
print(a[::-1])
print(a[:])
print(a[0:])
print(a[:11])

b = "hello WORLD"
print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.title())
print(b.swapcase())

c = "hii"
print(c.center(10))
print(c.ljust(5))
print(c.rjust(5))

d="1"
print(d.zfill(5))

e="       hello   hi     "
print(e.strip())
print(e.lstrip())
print(e.rstrip())

f="A string is a sequence of characters enclosed in quotes"
print(f.split())
print(f.split('i'))

g=f.split()
print(''.join(g))
print(' '.join(g))
print(f.rsplit(' ',2))

h = "hi hello hi"
print(h.partition(' '))

a = "python program"
print(a.find('o'))
print(a.rfind('o'))
print(a.find('z'))
print(a.index('o'))
#print(a.index('z'))
print(a.replace('o','-'))
f="A string is in quotes"
print(f.count('e'))

n = input("Enter the number plate Number : ")
print(n.startswith("TN30"))

n = input("Enter the Mail ID : ")
print(n.endswith("@gmail.com"))

print("mounika".isalpha())
print("39408520".isdigit())
print("Id001".isalnum())
print(" ".isspace())
print("MOUNIKa".isupper())
print("MOUNIKa".islower())
print("Mounika Harini".istitle())

name = "Mounika"
course = "Python"
#f-string
print("I'm",name,",Currently Learning",course)
print(f"I'm {name}, Currently Learning {course}")
duration = 3
print(f"The Duration is {duration + 1} months")

#format()
print("I'm {}, Currently Learning {}".format(name,course))
print("I'm {1}, Currently Learning {0}".format(course,name))
print("I'm {n}, Currently Learning {c}".format(c=course,n=name))

#% method

%s -> string
%d -> decimal(integer values)
%f -> float(float values)

Object = "red-balls"
Count = 2
Ratio = 0.5
a = "The probability of picking %d %s is %f"%(Count,Object,Ratio)
print(a)
'''
# count the characters
lower = 0
upper = 0
symbols = 0
numbers = 0
space = 0
vowelCount = 0
ConsonantCount = 0
a = "Xk# 8mP$ 9vL !2q Z"

for i in a:
    ch = i
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        if ch in vowel:
            vowelCount+=1
        else:
            ConsonantCount+=1
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    elif i.isdigit():
        numbers+=1
    elif i.isspace():
        space+=1
    else:
        symbols+=1

print(f"""
The Word = {a}
--------------------------------
Lower Characters   : {lower}
Upper Characters   : {upper}
Symbol Characters  : {symbols}
Numeric Characters : {numbers}
Space Characters   : {space}
Vowel Characters   : {vowelCount}
Consonants         : {ConsonantCount}
--------------------------------
Total Characters   : {len(a)}
""")

#write the sum of the digits in a string
# Input -> ab\62kd76/h6
# Output -> 27
a = "ab/62kd76/h6"
s = 0
for i in a:
    if i.isdigit():
        s = s + int(i)
print(s)

#write the count of unique letters
#programming
#8

a = "programming"
x = set({})
for i in a:
    x.add(i)
print(len(x))









