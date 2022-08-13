# Write a program to check the Armstrong Number?
num = int(input("Enter the number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp>0:
    digit  = temp % 10
    sum +=digit**3
    temp//=3

# display the result
if num == sum:
    print(num,"Is the armstrong number: ")
else:
    print(num, "Is not a armstrong number: ")