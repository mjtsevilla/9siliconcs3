class ClubMember:
    def __init__(self, name, gradeLevel, position, active):
        self.name = name
        self.gradeLevel = gradeLevel
        self.position = position
        self.__active = active

    def updatePosition(self, newPosition):
        self.position = newPosition

    def displayInfo(self):
        print("Name:", self.name)
        print("Grade Level:", self.gradeLevel)
        print("Position:", self.position)
        print("Active:", self.__active)

    def changeStatus(self, status):
        self.__active = status

    def getStatus(self):
        return self.__active


class Club:
    def __init__(self, name, adviser):
        self.name = name
        self.adviser = adviser
        self.members = []

    def addMember(self, member):
        self.members.append(member)

    def displayMembers(self):
        print("Club:", self.name)
        print("Adviser:", self.adviser)
        print("Members:")

        for member in self.members:
            print("-", member.name, "-", member.position)


# Create objects
club1 = Club("Math Club", "Mr. Syeldir")

member1 = ClubMember("Yuna", 10, "President", True)
member2 = ClubMember("Jaz", 8, "Secretary", True)
member3 = ClubMember("Yvaine", 9, "Treasurer", True)


# BEFORE RELATIONSHIP
print("--- BEFORE RELATIONSHIP ---")
print("Club:", club1.name)
print("Number of members:", len(club1.members))


# BUILDING RELATIONSHIP
print("\n--- BUILDING RELATIONSHIP ---")
print("Adding members to the Math Club...")

club1.addMember(member1)
club1.addMember(member2)
club1.addMember(member3)


# AFTER RELATIONSHIP
print("\n--- AFTER RELATIONSHIP ---")
club1.displayMembers()

print("\n--- RELATED OBJECTS ---")

for member in club1.members:
    print("Name:", member.name)
    print("Grade Level:", member.gradeLevel)
    print("Position:", member.position)
    print("Active:", member.getStatus())
    print()
