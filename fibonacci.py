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

Mycal = Fibonacci(userTerm)
numerator = Mycal.fTerm()-Mycal.sTerm()
denominator = math.sqrt(5)
fn = numerator/denominator
print(int (fn))

