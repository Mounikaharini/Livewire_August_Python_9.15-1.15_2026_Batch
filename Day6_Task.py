name = input("Enter The Student Name :")
rollNo = int(input("Enter The Roll Number :"))
department = input("Enter The Department Name :")
python = int(input("Enter Python Mark :"))
english = int(input("Enter English Mark :"))
maths = int(input("Enter Maths Mark :"))
total = python + english + maths
avg = total // 3
grade = ""
if avg>=76 and avg<=100:
    grade = "A"
elif avg>=51 and avg<=75:
    grade = "B"
elif avg>=26 and avg<=50:
    grade = "C"
elif avg>=0 and avg<=25:
    grade = "D"
else:
    grade = "Invalid Grade / Mark"
result = "Fail"
if python>=35 and maths>=35 and english>=35:
    result = "Pass"
print("Name         :",name)
print("Roll No      :",rollNo)
print("Department   :",department)
print("--------------------------------")
print("Python Mark  :",python)
print("English Mark :",english)
print("Maths Mark   :",maths)
print("--------------------------------")
print("Total        :",total)
print("Average      :",avg)
print("Grade        :",grade)
print("--------------------------------")
print("Result       :",result)
print("--------------------------------")
