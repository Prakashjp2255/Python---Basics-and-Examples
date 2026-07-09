"""
==========================================================
                  Abstraction in Python
==========================================================

Definition:
-----------
Abstraction is one of the four main OOP principles.

Abstraction means:
    -> Hiding the implementation details.
    -> Showing only the essential features to the user.

In simple words:
----------------
The user knows WHAT an object does,
but doesn't need to know HOW it does it.

==========================================================
                Real-Time Examples
==========================================================

1. Car
------
You know how to:
    ✔ Start the car
    ✔ Stop the car
    ✔ Accelerate

But you don't need to know how
the engine works internally.

--------------------------------------------

2. ATM Machine
--------------
You know how to:
    ✔ Withdraw money
    ✔ Deposit money
    ✔ Check balance

You don't know how the bank processes
your transaction internally.

--------------------------------------------

3. Mobile Phone
---------------
You know how to:
    ✔ Make calls
    ✔ Send messages
    ✔ Browse the internet

You don't know the internal implementation.

These are examples of Abstraction.

==========================================================
        Abstract Class and Abstract Method
==========================================================

Python provides the abc module.

abc = Abstract Base Class

To create an Abstract Class:

from abc import ABC, abstractmethod

ABC
----
Used to create an Abstract Class.

@abstractmethod
---------------
Used to create an Abstract Method.

==========================================================
                Example 1
        Creating an Abstract Class
==========================================================
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says Woof!")


print("========== Example 1 ==========")

dog = Dog()
dog.sound()

"""
Output

Dog says Woof!

Explanation:
-------------
Animal is an Abstract Class.

sound() is an Abstract Method.

Dog inherits Animal
and provides the implementation.

"""

print()

"""
==========================================================
                Example 2
      Cannot Create Object of Abstract Class
==========================================================
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


"""
The following code will produce an error.

shape = Shape()

TypeError:
Can't instantiate abstract class Shape
with abstract method area

Reason:
-------
Abstract Classes cannot be instantiated.

"""

print("========== Example 2 ==========")
print("Abstract classes cannot create objects.")

print()

"""
==========================================================
                Example 3
      Child Class Implements Method
==========================================================
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)


print("========== Example 3 ==========")

r = Rectangle(10, 5)
r.area()

"""
Output

Area = 50

Explanation:
-------------
Rectangle inherits Shape.

Rectangle MUST implement area().

Otherwise Python throws an error.

"""

print()

"""
==========================================================
            What Happens If We Don't Implement?
==========================================================


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    pass


circle = Circle()

Error:

TypeError:
Can't instantiate abstract class Circle
with abstract method area

Reason:
-------
Every Child Class MUST implement
all Abstract Methods.

"""

print("========== Example 4 ==========")
print("Every child class must implement abstract methods.")

print()

"""
==========================================================
        Difference Between Interface and Abstraction
==========================================================

Python does not have interfaces like Java.

Instead,
Python uses Abstract Classes.

==========================================================
        Abstraction vs Encapsulation
==========================================================

Abstraction
-----------
Hides implementation.

Example:
Car Engine

You only know:

Start()
Stop()

Not the engine logic.

--------------------------------------------

Encapsulation
-------------
Protects data.

Example:

Private Variable

self.__balance

==========================================================
                Advantages
==========================================================

✔ Hides unnecessary details.

✔ Improves Security.

✔ Reduces Complexity.

✔ Makes Code Easy to Understand.

✔ Easy Maintenance.

✔ Encourages Standard Design.

==========================================================
                Interview Questions
==========================================================

Q1. What is Abstraction?

Abstraction is the process of hiding
implementation details and showing
only the essential functionality.

----------------------------------------------------------

Q2. Which module is used?

abc

----------------------------------------------------------

Q3. What is ABC?

ABC stands for

Abstract Base Class.

----------------------------------------------------------

Q4. What is @abstractmethod?

It is a decorator used to declare
an Abstract Method.

----------------------------------------------------------

Q5. Can we create an object
of an Abstract Class?

No.

----------------------------------------------------------

Q6. Can a Child Class skip
an Abstract Method?

No.

Every child class must implement
all abstract methods.

==========================================================
                Summary
==========================================================

Abstraction
-----------
Hide implementation.

Show only essential functionality.

Abstract Class
--------------
Created using ABC.

Abstract Method
---------------
Created using @abstractmethod.

Object Creation
---------------
❌ Cannot create object
of Abstract Class.

Child Class
-----------
Must implement all Abstract Methods.

Benefits
--------
✔ Security

✔ Less Complexity

✔ Easy Maintenance

✔ Cleaner Code

==========================================================
"""