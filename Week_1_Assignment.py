# 1. Class Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")


# Create an object and call the method
car1 = Car("Toyota", "Corolla", 2022)
car1.display_details()


# 2. Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Instantiate and print both values
rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


# 3. Inheritance Example
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")


# Create an object and call speak()
dog1 = Dog()
dog1.speak()


# 4. Encapsulation Example
class Employee:
    def __init__(self, salary):
        self.__salary = salary  # private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount.")


# Demonstrate encapsulation
emp = Employee(50000)
# print(emp.__salary)  # ❌ This will raise an error (private attribute)
print("Current Salary (via getter):", emp.get_salary())
emp.set_salary(60000)
print("Updated Salary (via getter):", emp.get_salary())


# 5. Multiple Inheritance Example
class A:
    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C(A, B):
    pass


# Create an object of C
c_obj = C()
c_obj.greet()  # Will call method from class A because of Method Resolution Order (MRO)


# 6. Abstract Class Example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Instantiate both and print their areas
circle = Circle(5)
square = Square(4)
print("Area of Circle:", circle.area())
print("Area of Square:", square.area())


# 7. Class Variable Example
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1


# Create multiple objects and print the count
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print("Number of instances created:", Counter.count)
