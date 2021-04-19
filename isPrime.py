# Python program to check if the input number is prime or not

# num = int(input("Type in a number to see if it is PRIME: "))
# while (num>0):
num = int(input("Type in a number to see if it is PRIME: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number or not greater then '0'\n")
print("hello\n\n\n\n")
print("goodbye")
