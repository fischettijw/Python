x = 8
y = [1, 2, 3, 4, 5]


print(y)

y = y + y

y = y + y
y = y + [3, 4, 5]


while True:
    y.remove(5)


y

y = [7, 3, 9, 12, 45]
print(y)
print(y+y)
print(y)

myList = [2, 1, 3, 5, 1, 1, 1, 0]
valueToBeRemoved = 1

print(myList)
try:
    while True:
        myList.remove(valueToBeRemoved)
except ValueError:
    pass

print(myList)
