# Code Runner: RUN: Ctrl-Alt-n          STOP: Ctrl-Alt-m
# Math     +ADD     -SUB    *MULT   /DIV    **EXPONENT

# x = "john"
# y = "john"

# print(f"x = _{x}_ at address {id(x)}")
# print(f"y = _{y}_ at address {id(y)}")

# exit()


def printName(n):
    print("Your name is", n)


def print_age(a):
    print("age =", a)


age = 5
your_age = 23
print("My age is", age, "and your age is", your_age)
print(f"My age is {age} and your age is {your_age}")
print("My name is Mary\nand I am 36")   # \n newline

name = "Larry"
# name = input("Enter your name: ")
print("Your name is", name)

printName("Mary")


# def printName(n):
#     print("Your name is", n)


age = 3
# print("may age is " + age)
print("may age is " + str(age))

print(float(age))
num = 4.9
print(f"num = {num} and is of type {type(num)}")
print(int(num))

num = 8
print(num**100)


print("Hello my name is ")
print("Mary")

print("Hello my name is ", end="")
print("Mary")

print("Hello my name is ", end="--- ")
print("Mary")

b = True
print(b)

x = 8
y = 8

if x > y:
    print(f"{x} > {y}")
elif x == y:
    print(f"{x} = {y}")
else:
    print(f"{x} < {y}")

# Python DOES NOT have ARRAYs   use List      there are import to work with arrays

this_list = ["apple", "banana", "cherry"]
print(this_list)
print(this_list[1])

this_list.append("orange")
print(this_list)

this_list.remove("banana")
print(this_list)

for x in this_list:
    print(x)

print("\nDictionaries are key:value pairs - ORDERED")
print("--------------------------------------------")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict", thisdict)
print("thisdict", thisdict.keys())
print("thisdict", thisdict.values())
for key in thisdict.keys():
    print(key, thisdict[key])


print("\nTuples store multiple items in a single variable")
print("     which are indexed and unchangeable")
print("--------------------------------------------")
thistuple = (142, "banana", True, "apple", 3.14159)
print("Tuple", thistuple)


print("\nSets are collections which are unordered, unindexed,")
print("      and set items are unchangeable, and ignore duplicates")
print("--------------------------------------------")
thisset = {"apple", 56, "cherry", "apple"}
print("Set", thisset)
for setitem in thisset:
    print(setitem)
