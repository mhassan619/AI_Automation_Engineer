## Polymorphism
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
shapes = [Circle(5),Rectangle(4,6),Triangle(3,8)]
for shape in shapes:
    print(f"Area: {shape.area()}")

##Encapsulation
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance  ##private attribute 
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited")
        else:
            print("Amount must be positive.")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance!")
        elif amount <=0:
            print("Amount must be positive.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn.")
    def get_balance(self):
        return self.__balance
acc = BankAccount("Hassan",20000)
acc.deposit(10000)
acc.withdraw(15000)
print(acc.get_balance())

##Upgraded GoatFarm
class Animal:
    def __init__(self,name,age):
        self.name = name
        self._age = age 
    def sound(self):
        pass
    def info(self):
        pass
class Goat(Animal):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milk_capacity = milk_capacity
    def sound(self):
        print(f"{self.name} is speaking: Meh Meh!")
    def milk_production(self,days):
        return self.__milk_capacity * days
    def get_milk_capacity(self):
        return self.__milk_capacity
    def info(self):
        print(f"""Name: {self.name}
Age: {self._age}
Milk Capacity: {self.__milk_capacity}""")
class Cow(Animal):
    def __init__(self, name, age,milk_capacity):
        super().__init__(name, age)
        self.__milk_capacity = milk_capacity
    def sound(self):
        print(f"{self.name} is speaking: Moo Moo!")
    def milk_production(self,days):
        return self.__milk_capacity * days
    def info(self):
                print(f"""Name: {self.name}
Age: {self._age}
Milk Capacity: {self.__milk_capacity}""")
animals = [Goat("Safeda",3,2.5),Cow("Daisy",5,15)]
for animal in animals:
    animal.sound()
    animal.info()
    print(animal.milk_production(30))