class Room:
    def studentName(self, nameOfStudent):
        self.nameOfStudent = nameOfStudent


    def __init__(self, roomNumber, totalNumber):
        self.roomNumber = roomNumber
        self.totalNumber = totalNumber
        self.limit = 4

    def increaseTotalStudents(self):
        self.totalNumber = int(self.totalNumber) + 1    

nameOfStudent = input("Please Enter your name: ")
roomNumber = input("Please enter your room Number: ")
totalNumber = input("Please enter total students: ")

myRoom = Room(roomNumber, totalNumber)
myOcc = Room(nameOfStudent)


print("Name: "+ nameOfStudent)
print("Room Number: " + roomNumber)
print("Total: " + totalNumber )

myRoom.increaseTotalStudents()

print("After increase")
print("Total: " + totalNumber)

