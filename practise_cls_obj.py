''' 
Instructions
Inside the editor, complete the following steps:
Create a class called Person
Add an __init__ method that takes name and age as parameters
Add a method called greet that prints "Hello, my name is " followed by the name
Create an object p1 of the class with name "John" and age 36
Call the greet method on p1

'''

# ==========================================================
# ❌ Mistakes in Your Code
# ==========================================================

# class person():

#     # ❌ Mistake 1:
#     # You wrote __intit__
#     # Correct spelling is __init__
#     def __intit__(self, name, age):
#         self.name = name
#         self.age = age

#     # ❌ Mistake 2:
#     # Indentation is incorrect.
#     # Methods inside a class should have the same indentation.

#     # ❌ Mistake 3:
#     # Missing 'self' parameter.
#     # Every instance method must have self as the first parameter.
#     def greet():

#         # ❌ Mistake 4:
#         # 'name' is not defined.
#         # Use self.name to access the object's attribute.
#         print("Hello, my name is", name)


# # ❌ Mistake 5:
# # Class name should ideally start with a capital letter (Python convention).
# # Although 'person' works, 'Person' is recommended.
# p1 = person("John", 36)

# # ❌ Mistake 6:
# # greet() is not a standalone function.
# # It belongs to the object p1.
# greet() 



# ==========================================================
# Correct Version
# ==========================================================

# Class names should start with a capital letter (PEP 8 convention)
class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        print("Hello, my name is", self.name)


# Create an object
p1 = Person("John", 36)

# Call the method using the object
p1.greet()



# why init used ? 

class person: 
    def __init__(self ,  name , age , clas):  
        self.name = name 
        self.age = age
        self.clas =clas

p_obj = person("prakash" , 22 , "software engineer") 
a = p_obj.name
b = p_obj.age
c = p_obj.clas
print(a , b , c ) 
        

'''
2. Instructions
Inside the editor, complete the following steps:
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1

'''

# Create the Dog class
class Dog : 
     def __init__(self ,  name  , age ) : 
         self.name = name 
         self.age = age 
     def Bark(self): 
         print(f"{self.name} and the age is {self.age} says Woof!")


# Create an object
d1 = Dog("Buddy" , 3)
# Call the bark method
d1.Bark()
 


# Calling Methods with self
# You can also call other methods within the class using self:

# Example
# Call one method from another method using self:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()


'''
3. Instructions
Inside the editor, complete the following steps:
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1

'''

# Create the Car class
class car : 
     def __init__(self , brand) : 
         self.brand = brand 
     def show(self) :
         return self.brand 
# Create an object
c1 = car("Ford") 
a = c1.show() 
print(a) 



