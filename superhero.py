"""
Assignment 1: Design Your Own Class - Superhero Theme
Assignment 2: Polymorphism Challenge - Vehicles in Action
"""

# ===========================
# ASSIGNMENT 1: SUPERHERO CLASS DESIGN
# ===========================

class Superhero:
    """Base Superhero class with common attributes and methods"""
    
    # Class variable - shared by all superheroes
    total_heroes = 0
    
    def __init__(self, name, real_name, power_level=50):
        """Constructor to initialize superhero attributes"""
        # Instance attributes (encapsulation)
        self.__name = name  # Private attribute
        self.__real_name = real_name  # Private attribute  
        self._power_level = power_level  # Protected attribute
        self.is_active = True
        self.missions_completed = 0
        
        # Increment total heroes count
        Superhero.total_heroes += 1
    
    # Getter methods (encapsulation)
    def get_name(self):
        return self.__name
    
    def get_real_name(self):
        return self.__real_name
    
    def get_power_level(self):
        return self._power_level
    
    # Methods that define superhero behavior
    def introduce(self):
        return f"I am {self.__name}! Ready to protect the world!"
    
    def use_power(self):
        return f"{self.__name} uses their incredible powers!"
    
    def complete_mission(self):
        self.missions_completed += 1
        self._power_level += 5  # Power grows with experience
        return f"{self.__name} completed a mission! Power level now: {self._power_level}"
    
    def __str__(self):
        return f"{self.__name} (Power: {self._power_level}, Missions: {self.missions_completed})"


class FlyingHero(Superhero):
    """Inherited class for heroes who can fly"""
    
    def __init__(self, name, real_name, power_level=50, max_altitude=10000):
        super().__init__(name, real_name, power_level)  # Call parent constructor
        self.max_altitude = max_altitude
        self.is_flying = False
    
    def use_power(self):
        # Override parent method (polymorphism)
        return f"{self.get_name()} soars through the sky at {self.max_altitude} feet!"
    
    def fly(self):
        self.is_flying = True
        return f"{self.get_name()} takes flight!"
    
    def land(self):
        self.is_flying = False
        return f"{self.get_name()} lands gracefully!"


class TechHero(Superhero):
    """Inherited class for technology-based heroes"""
    
    def __init__(self, name, real_name, power_level=50, gadget_count=5):
        super().__init__(name, real_name, power_level)
        self.gadget_count = gadget_count
        self.gadgets = []
    
    def use_power(self):
        # Override parent method (polymorphism)
        return f"{self.get_name()} deploys high-tech gadgets!"
    
    def add_gadget(self, gadget):
        self.gadgets.append(gadget)
        return f"{self.get_name()} acquired new gadget: {gadget}!"
    
    def hack_system(self):
        return f"{self.get_name()} hacks into enemy systems!"


# ===========================
# ASSIGNMENT 2: POLYMORPHISM CHALLENGE - VEHICLES
# ===========================

