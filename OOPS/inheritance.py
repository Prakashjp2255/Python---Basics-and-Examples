"""
==========================================================
                  Inheritance in Python
==========================================================

Definition:
-----------
Inheritance is one of the four main OOP principles.

Inheritance allows one class (Child Class) to inherit
the properties (variables) and methods (functions)
of another class (Parent Class).

In simple words:
----------------
Instead of writing the same code again and again,
we can reuse the existing class.

Inheritance = Code Reusability

==========================================================
                Real-Time Example
==========================================================

Parent : Animal

Properties
----------
name
age

Methods
-------
eat()
sleep()

            ▲
            |
        Inherited by
            |
            ▼

Child : Dog

Properties
----------
name
age

Methods
-------
eat()
sleep()
bark()

The Dog class automatically gets all the
properties and methods of Animal.

==========================================================
            Syntax of Inheritance
==========================================================

class Parent:
    ...

class Child(Parent):
    ...

Child inherits everything from Parent.

==========================================================
                Example 1
            Basic Inheritance
==========================================================
"""


class Animal:

    # Parent Constructor
    def __init__(self, name):
        self.name = name

    # Parent Method
    def speak(self):
        print(f"{self.name} makes a sound.")


# Child Class
class Dog(Animal):
    pass


print("========== Example 1 ==========")

d1 = Dog("Buddy")
d1.speak()

"""
Output

Buddy makes a sound.

Explanation:
-------------
Dog inherits the speak() method from Animal.
Even though Dog has no methods,
it can still use speak().
"""

print()

"""
==========================================================
                Example 2
        Child Adds Its Own Method
==========================================================
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} says Woof!")


print("========== Example 2 ==========")

d1 = Dog("Rocky")

d1.eat()
d1.bark()

"""
Output

Rocky is eating.
Rocky says Woof!

Explanation:
-------------
Dog inherits eat() from Animal.

Dog also has its own method bark().
"""

print()

"""
==========================================================
                Example 3
            Using super()
==========================================================
"""


class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, age):

        # Calls Parent Constructor
        super().__init__(name)

        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


print("========== Example 3 ==========")

d1 = Dog("Tommy", 3)
d1.display()

"""
Output

Name : Tommy
Age  : 3

Explanation:
-------------
super().__init__(name)

calls the constructor of the Parent class.

This avoids rewriting:

self.name = name

==========================================================
                Example 4
            Method Overriding
==========================================================
"""


class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    # Override Parent Method
    def speak(self):
        print("Dog says Woof!")


print("========== Example 4 ==========")

d1 = Dog()
d1.speak()

"""
Output

Dog says Woof!

Explanation:
-------------
The Child class replaces the Parent's speak()
method with its own implementation.

This is called Method Overriding.

==========================================================
                Types of Inheritance
==========================================================

1. Single Inheritance

Animal
   │
   ▼
 Dog


2. Multilevel Inheritance

Animal
   │
   ▼
 Dog
   │
   ▼
 Puppy


3. Multiple Inheritance

 Animal     Pet
     \      /
      \    /
       \  /
        Dog


4. Hierarchical Inheritance

        Animal
       /   |   \
     Dog  Cat  Cow


5. Hybrid Inheritance

Combination of two or more inheritance types.

==========================================================
                Advantages
==========================================================

✔ Code Reusability

✔ Less Duplicate Code

✔ Easy Maintenance

✔ Better Organization

✔ Easier Extension of Existing Code

✔ Supports Method Overriding

==========================================================
                Interview Questions
==========================================================

Q1. What is Inheritance?

Inheritance is the process by which one class
acquires the properties and methods of another class.

----------------------------------------------------------

Q2. Why do we use Inheritance?

To reuse existing code and reduce duplication.

----------------------------------------------------------

Q3. What is Parent Class?

The class whose members are inherited.

Example:
Animal

----------------------------------------------------------

Q4. What is Child Class?

The class that inherits from another class.

Example:
Dog

----------------------------------------------------------

Q5. What is super()?

super() is used to access the Parent class.

Example:

super().__init__(name)

==========================================================
                    Summary
==========================================================

Parent Class
-------------
Existing class.

Child Class
------------
New class that inherits Parent.

Inheritance
-------------
Reuse existing code.

super()
--------
Calls Parent constructor or methods.

Method Overriding
-----------------
Child replaces Parent's method.

Benefits
--------
✔ Code Reusability

✔ Less Code

✔ Easy Maintenance

✔ Better Readability

==========================================================
"""