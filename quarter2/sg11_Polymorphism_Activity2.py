1. 
a. Duck typing is a concept in Python where an object can be used based on the methods it has, rather than the class it belongs to. if an object has he required method, Python can use it even if it does not inherit from another class.
b. The Car class needed to have the same method, such as make_sound() or whichever the method loop calls. It does not need to inherit from the Animal class as long as it has that method.

2.
class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle):
  vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

start_trip(car1)
start_trip(boat1)
start_trip(drone1)

3. The code demonstrates polymorphism because the same move() method is used by different classes, but each class performs a different action. The start_trip function can work with Car, Boat, and Drone objects without needing to know their specific classes.
