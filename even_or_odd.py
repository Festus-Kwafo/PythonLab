#Write a program that reads an integer from the user. Then your program should
#display a message indicating whether the integer is even or odd.
getInteger = int(input("Enter any integer "))
n = getInteger%2
if n == 0:
    print("The integer "+ str(getInteger)+ " is even")
else:
    print("The integer "+ str(getInteger)+ " is odd")
