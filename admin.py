import random
class School:
    def __init__(self, stuName, stuDateofBirth, stuLocation ):
        self.stuName = stuName
        self.stuDateofBirth = stuDateofBirth
        self.stuLocation = stuLocation
    
    def getStudetails(self, getName, getDateofBirth, getLocation):
        stuDetails = School(getName, getDateofBirth, getLocation)
        det.append(stuDetails)
        
    
    def displayStudetails(self, stuDetails):
        print("Name of Student: ", stuDetails.stuName)
        print("Date of birth: ", stuDetails.stuDateofBirth)
        print("Location of Student", stuDetails.stuLocation)
        print("\n")
    
    
det = []

Myadmin = School(" ", " ", " ")
Myadmin.getStudetails(input("Enter Student Name: "), input("Enter Date of Birth: "), input("Enter Student's Location: "))
for i in range(det.__len__()):
    Myadmin.displayStudetails(det[i])

