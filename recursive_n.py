#class N:
#    def recursive(n):
 #       abs(n)
  #      if n==0:
   #         print(n)
    #    else:
     #       print(n-1)
def recursive(n):
    if n == 0:
        return
    else:
        if n >= 1:
            print(n)
            recursive(n - 2)

a = int(input("Enter a number: "))
recursive(a)


