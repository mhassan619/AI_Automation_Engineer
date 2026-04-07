from abc import ABC, abstractmethod
class Animal(ABC):   #abstract class
    def __init__(self,name,age): 
        self.name = name
        self._age = age
    @abstractmethod
    def sound(self):  #abstract method - it must be implemented.
        pass
    @abstractmethod
    def info(self):
        pass
    def eat(self):  #Normal method - override  is otional. 
        print(f"{self.name} is eating.")
class Goat(Animal):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milkcapacity = milk_capacity
    def sound(self):  #implementing it is important
        print(f"{self.name}: Meh Meh!")
    def info(self):
        print(f"Goat: {self.name}, Age: {self._age}, Milk: {self.__milkcapacity}L/day.")
    def milk_production(self,days):
        return self.__milkcapacity * days
class Cow(Animal):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milkcapacity = milk_capacity
    def sound(self):
        print(f"{self.name}: Moo!")
    def info(self):
        print(f"Cow: {self.name}, Age: {self._age}, Milk: {self.__milkcapacity}L/day.")
    def milk_production(self,days):
        return self.__milkcapacity * days
# a = Animal("Cow",78)  #this line gives error because object is not made from abstract class
animals = [Goat("Safeda",3,2.5), Cow("Daisy",5,15)]
for animal in animals:
    animal.sound()
    animal.info()
    animal.eat() # from parent

print("\n\n")
##Goat Farm Version 3 including Complete OOP four pillars
from abc import ABC, abstractmethod
class Animal2(ABC):
    def __init__(self,name,age):
        self.name = name
        self._age = age
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def milk_production(self,days):
        pass
    def eat(self):
        print(f"{self.name} is eating grass.")
class Goat2(Animal2):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milk_capacity = milk_capacity
    def sound(self):
        print(f"{self.name}: Meh Meh!")
    def milk_production(self, days):
        return self.__milk_capacity * days
    def get_milk_capacity(self):
        return self.__milk_capacity
class Cow2(Animal2):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milk_capacity = milk_capacity
    def sound(self):
        print(f"{self.name}: Moo!")
    def milk_production(self, days):
        return self.__milk_capacity * days
class Farm:
    def __init__(self,farm_name):
        self.farm_name = farm_name
        self.__animals = [] # private list
    def add_animal(self,animal):
        self.__animals.append(animal)
        print(f"{animal.name} added to the farm!")
    def total_milk(self,days):
        total = 0
        for animal in self.__animals:
            total += animal.milk_production(days)
        return total
    def all_sounds(self):
        print(f"\n--- Sounds of {self.farm_name} ---")
        for animal in self.__animals:
            animal.sound()
    def farm_report(self,days):
        print(f"\n📊 {self.farm_name} Report ({days} days)")
        print("-" * 35)
        for animal in self.__animals:
            milk = animal.milk_production(days)
            print(f"{animal.name}: {milk} litres")
        print("-" * 35)
        print(f"Total Milk: {self.total_milk(days)} litres")
farm = Farm("Hassan's Farm")
farm.add_animal(Goat("Safeda",3,2.5))
farm.add_animal(Goat("Kali",4,3.0))
farm.add_animal(Cow("Daisy",5,15))
farm.all_sounds()
farm.farm_report(30)