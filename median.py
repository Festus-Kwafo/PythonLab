#Write a function that takes three numbers as parameters, and returns the median
#value of those parameters as its result.
class Median:
    def median(self, a, idx):
        idx = 1
        for idx in range(0,3):
            a = int(input("Enter number: "))
            lst.append(a)
            idx= idx +1
        
        lst.sort()
        return print("The median is: "+str(lst[1]))
lst=[]
Mymedian= Median()
Mymedian.median(0, 0)
