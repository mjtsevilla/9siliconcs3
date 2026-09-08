class clubMember:
  
  def __init__(self, name, gradeLevel, position, active):
    self.name=name
    self.gradeLevel=gradeLevel
    self.position=position
    self.__active=active

  def updatePosition(self, newPosition):
    self.position=newPosition

  def displayInfo(self):
    print("Name: ", self.name)
    print("gradeLevel: ", self.gradeLevel)
    print("Position: ", self.position)
    print("Active: ", self.__active)

  def changeStatus(self, status):
    self.__active=status

  def getStatus(self):
    return self.__active

member1=clubMember("Yuna", 10, "President", True)

member2=clubMember("Jaz", 8, "Secretary", True)

print("---BEFORE---")
print("Object 1: ")
member1.displayInfo()

print("\nObject 2: ")
member2.displayInfo()

print("\nChanging Object 1's Position" )
member1.updatePosition("Vice President")

print("\n---AFTER---")
print("Object 1: ")
member1.displayInfo()

print("\nObject 2: ")
member2.displayInfo()
