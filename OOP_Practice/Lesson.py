# # Lesson Abstract Class:

# from abc import ABC, abstractmethod

# class Vechile(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass



# class Car(Vechile):
#     def go(self):
#         print("your drive the car")

#     def stop(self):
#         print("you stopped the car")



# car1 = Car()


# car1.go()




#Lesson super class


# class Shape:
#     def __init__(self,color,filled):
#         self.color = color
#         self.filled = filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self,radius,color,filled):
#         super().__init__(color,filled)
#         self.radius = radius
#     def describe(self):
#         print(f"It is a Circle with an area of {3.14 * self.radius * self.radius}cm^2. ",end="")
#         super().describe()
    
# class Square(Shape):
#     def __init__(self,width, color, filled):
#         super().__init__(color, filled)
#         self.width = width
#     def describe(self):
#         print(f"It is a Square with an area of {self.width * self.width}cm^2. ",end="")
#         super().describe()


# class Triangle(Shape):
#     def __init__(self,width,height,color,filled):
#         super().__init__(color,filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         print(f"It is a Triangle with an area of {self.width * self.height}cm^2. ",end="")
#         super().describe()


# circle = Circle(radius =5,color="black",filled=True)
# square = Square(width=10,color="Blue",filled=False)
# triangle = Triangle(width=10,height=5,color="Green",filled=False)



# circle.describe()
# square.describe()
# triangle.describe()




# polymorphism
# poly = many
# morphe = form

# 2 ways of poly 
# 1. inheritance =an object could be treated of the same type as a parent class
# 2. "Duck typing" = object must have necessary attributes/method
# 1st way = inheritance lesson 




# from abc import ABC, abstractmethod


# class Shape:

#     @abstractmethod
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#     def area(self):
#         return self.side ** 2


# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         self.topping = topping
#         super().__init__(radius)

# shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("Kebab",15)]

# for shape in shapes:
#     print(f"{shape.area()}cm")







# 2nd way = duck typing
# Basically if there is any similarity u can do it.
# so in the car example, its nt gonna speak but lets imagine its an ai car, then it would speak XD. 
# its nt an animal but it can speak basically has the minumum requirements.
# so if it look like a duck and quacks like a duck, it must be a duck




# class Animal:
#     alive = True


# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")


# class Tiger(Animal):
#     def speak(self):
#         print("Roar!")


# class Cow(Animal):
#     def speak(self):
#         print("MOOOOOO!")

# class Car:
#     alive = False
#     def speak(self):
#         print("HONK!")


# animals = [Cat(),Tiger(),Cow(),Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)



# Aggreation lesson = reprents a relationship where one object(the whole)
# contains references to one or more INDEPENDENT objects(the parts)


# these 2 classes doesnt need each other.
# they can exist without eachother
# class Library:
#     def __init__(self,name):
#         self.name = name
#         self.books = []

#     def add_book(self,book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author


# library = Library("GreenLand Super Library")

# book1 = Book("GreenForest","Green Man")
# book2 = Book("RainyForest","Blue Man")

# library.add_book(book1)
# library.add_book(book2)


# print(library.name)

# for book in library.list_books():
#     print(book)



#Compositon lesson
# The composed object directly owns it components ,which cannot exist indepnendently 
# basicaly it owns the objects from other classes


# class Engine:
#     def __init__(self,horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self,size):
#         self.size = size


# class Car:
#     def __init__(self,make,model,horse_power,wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size)for wheel in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} , {self.engine.horse_power}(hp) , {self.wheels[0].size}in"

# car1 = Car(make="Wolksvagen",model="Golf",horse_power=800,wheel_size=20)
# car2 = Car(make="Ford",model="Mustang",horse_power=500,wheel_size=18)
# car3 = Car(make="Wolksvagen",model="Polo",horse_power=600,wheel_size=20)


# print(car1.display_car())
# print(car2.display_car())
# print(car3.display_car())




#Nested class = class defined within another class 
# Allows you to group classes that are close related to each other

# class Company:
#     class Employee:
#         def __init__(self,name,position):
#             self.name = name
#             self.position = position

