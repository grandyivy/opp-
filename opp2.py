# Parent class (Animal)
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass (Dog)
class Dog(Animal):
    def move(self):
        return "Running 🐕"

# Subclass (Bird)
class Bird(Animal):
    def move(self):
        return "Flying 🐦"

# Parent class (Vehicle)
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass (Car)
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass (Plane)
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Testing the classes
animals = [Dog(), Bird()]
vehicles = [Car(), Plane()]

# Call the move() method for each animal and vehicle
for animal in animals:
    print(animal.move())  # Each animal moves differently

for vehicle in vehicles:
    print(vehicle.move())  # Each vehicle moves differently
