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


class ClubOfficer(ClubMember):
    def __init__(self, name, gradeLevel, position, active, duty):
        super().__init__(name, gradeLevel, position, active)
        self.duty = duty

    def performDuty(self):
        print(self.name, "is performing the duty of", self.duty)


# Create ClubMember objects
member1 = ClubMember("Jaz", 8, "Secretary", True)
member2 = ClubMember("Yvaine", 9, "Treasurer", True)

# Create ClubOfficer object
officer1 = ClubOfficer(
    "Yuna",
    10,
    "President",
    True,
    "Lead club activities"
)

# Create Club object
club1 = Club("Math Club", "Mr. Syeldir")


# TEST 1 - INHERITANCE
print("--- TEST 1: INHERITANCE ---")
print("Club Officer:", officer1.name)
print("Grade Level:", officer1.gradeLevel)
print("Position:", officer1.position)
print("Active:", officer1.getStatus())
print("Duty:", officer1.duty)

print("\nUsing inherited method:")
officer1.displayInfo()

print("\nOfficer's own method:")
officer1.performDuty()


# TEST 2 - AGGREGATION
print("\n--- TEST 2: AGGREGATION ---")

club1.addMember(member1)
club1.addMember(member2)
club1.addMember(officer1)

print("Club:", club1.name)
print("Adviser:", club1.adviser)

print("\nMembers connected to the club:")

for member in club1.members:
    print("-", member.name, "-", member.position)
