
print("Start")

try:
    y = {1:1,2:2,3:3}
    print(y[5])
    
    x = int(input("Enter Data : "))
    
    print(a)
    a=10
except NameError as e:
    print("Error :",e)

except ValueError as e:
    print("Error :",e)

except KeyError as e:
    print("Error :",e)

except Exception as e:
    print("Error :",e)

finally:
    print("Code Executed")
    
print("Stop")

#assert

a = 10
assert a!=10,"Error Found"


#raise

x=10
if x==10:
    raise NameError("X Value is 10")















