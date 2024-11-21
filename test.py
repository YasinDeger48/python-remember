#print hello world

print("Hello World!")

#comments in python

#this is command line

#docstrings
docstring = """
This is multiline doc string
"""
print(docstring)

#variables

x = 2
y = "test"
z = False

a = "Python"
b = "is"
c = "Awesome"

print(a, b, c)

a1 = "Python "
b1 = "is "
c1 = "Awesome"

print(a1+b1+c1)

#verifying type of object
sampleFloat = 1.25

print(type(a1)) # <class 'str'>
print(type(z)) #<class 'bool'>
print(type(x)) #<class 'int'>
print(type(sampleFloat)) #<class 'float'>

#Casting
x = int(1)
y = int(2.5)
z = int("5")

print(x,y,z) # 1 2 5

x = float(1)
y = float(2.5)
z = float("5")

print(x,y,z) # 1.0 2.5 5.0

x = str(1)
y = str(2.5)
z = str("5")

print(x,y,z) # 1 2.5 5

#Strings in python

a = "Hello Yasin"

print(a[0]) # H
print(a[-1]) # n

print(a[2:5]) # 5 not included llo

#like trim - strip

a = "     Hello i     n     "

print(a.strip())

a = "Hello Yasin"

print(len(a)) # 11

print(a.upper())
print(a.lower())

# replace string

print(a.replace("Yasin","Python"))

# split

a = "There are 2 apples in the basket"

print(a.split(" "))

b = a.split(" ")
count = 0
for i in b:
    print(i)
    count += 1

print(count)
print(len(b))

#operators

x = 12
y = 15

print(x+y) # 27
print(y-x) # 3
print(x*y) # 180
print(x**y) # 15407021574586368
print(y/x) # 1,25
print(y%x) # 3


#python lists

thisList = ["banana","apple","cheery","mango","melon"]

print("List length: "+ str(len(thisList)))

print(thisList[0]) # first item

print(thisList[-1]) # last item

print(thisList[-3:]) #['cheery', 'mango', 'melon']

print(thisList[0:2]) # ['banana', 'apple']

thisList[0] = "Dragon Fruit"

print(thisList)
count = 1
for x in thisList:
    print(str(count)+". fruit is "+ x)
    count += 1

for x in thisList:
    if(x == "mangol"):
        print("Fruit is founded")
        break
    else:
        print("Your fruit is not found in fruit list")

thisList.append("Water Melon")

print("append water melon: "+str(thisList))

thisList.insert(1,"Orange")

print("insert orange: "+str(thisList))

thisList.remove("cheery")

print("remove cheery: "+str(thisList))

thisList.pop()

print("pop: "+ str(thisList))

del thisList[0]

print("Delete first item: "+ str(thisList))

#thisList.clear()
#thisList = []
print("This list should be empty: "+ str(thisList))

# using list constructor for creating a list

thisList = list(("Elma","Armut","Karpuz","Çilek"))

print(thisList)


#Tuples

thisTuple = ("BMW","Toyota","Mercedes","Volkwagen")

print("This is a tuple: "+ str(thisTuple))

print(thisTuple[1]) # toyota

# we can not update tuple value
#thisTuple[0] = "Volvo"
#print("New tuple: "+ str(thisTuple))

for y in thisTuple:
    print(y)

if "Mercedes" in thisTuple:
    print("Mercedes is in the tuple")

# del thisTuple
#
# print("Is tuple deleted: " + str(thisTuple))

thisTuple = tuple(("Kia","Hyundai","Sangyong"))

print(thisTuple)

# set in python
#unordered
thisSet = {"red","green","blue"}

print("This set is : "+ str(thisSet))

for x in thisSet:
    print(x)

print("red" in thisSet) # True

thisSet.add("yellow")

print("After yellow: "+ str(thisSet))

# add multiple item

thisSet.update({"purple","pink","gray"})

print("After new colors: "+ str(thisSet))

print("length of set: "+ str(len(thisSet)))

thisSet.remove("yellow")

print("After yellow removed: "+ str(thisSet))

thisSet = set(("apple", "banana", "cherry"))

print("new set: "+ str(thisSet))


# Dictionary in python

thisDic = {
    "name":"Yasin",
    "surname":"Deger",
    "age":"37",
    "country":"italy"
}

print(thisDic)

for x in thisDic.values():
    print(x)

print(thisDic["surname"])

thisDic["country"] = "turkey"

print(thisDic)

if "surname" in thisDic.keys():
    print("surname is exist")

thisDic["color"] = "black"

print(thisDic)

thisDic.pop("color")

print("After color removed: "+ str(thisDic))

thisdict = dict(brand="Ford", model="Mustang", year=1964)

print(thisdict)

# If else

today = "wEdnEsday"

if today.lower() == "thursday":
    print("Today is thursday")
elif today.lower() == "wednesday":
    print("Today is wednesday")

#shorthand if statements

a = 42
b = 33

if a < b : print("b is greater than a")

print("a is greater than b") if a > b else print("B is greater than a")

#both conditions

a = 12
b = 15
c = 14

if c>a and b>c :
    print("both condition are true")

if c>a and b>c :
    print("at least one condition is true")

#while loop

# i = 0
#
# while(i < 6):
#     print(i)
#     i += 1

# i = 0
#
# while(i < 6):
#     print(i)
#     if i == 3:
#         break
#     i += 1

i = 0

while(i < 6):
    if i == 3:
        i += 1
        continue
    else:
        print("continue: "+ str(i))
        i += 1

newOdd = []

for i in range(100):
    if i % 2 == 0:
        continue
    else:
        newOdd.append(i)


print(newOdd)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

def defaultValueCheck(country="turkey"):
    print("Your country is "+ country)


defaultValueCheck("Sweden")
defaultValueCheck()

def recursive(x):
    return x ** 2


print(recursive(2))

z = lambda a : a +10

print(z(10))

x = lambda a, b: a * b
print(x(5, 6))


x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

class myClass:
    x = 5


classObject = myClass()
print(classObject.x)

class myClass2:

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = myClass2("John",36)

print(p1.name)
print(p1.age)

import array

a = array.array

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[1::2])


def decorator(testDecorator):
    def wrap():
        print("before the function")
        testDecorator()
        print("After the function")

    return wrap

@decorator
def testDecorator():
    print("Hello Decorator")


testDecorator()