# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass   

class Car(Vehicle):
    def move(self):
        print("🚗 Driving")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Cycling")

vehicles = [Car(), Plane(), Bicycle()]
for v in vehicles:
    v.move()
