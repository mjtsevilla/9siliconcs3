# SG 4 Understanding Classes and Objects
## ClubMember
## A ClubMember represents a student who is a member of a school club. It stores information about the student, such as their name, grade level, position, and membership status, and can perform actions related to their membership.
## Properties
| Property | Data Type | Description |
|---|---|---|
| name | string | Name of the club member|
| gradeLevel | int | Grade level of the member |
| position | string | Role or position of the member in the club |
| active | boolean | Indicates whether the member is currently active |
## Methods
| Method | Description |
|---|---|
| updatePosition(newPosition: string) | Changes the member's club position |
| displayInfo() | Displays the member's information |
| changeStatus(Status: boolean) | Changes whether the member is active |

## Class Diagram
![Class Diagram](classDiagram.png/https://github.com/mjtsevilla/9siliconcs3/blob/11c6743d0f7e65a0f87925496ecf9e5a7ce0b89c/classDiagram.png)

## Design Explanation
### Why did you choose this class?
  - I chose the ClubMember class because school clubs have many members, and each member has important information that needs to be organized and managed. This class makes it easier for a school club to keep track of its members.
### Which property is the most important? Why?
  - The name property is the most important because it identifies the club member. Without the member's name, it would be difficult to know which student the other information belongs to.
### Which method is the most useful? Why?
  - The displayInfo() method is the most useful because it allows the system to show all the important information about a club member in one place. This makes it easier to check and manage member records.
