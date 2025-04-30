"""
🏗️ OOP Assignment: Superhero Universe & Polymorphism Challenge
Demonstrates:
- Class design with encapsulation
- Inheritance
- Polymorphism
- Method overriding
"""

# ==================== 🦸 SUPERHERO CLASSES ====================
class Superhero:
    """Base class demonstrating encapsulation and inheritance"""
    def __init__(self, name, secret_identity, power_level=50):
        self._name = name  # Protected attribute
        self.__secret_identity = secret_identity  # Private attribute
        self.power_level = power_level
        self.abilities = ["Super strength"]
        
    def reveal_identity(self, authorization):
        """Encapsulation example with controlled access"""
        if authorization == "SHAZAM":
            return f"Secret identity: {self.__secret_identity}"
        return "🔒 Identity protected!"
    
    def train(self, hours):
        """Method to increase power level"""
        self.power_level += hours * 2
        return f"{self._name} trained for {hours} hours! Power level: {self.power_level}"
    
    def use_ability(self):
        """Polymorphic method to be overridden by subclasses"""
        return f"{self._name} uses {self.abilities[0]}!"
    
    def __str__(self):
        return f"Superhero: {self._name} | Power: {self.power_level}"

class SpiderHero(Superhero):
    """Subclass demonstrating inheritance"""
    def __init__(self, name, secret_identity, web_color="red"):
        super().__init__(name, secret_identity, 75)
        self.web_color = web_color
        self.abilities.extend(["Web slinging", "Wall crawling", "Spider sense"])
        
    def use_ability(self):
        """Overridden polymorphic method"""
        return f"{self._name} shoots {self.web_color} webs! 🕸️"
    
    def climb_building(self):
        """Subclass-specific method"""
        return f"{self._name} climbs skyscrapers with ease!"

class IceHero(Superhero):
    """Subclass demonstrating inheritance"""
    def __init__(self, name, secret_identity, freeze_power=-50):
        super().__init__(name, secret_identity, 80)
        self.freeze_power = freeze_power
        self.abilities.extend(["Ice blast", "Snow creation", "Cold resistance"])
        
    def use_ability(self):
        """Overridden polymorphic method"""
        return f"{self._name} freezes enemies at {self.freeze_power}°C! ❄️"
    
    def make_ice_bridge(self):
        """Subclass-specific method"""
        return f"{self._name} creates an ice bridge across the river!"

# ==================== 🚗 VEHICLE CLASSES (POLYMORPHISM) ====================
class Vehicle:
    """Base class for polymorphism demonstration"""
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def move(self):
        """Polymorphic method to be overridden"""
        return f"{self.name} is moving at {self.speed} mph"

class Car(Vehicle):
    """Subclass demonstrating polymorphism"""
    def move(self):
        """Overridden method with specific behavior"""
        return f"🚗 {self.name} is driving on the road at {self.speed} mph"
    
    def honk(self):
        """Subclass-specific method"""
        return "Beep beep!"

class Plane(Vehicle):
    """Subclass demonstrating polymorphism"""
    def move(self):
        """Overridden method with specific behavior"""
        return f"✈️ {self.name} is flying at {self.speed} mph"
    
    def take_off(self):
        """Subclass-specific method"""
        return "Fasten your seatbelts for takeoff!"

class Boat(Vehicle):
    """Subclass demonstrating polymorphism"""
    def move(self):
        """Overridden method with specific behavior"""
        return f"🛥️ {self.name} is sailing at {self.speed} knots"
    
    def anchor(self):
        """Subclass-specific method"""
        return "Dropping anchor!"

# ==================== 🧪 DEMONSTRATION FUNCTIONS ====================
def superhero_demo():
    """Demonstrates superhero class functionality"""
    print("\n" + "="*40)
    print("🦸 SUPERHERO DEMONSTRATION")
    print("="*40)
    
    heroes = [
        SpiderHero("Spider-Man", "Peter Parker"),
        IceHero("Captain Cold", "Leonard Snart")
    ]
    
    for hero in heroes:
        print("\n" + str(hero))
        print(hero.use_ability())
        print(hero.train(3))
        print(hero.reveal_identity("SHAZAM"))
        
        # Demonstrate subclass-specific methods
        if isinstance(hero, SpiderHero):
            print(hero.climb_building())
        elif isinstance(hero, IceHero):
            print(hero.make_ice_bridge())

def polymorphism_demo():
    """Demonstrates polymorphism with vehicles"""
    print("\n" + "="*40)
    print("🚗 POLYMORPHISM DEMONSTRATION")
    print("="*40)
    
    vehicles = [
        Car("Mustang", 120),
        Plane("Boeing 747", 570),
        Boat("Luxury Yacht", 25)
    ]
    
    for vehicle in vehicles:
        print("\n" + vehicle.move())
        
        # Demonstrate subclass-specific methods
        if isinstance(vehicle, Car):
            print(vehicle.honk())
        elif isinstance(vehicle, Plane):
            print(vehicle.take_off())
        elif isinstance(vehicle, Boat):
            print(vehicle.anchor())

# ====================  MAIN EXECUTION ====================
if __name__ == "__main__":
    print("🌟 OOP ASSIGNMENT: SUPERHEROES & POLYMORPHISM 🌟")
    
    # Run both demonstrations
    superhero_demo()
    polymorphism_demo()
    
    print("\n" + "="*40)
    print("✅ ASSIGNMENT COMPLETE")
    print("="*40)