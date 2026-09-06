# LIST
'''
a = [1,1,2.0,True,"hi"]
print(a)

a = [10,20,30,40,50,60]
print(a[:])
print(a[:6])
print(a[0:])
print(a[::-1])
print(a[2])
print(a[-1])
print(a[2:5])
a.append(70)
print(a)
a.extend([80,100])
print(a)
a.insert(8,90)
print(a)
a.remove(100)
print(a)
a.pop()
print(a)
a.pop(7)
print(a)

#remove the multiples of 20 in a list
a = [30, 30, 10, 40, 100, 100, 20, 80, 40, 100, 50, 10, 40, 80, 30, 40, 10, 70, 70, 10]
for i in a:
    if i%20==0:
        a.remove(i)
print(a)

a[6]=7
print(a)
#a.clear()
#print(a)
print(a.index(50))
print(a.count(10))
a.sort()
print(a)

#pass by reference
a = [10,20,30]
b = a.copy()
print(a)
print(b)
a.append(40)
print(a)
print(b)

#pass by value
a = [10,20,30]
b = a
print(a)
print(b)
a.append(40)
print(a)
print(b)
b = [x**2 for x in range(5)]
print(b)

data = ["Mounika",9384542020,"Course"]
a = tuple(data)
print(type(a))

#TUPLE

b = (1,2,3,4)
print(b)
print(b[3])
print(b[:])
print(b[0:])
print(b[:4])
print(b[::-1])

a1 = (1,2,3)
a2 = (4,5,6)
a3 = a1 + a2
print(a3)
print(a3 * 2)

data = ("Mounika",9384542020,"Python")
name = data[0]
phone = data[1]
course = data[2]
n , p , c = data
print(n)
print(p)
print(c)
a,b,c  = 10,20,30
a,b = b,a

#SET

s = {1,1,1.01,'hi',True,False,0,23,90}
print(s)
s = {1,5,3,9,7}
s.add(11)
print(s)
s.update([2,4,6])
print(s)
s.pop()
print(s)
s.remove(2)
print(s)
s.discard(3)
print(s)
s.discard(3) # does nothing and raises no error
print(s)
s.remove(2)#remove() raises a KeyError if the element does not exist
print(s)
s.clear()

s1 = {1,2,3,4,5}
s2 = {2,4,6,8,10}
print(s1.union(s2))
print(s1.intersection(s2))
#s1.intersection_update(s2)
#print(s1 , s2)
print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))

a1 = {1,2,3,4,5,6}
a2 = {1,2,3}
a3 = {1,11,2}
print(a2.issubset(a1))
print(a3.issubset(a1))

print(a1.issuperset(a2))
print(a1.issuperset(a3))

b1 = {1,2,3,4}
b2 = {4,5,6,7}
b3 = {5,6,7,8}

print(b1.isdisjoint(b2))
print(b1.isdisjoint(b3))
'''

#Dictionary
'''
syntax : variable = {key1 : value1 , key2 : value2 , key3 : value3}
rule =>
key : data types : int , float , string
     unique keys only allowed
value : duplicates allowed , all data type used
'''

a = {1:"Mounika",2:"Prathika",1:"Shiny"}
print(a)
a = {1:"Mounika",2:"Prathika",3:"Shiny"}
print(a)
print(a[1])
print(a.get(3))
print(a.keys())
print(a.values())
print(a.items())
a.update({4:"Vinodhini"})
print(a)
a.update({3:"Keerthi"})
print(a)
a[1]="Surya"
print(a)
a.pop(3)
print(a)
students = {
    "st1": {"name": "Anu", "age": 25},
    "st2": {"name": "Anil", "age": 23}
}
print(students["st1"]["age"])

for i in a:
    print(i , " : ",a[i])








