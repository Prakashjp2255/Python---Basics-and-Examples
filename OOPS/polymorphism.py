"""
==========================================================
                 Polymorphism in Python
==========================================================

Definition:
-----------
Polymorphism is one of the four main OOP principles.

The word "Polymorphism" comes from two Greek words:

    Poly  -> Many
    Morph -> Forms

Meaning:
--------
One method can have many forms.

In Python, different classes can have methods
with the same name but different implementations.

==========================================================
                Real-Time Example
==========================================================

Think about the "Speak" action.

Dog  -> Woof
Cat  -> Meow
Cow  -> Moo

Every animal can "speak",
but each animal speaks differently.

This is called Polymorphism.

==========================================================
                Example 1
        Same Method, Different Classes
==========================================================
"""


class Dog:

    def speak(self):
        print("Dog says Woof!")


class Cat:

    def speak(self):
        print("Cat says Meow!")


class Cow:

    def speak(self):
        print("Cow says Moo!")


print("========== Example 1 ==========")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()

"""
Output

Dog says Woof!
Cat says Meow!
Cow says Moo!

Explanation:
-------------
All three classes have a method called speak().

Although the method name is the same,
each class behaves differently.

This is Polymorphism.
"""

print()

"""
==========================================================
                Example 2
            Method Overriding
==========================================================
"""


class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        print("Dog says Woof!")


class Cat(Animal):

    def speak(self):
        print("Cat says Meow!")


print("========== Example 2 ==========")

d = Dog()
c = Cat()

d.speak()
c.speak()

"""
Output

Dog says Woof!
Cat says Meow!

Explanation:
-------------
Dog and Cat inherit from Animal.

Each class overrides the Parent's speak() method.

This is Runtime Polymorphism.

"""

print()

"""
==========================================================
                Example 3
            Polymorphism Using Loop
==========================================================
"""


class Dog:

    def speak(self):
        print("Woof!")


class Cat:

    def speak(self):
        print("Meow!")


class Cow:

    def speak(self):
        print("Moo!")


animals = [Dog(), Cat(), Cow()]

print("========== Example 3 ==========")

for animal in animals:
    animal.speak()

"""
Output

Woof!
Meow!
Moo!

Explanation:
-------------
The loop doesn't care which object it receives.

It simply calls:

animal.speak()

Each object performs its own implementation.

This is one of the biggest advantages
of Polymorphism.

"""

print()

"""
==========================================================
                Example 4
        Polymorphism with Function
==========================================================
"""


class Dog:

    def speak(self):
        print("Woof!")


class Cat:

    def speak(self):
        print("Meow!")


def make_sound(animal):
    animal.speak()


print("========== Example 4 ==========")

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

"""
Output

Woof!
Meow!

Explanation:
-------------
The function accepts any object.

As long as the object has a speak() method,
the function works.

This is called Duck Typing in Python.

"If it walks like a duck and quacks like a duck,
Python treats it like a duck."

"""

print()

"""
==========================================================
        Compile-Time vs Runtime Polymorphism
==========================================================

1. Compile-Time Polymorphism

Examples:
---------
Method Overloading

Python does NOT support true method overloading
like Java or C++.

Instead, Python uses:
    - Default Arguments
    - *args
    - **kwargs

----------------------------------------------------------

2. Runtime Polymorphism

Achieved using Method Overriding.

Example:

Parent Class
-------------
Animal

Child Class
------------
Dog

Both contain:

speak()

The Child class provides its own implementation.

==========================================================
                Advantages
==========================================================

✔ Code Reusability

✔ Easy Maintenance

✔ Flexible Code

✔ Better Readability

✔ Easy to Extend

✔ Supports Dynamic Programming

==========================================================
                Interview Questions
==========================================================

Q1. What is Polymorphism?

Polymorphism means
"One interface, many implementations."

----------------------------------------------------------

Q2. Why do we use Polymorphism?

To write flexible and reusable code.

----------------------------------------------------------

Q3. What is Method Overriding?

When a Child class provides its own implementation
of a Parent class method.

----------------------------------------------------------

Q4. Does Python support Method Overloading?

No.

Python uses:
    Default Parameters
    *args
    **kwargs

instead of true Method Overloading.

----------------------------------------------------------

Q5. What is Duck Typing?

If an object has the required method,
Python allows it to be used,
regardless of its class.

==========================================================
                    Summary
==========================================================

Polymorphism
------------
One method
Many implementations

Method Overriding
-----------------
Child class replaces Parent method.

Duck Typing
-----------
Python checks the object's behavior,
not its type.

Benefits
--------
✔ Flexible Code

✔ Reusable Code

✔ Easy Maintenance

✔ Dynamic Behavior

==========================================================
"""