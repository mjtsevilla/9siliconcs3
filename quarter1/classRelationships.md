# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: ClubMember

Description: A ClubMember represents a student who is a member of a school club. It stores information about the student, such as their name, grade level, position, and membership status, and can perform actions related to their membership.

## New Related Class
Class: Club

Description: A Club refers to a school organization of ClubMembers who share the same interests. There are various clubs on every school, such as Academic and Literary Club, Arts and Creativity Club, and Sports Club,  with several fun and interesting activities like solving puzzles, performing in school events, and playing team sports.

## Association
Relationship: Club contains ClubMembers

Explanation: A Club is connected to ClubMember because a club needs members to participate in its activities and events. The Club keeps track of its members, while the ClubMember represents the students who belong to the club. This relationship allows the club to manage and access information about its members.

## Multiplicity
Multiplicity: One-to-Many

Explanation: One club can have many members, which provides opportunities for members to build friendship with other students who share similar interests. Having multiple members also helps keep the club active because when members leave, there are still other members who can continue participating. 

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
- The association between Club and CLubMember is that a Club contains ClubMember objects. The club needs members to participate in activities and events. The club class manages the collection of students who belong to it. This allows the club to access information about its students.
### What multiplicity did you choose and why?
- I chose a One-to-Many multiplicity because one club can have zero or more members. A club can continue to add members as more students join the organization. Having many members also allows students with similar interests to participate and work together. 
### How did you implement the relationship in Python?
- I implemented the relationship by creating a member list inside the club class. The addMember() method receives a CLubMember object and adds it to the list. For example, club1.addMember(member1) stores the acual member1 object inside club1.members. This creates a direct relationship between the club and its members.
### Why did you store an object reference instead of copying its data?
-I stored an object reference because the club should use the actual ClubMember object rather than making another copy of the member's information. For example, club1.members contains member1, which already has Yuna's name, grade level, position, and status. This avoids duplicating the same information and allows the club to access the member's existing data. 
### If your relationship uses many, why is a list appropriate?
- A list is appropriate because one club can have many ClubMember objects. The members list contains the actual member objects, such as member1, member2, and member3. A loop can then go through the list and access each member's information. This makes it easy to add more members later.
