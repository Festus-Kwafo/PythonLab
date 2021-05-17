#Write a program that reads integers from the user and stores them in a list.
#Yourprogram should continue reading values until the user enters 0. Then it
#should display all of the values entered by the user (except for the 0) in order from
#smallest to largest,with one value appearing on each line.
dat =[]
num = int(input("Enter Number: "))
if num !=0:
    dat.append(num)
    while num != 0:
        num = int(input("Enter Number: "))
        dat.append(num)
    else:
        print(sorted(dat[:-1]))
else:
    print("Invalid Number")