#         def get_details(self):
#             return f"{self.name} {self.position}"


#     def __init__(self,company_name):
#         self.company_name = company_name
#         self.employees = []

#     def add_employee(self,name,position):
#         new_employee = self.Employee(name,position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         return [employee.get_details()for employee in self.employees]

# company = Company("168hours To Productivity")
# company.add_employee("Ali", "Manager")
# company.add_employee("Azam", "Vice Manager")
# company.add_employee("Yunus", "staff")


# for employe in company.list_employees():
#     print(employe)




# static methods Lesson

# class Employee:

#     def __init__(self,name,position):
#         self.name = name
#         self.position = position

#     #instance method
#     def get_info(self):
#         return f"{self.name} = {self.position}"


#     # Static method belongs to the class not the objects created in the class
#     @staticmethod
#     def is_valid_position(position):
#         valid_position = ["Manager","Project Leader","Worker","Co Manager"]
#         return position in valid_position


# emoplyee1 =Employee("Yunus","Worker")
# emoplyee2 =Employee("Ali","Co Manager")
# emoplyee3 =Employee("Azam","Manager")

# print(Employee.is_valid_position("Manager"))

# print(emoplyee1.get_info())
# print(emoplyee2.get_info())
# print(emoplyee3.get_info())





# Class method = allowss operations related to the class itself
# take (cls) as first parameter, which reprents the class itself.



# class EnergyDrink:

#     count = 0

#     def __init__(self,name,flavour):
#         self.name = name
#         self.flavour = flavour
#         EnergyDrink.count +=1

#     def get_info(self):
#         return f"{self.name} {self.flavour}"

#     @classmethod
#     def get_count(cls):
#         return f"total # of energydrinks: {cls.count}"
    
# energydrink = EnergyDrink("PeachVibe", "Peach")
# energydrink2 = EnergyDrink("GalaxyVibe", "Mango Melon")
# energydrink3 = EnergyDrink("DragonFruitVibe", "DragonFruit")

# print(EnergyDrink.get_count())






#magic method lesson
# pythons build in operations.
# by using the dunnder method it allows developers to define and customize the behvaior of objects.
# dunder method 
# __init__ , __str__ , __eq__ , 
# __str__ returns a string instead of memory 
# __eq__ check if the objects are equal to each other
# __lt__ less then
#__gt__ greater then
#__contains__ to find a keyword your looking for 
# __getitem__ gives you the index 




# class Book:

#     def __init__(self,title,author,num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages


#     def __str__(self):
#         return f"{self.title} by {self.author}"


#     def __eq__(self,other):
#         return self.title == other.title and self.author == other.author


#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#         return self.num_pages > other.num_pages

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"


#     def __contains__(self, item):
#         return item in self.title or item in self.author


#     def __getitem__(self, key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f"item {key} was not found "

    


    
# book1 = Book("The bird", "Birdman", 280)
# book2 = Book("The Tiger", "TigerMan", 250)
# book3 = Book("The cat", "Catman", 300)
# book4 = Book("The bird", "Birdman", 280)


# print("Lion" in book1)
# print("Birdman" in book4)
# print(book1['title'])
# print(book1['author'])
# print(book1['num_pages'])
# print(book1['video'])



#@ property 
# if u add after self. a underscore = _
# it tells u and other devs, they are meant to be protected, they are internal and shouldnt be access outside of the class directly
# but u can still ofc access them but u will get a warning




class Rectangle:
    def __init__(self,width,height):
         self._width = width  
         self._height = height
      
    @property
    def height(self):
         return f"{self._height:.1f}cm"
    @property 
    def width(self):
         return f"{self._width:.1f}cm"

    @width.setter
    def width(self,new_width):
         if new_width > 0:
              self._width = new_width
         else:
              print("width must be greater then zero")

    @height.setter
    def height(self,new_height):
         if new_height > 0:
              self._height = new_height
         else:
              print("height must be greater then zero")

    @width.deleter
    def width(self):
         del self._width
         print("width has been deleted")

    @height.deleter
    def height(self):
         del self._height
         print("height has been deleted")



rectangle = Rectangle(3,4)

del rectangle.width
del rectangle.height


