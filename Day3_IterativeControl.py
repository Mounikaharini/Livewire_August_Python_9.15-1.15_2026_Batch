#iterative control
#for loop
#1.increment loop
'''
for i in range(1,6,1):
    print(i)

#2 x 1 = 2 to 2 x 10 = 20
for i in range(1,11,1):
    print("2 x",i,"=",i*2)

#2.decrement loop
for i in range(5,0,-1):
    print(i)

#2 x 10 = 20 to 2 x 1 = 2
for i in range(10,0,-1):
    print("2 x",i,"=",i*2)

#3.nested loop
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):
    for j in range(5):
       print("*",end=" ")
    print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()
# * * * * *
#     *
#     *
#     *
#     *

#sum of list
a = [3,8,5,7,4]
s = 0 # 3 -> 11 -> 16 -> 23 -> 27
for i in a:
    s = s + i

    s = 0 + 3 = 3
    s = 3 + 8 = 11
    s = 11 + 5 = 16
    s = 16 + 7 = 23
    s = 23 + 4 = 27

print(s)

#linear search
a = [3,8,5,7,4]
key = 4
found = False
index = 0
foundIndex = 0
for i in a:
    if i==key:
        found = True
        foundIndex = index
    index = index + 1
if found:
    print("Key Present in",foundIndex,"Index")
else:
    print("Key Not Present")

#while loop
#1.increment loop
i = 1
while i<=5:
    print(i)
    i+=1
    
#2.decrement loop
i = 5
while i>=1:
    print(i)
    i-=1

#* * * * *

i = 1
while i<=5:
    print("*",end=" ")
    i+=1
print()

#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *

j = 1
while j<=5:
    i = 1
    while i<=5:
        print("*",end=" ")
        i+=1
    print()
    j+=1

#count the digits
n = 54621318653
c = 0
while n>0:
    n = n//10
    c = c + 1
print(c)

#sum of digits
n = 12345
s = 0
while n>0:
    r = n%10
    s = s + r
    n = n//10
print(s)

#find a given number is an armstrong or not

n = 153
n1 = n
n2 = n
c = 0
while n>0:
    n = n//10
    c = c + 1
    
s = 0
while n1>0:
    r = n1%10
    s = s + (r**c)
    n1 = n1//10
if n2 == s:
    print("yes")
else:
    print("no")

#factors of given number
n = 56
c = 0
#1 2 3 4 6 9 12 18 36
for i in range(1,n+1,1):
#1.for i in range(2,n,1):
#2.for i in range(2,(n//2+1),1)
    if n%i==0:
        print(i)
        c+=1
if c==2:
#1.if c==0
#2.c==0
    print("Prime number")
else:
    print("Not a Prime number")

24 -> 1 2 3 4 6 8 12 24
32 -> 1 2 4 8 16 32
16 -> 1 2 4 8 16
56 -> 1 2 4 7 8 14 28 56 
8 -> 1 2 4 8
'''

#jumping control
#break , continue , pass

for i in range(1,5,1):
    if i==3:
        break
    print(i)

for i in range(1,5,1):
    if i==3:
        continue
    print(i)

for i in range(1,5,1):
    if i==3:
        pass
    print(i)













