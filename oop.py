# Parent class (base class)
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Encapsulation: private attributes
        self._brand = brand
        self._model = model
        self._battery_life = battery_life
    
    # Method to display phone info
    def display_info(self):
        return f"{self._brand} {self._model} - Battery Life: {self._battery_life} hours"
    
    # Method to simulate calling
    def make_call(self, number):
        return f"Calling {number}..."
    
    # Encapsulation: Method to access battery life
    def get_battery_life(self):
        return self._battery_life

    def set_battery_life(self, new_battery_life):
        self._battery_life = new_battery_life
        return f"Battery life updated to {new_battery_life} hours"

# Child class (derived class) - Inheritance & Polymorphism
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_color):
        # Call the constructor of the parent class
        super().__init__(brand, model, battery_life)
        self._strap_color = strap_color
    
    # Override the display_info method (Polymorphism)
    def display_info(self):
        return f"{self._brand} {self._model} - Battery Life: {self._battery_life} hours - Strap Color: {self._strap_color}"
    
    # Additional method specific to Smartwatch
    def track_heart_rate(self):
        return "Tracking heart rate..."

# Instantiate objects
phone = Smartphone("Apple", "iPhone 13", 20)
watch = Smartwatch("Apple", "Apple Watch Series 7", 18, "Midnight")

# Accessing methods and attributes
print(phone.display_info())  # Polymorphism not applied here
print(phone.make_call("123456789"))

# Smartwatch: Inherited method and polymorphic method
print(watch.display_info())  # Polymorphism in action
print(watch.track_heart_rate())
print(watch.make_call("987654321"))

# Accessing encapsulated attribute
print(phone.get_battery_life())  # Access battery life
print(phone.set_battery_life(25))  # Update battery life
