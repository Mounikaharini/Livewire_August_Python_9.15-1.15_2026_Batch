'''
#doc string
"""hi this is my module"""
def hello():
    """This is a function"""
    print("hello")
"""hi this is not my module"""
hello()
print(hello.__doc__)
print(__doc__)

#iterator
m = [1,2,3,4,5]
t = iter(m)
print(m)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
#print(next(t)) -> error occur

#Generator
def hi(n):
    for i in range(1,n+1):
        yield i
        
for i in hi(5):
    print(i)

#Closure
def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
times3 = make_multiplier(3)
print(times3(10))  # 30

def hi():
    def hello():
        return "hiii"
    return hello
m = hi()
print(m())

#decorator

def hello(function):
    def bye():
        function()
    return bye
    
@hello
def hi():
    print("..........hi")
hi()

#single thread
import time
def hi():
    time.sleep(3)
    print("hi")
hi()
'''
#Multi thread
import time
import threading
def fun1():
    for i in range(1,6):
        time.sleep(2)
        print(f"Thread {i} from fun 1 is Running .....")
def fun2():
    for i in range(1,6):
        time.sleep(1)
        print(f"Thread {i} from fun 2 is Running .....")
thread1 = threading.Thread(target=fun1)
thread2 = threading.Thread(target=fun2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()











