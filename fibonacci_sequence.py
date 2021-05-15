import math
class Fibonacci:
    def __init__(self, userTerm):
        self.userTerm = userTerm

    def fTerm(self):
        f1 = (1 + math.sqrt(5))/2
        ans_f1 = f1**userTerm
        return ans_f1
        
        
    def sTerm(self):
        f2= (1 - math.sqrt(5))/2
        ans_f2 = f2**userTerm
        return ans_f2
     

userTerm = int (input("Enter term: "))
ordinal = lambda userterm: "%d%s" % (userterm,"tsnrhtdd"[(userTerm//10%10!=1)*(userTerm%10<4)*userterm%10::4])
limit = userTerm
while limit > 0:
    
    Mycal = Fibonacci(userTerm)
    numerator = Mycal.fTerm()-Mycal.sTerm()
    denominator = math.sqrt(5)
    fn = int (numerator/denominator)
    print("The value of the "+ str(ordinal(userTerm))+ " term is: " + str (fn))
    userTerm = userTerm-1
    limit = limit-1 




