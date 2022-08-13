# Write a python program to find a factorial of a number.

Number = int(input("Enter the number: "))

factorial = 1

if Number < 0:
    print("sorry, fact2orial does not exit negative number: ")
elif Number == 0:
    print("The factorial 0 is 1: ")
else:
    for i in range(1,Number+1):
        factorial = factorial*i
    print("The factorial is" , Number, "is",factorial)