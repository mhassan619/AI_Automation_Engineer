class Animal:
    def  __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(f"{self.name} is barking: Woof Woof!")
    def info(self):
        super().info()
        print(f"Breed: {self.breed}")
class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    def meow(self):
        print(f"{self.name} is speaking: Meow!")
dog1 = Dog("Bruno", 3, "Labrador")
dog1.eat()
dog1.bark()
dog1.info()
cat1 = Cat("Mimi",2,"White")
cat1.eat()
cat1.meow()
cat1.info()
print("\n")

### Practice scenerio
class Animal2:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def eat(self):
        print(f"{self.name} is eating.")
    def sound(self):
        print(f"{self.name} produces cool sound.")
class Goat(Animal2):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.milk_capacity = milk_capacity
    def sound(self):
        print(f"{self.name} is speaking: Meh Meh!")
    def milk_production(self,days):
        print(f"{self.name} milk production in litres per day: {self.milk_capacity}")
        total_production = self.milk_capacity * days
        print(f"Total milk Production in {days} Days: {total_production}")
class Cow(Animal2):
    def __init__(self, name, age,milk_capacity,breed):
        super().__init__(name, age)
        self.milk_capacity = milk_capacity
        self.breed = breed
    def sound(self):
        print(f"{self.name} is speaking: Moo! ")
    def milk_production(self,days):
        print(f"{self.name} produces a milk per day in litres: {self.milk_capacity}")
        total_production = self.milk_capacity * days
        print(f"Total milk Production in {days} Days: {total_production}")
g1 = Goat("Safeda",3,2.5)
g1.eat()
g1.sound()
g1.milk_production(30)
c1 = Cow("Daisy",5,7,"Holstein")
c1.sound()
c1.milk_production(30)