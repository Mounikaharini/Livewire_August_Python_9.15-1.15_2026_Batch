'''
class student:
    def __init__(self):
        pass
    def studentDetails(self):
        print("Add Student Details")
    def studentMarks(self):
        print("Add Student Marks")

s = student()
s.studentDetails()
s.studentMarks()

class calc:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
c = calc()
c.add(10,20)
c.sub(20,36)
c.mul(2,9)
c.div(10,3)

class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
c = calc(10,20)
c.add()
c.sub()
c.mul()
c.div()

#single Inheritance
class instagramLite:
    def features():
        featureList = ['Add to story','Add Post','Add Notes','Reels','Live']
        for i in featureList:
            print(i)
    def appDesign():
        designDetails = ['Low Storage','Low UX','Having More Bugs']
        for i in designDetails:
            print(i)

class instagram(instagramLite):
    def instaFeature():
        featureList = ['Download Reels','Instants Option']
        print("Hi")
    def appDesign():
        designDetails = ['High Storage','Good UX','Having Less Bugs']
        for i in designDetails:
            print(i)

o1 = instagramLite
o1.features()
o1.appDesign()

o2 = instagram
o2.features()
o2.appDesign()
o2.instaFeature()
'''

#Multiple Inheritance

class Watch:
    def watchFeature():
        print("It Shows the Time")
class Mobile:
    def mobileFeature():
        print("We can use the apps")
class SmartWatch(Mobile,Watch):
    def smartWatchFeature():
        print("We can see WC , BP , HeartBeat")

w = Watch
w.watchFeature()

m = Mobile
m.mobileFeature()

s = SmartWatch
s.watchFeature()
s.mobileFeature()
s.smartWatchFeature()