class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_moving = False
    
    def move(self):
        """Base method - to be overridden by subclasses"""
        return f"{self.brand} {self.model} is moving!"
    
    def stop(self):
        self.is_moving = False
        return f"{self.brand} {self.model} has stopped."
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Car class with specific movement behavior"""
    
    def __init__(self, brand, model, year, fuel_type="gasoline"):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
    
    def move(self):
        """Override: Cars drive on roads"""
        self.is_moving = True
        return f"{self.brand} {self.model} is driving on the highway!"
    
    def honk(self):
        return f"{self.brand} {self.model} goes BEEP BEEP!"


class Plane(Vehicle):
    """Plane class with flying behavior"""
    
    def __init__(self, brand, model, year, max_altitude=35000):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude
        self.altitude = 0
    
    def move(self):
        """Override: Planes fly in the air"""
        self.is_moving = True
        self.altitude = self.max_altitude
        return f"{self.brand} {self.model} is flying at {self.altitude} feet!"
    
    def takeoff(self):
        return f"{self.brand} {self.model} is taking off!"
    
    def land(self):
        self.altitude = 0
        return f"{self.brand} {self.model} is landing!"


class Boat(Vehicle):
    """Boat class with water movement"""
    
    def __init__(self, brand, model, year, boat_type="sailboat"):
        super().__init__(brand, model, year)
        self.boat_type = boat_type
    
    def move(self):
        """Override: Boats sail on water"""
        self.is_moving = True
        return f"{self.brand} {self.model} is sailing across the ocean!"
    
    def anchor(self):
        return f"{self.brand} {self.model} drops anchor!"


class Bicycle(Vehicle):
    """Bicycle class with pedaling behavior"""
    
    def __init__(self, brand, model, year, gear_count=21):
        super().__init__(brand, model, year)
        self.gear_count = gear_count
    
    def move(self):
        """Override: Bicycles are pedaled"""
        self.is_moving = True
        return f"{self.brand} {self.model} is pedaling down the bike path!"
    
    def ring_bell(self):
        return f"{self.brand} {self.model} rings its bell!"


# ===========================
# DEMONSTRATION & TESTING
# ===========================

def demonstrate_assignment_1():
    """Demonstrate the Superhero class system"""
    print("=" * 50)
    print("ASSIGNMENT 1: SUPERHERO CLASS DEMO")
    print("=" * 50)
    
    # Create different types of heroes
    hero1 = Superhero("Captain Courage", "John Smith", 75)
    hero2 = FlyingHero("Sky Sentinel", "Maria Garcia", 80, 15000)
    hero3 = TechHero("Cyber Guardian", "Alex Chen", 70, 8)
    
    # Demonstrate encapsulation
    print(f"Hero's public name: {hero1.get_name()}")
    print(f"Hero's secret identity: {hero1.get_real_name()}")
    print()
    
    # Demonstrate polymorphism - same method, different behaviors
    heroes = [hero1, hero2, hero3]
    print("Heroes using their powers:")
    for hero in heroes:
        print(f"- {hero.use_power()}")
    print()
    
    # Demonstrate inheritance and specific methods
    print("Flying Hero specific actions:")
    print(f"- {hero2.fly()}")
    print(f"- {hero2.land()}")
    print()
    
    print("Tech Hero specific actions:")
    print(f"- {hero3.add_gadget('Nano Shield')}")
    print(f"- {hero3.hack_system()}")
    print()
    
    # Show mission completion
    print("Mission Results:")
    for hero in heroes:
        print(f"- {hero.complete_mission()}")
    
    print(f"\nTotal Heroes Created: {Superhero.total_heroes}")


def demonstrate_assignment_2():
    """Demonstrate polymorphism with vehicles"""
    print("\n" + "=" * 50)
    print("ASSIGNMENT 2: POLYMORPHISM CHALLENGE DEMO")
    print("=" * 50)
    
    # Create different vehicles
    vehicles = [
        Car("Tesla", "Model S", 2023, "electric"),
        Plane("Boeing", "737", 2022, 40000),
        Boat("Yamaha", "Wave Runner", 2023, "jetski"),
        Bicycle("Trek", "Mountain Bike", 2023, 27)
    ]
    
    print("Polymorphism in Action - Same method, different behaviors:")
    print()
    
    # This is the key demonstration of polymorphism!
    # Each vehicle's move() method behaves differently
    for vehicle in vehicles:
        print(f"{vehicle}")
        print(f"   {vehicle.move()}")
        print(f"   {vehicle.stop()}")
        print()
    
    # Demonstrate specific behaviors
    print("Vehicle-specific actions:")
    car = vehicles[0]
    plane = vehicles[1]
    boat = vehicles[2]
    bike = vehicles[3]
    
    print(f"- {car.honk()}")
    print(f"- {plane.takeoff()}")
    print(f"- {boat.anchor()}")
    print(f"- {bike.ring_bell()}")


def polymorphism_challenge():
    """Additional polymorphism examples"""
    print("\n" + "=" * 50)
    print("BONUS: More Polymorphism Examples")
    print("=" * 50)
    
    # Create a mixed list of heroes and vehicles
    entities = [
        FlyingHero("Wind Walker", "Sam Wilson", 85),
        Car("Ferrari", "F40", 2023),
        TechHero("Code Master", "Lisa Park", 90),
        Plane("Airbus", "A380", 2022)
    ]
    
    print("Polymorphism with mixed object types:")
    for entity in entities:
        if hasattr(entity, 'move'):
            print(f"{entity.move()}")
        elif hasattr(entity, 'use_power'):
            print(f"{entity.use_power()}")


# ===========================
# RUN THE DEMONSTRATIONS
# ===========================

if __name__ == "__main__":
    # Run both assignment demonstrations
    demonstrate_assignment_1()
    demonstrate_assignment_2()
    polymorphism_challenge()
    
    print("\n" + "=" * 50)
    print("Both assignments completed successfully!")
    print("Key concepts demonstrated:")
    print("- Classes and Objects")
    print("- Constructors and Attributes") 
    print("- Encapsulation (private/protected attributes)")
    print("- Inheritance")
    print("- Polymorphism (method overriding)")
    print("- Method overloading")
    print("=" * 50)