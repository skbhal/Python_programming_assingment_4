# write a python program to find the sum of natural number?
n = int(input("Enter any natural number: "))

if n<0:
    print("Wrong input, please Enter the positive number: ")
else:
    sum = 0
    while (n>0):
        sum +=n
        n-=1
    print("The sum of the natural number is",sum )