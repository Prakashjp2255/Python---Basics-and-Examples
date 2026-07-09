"""
==========================================================
                 Encapsulation in Python
==========================================================

Definition:
-----------
Encapsulation is one of the four main OOP principles.

Encapsulation means:
    -> Combining data (variables) and methods (functions)
       into a single unit called a Class.
    -> Restricting direct access to the object's data and
       providing controlled access through methods.

In simple words:
----------------
Encapsulation = Data + Methods + Data Protection

Real-Time Example:
------------------
Think of an ATM machine.

You cannot directly modify your account balance.
Instead, you use methods like:
    - Deposit()
    - Withdraw()
    - Check Balance()

The actual balance is hidden inside the ATM system.

This is called Encapsulation.

==========================================================
                Types of Variables
==========================================================

1. Public Variable
------------------
Syntax:
    self.name

Can be accessed from anywhere.

2. Protected Variable
---------------------
Syntax:
    self._name

Single underscore (_)

Python doesn't prevent access.
It is only a convention that says:
"Don't access this variable directly."

3. Private Variable
-------------------
Syntax:
    self.__name

Double underscore (__)

Python performs Name Mangling.
The variable cannot be accessed directly outside the class.

==========================================================
                    Example 1
            Basic Encapsulation
==========================================================
"""


class Student:

    # Constructor
    def __init__(self, name, grade):

        # Public variables
        self.name = name
        self.grade = grade

    # Method
    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Student Grade: {self.grade}")


print("========== Example 1 ==========")

s1 = Student("Anna", "A")
s1.display()

"""
Output

Student Name : Anna
Student Grade: A

Explanation:
-------------
The Student class contains both:
    Data    -> name, grade
    Method  -> display()

This is the basic idea of Encapsulation.
"""

print()

"""
==========================================================
                    Example 2
               Protected Variable
==========================================================
"""


class Employee:

    def __init__(self):

        # Protected Variable
        self._salary = 50000


emp = Employee()

print("========== Example 2 ==========")
print(emp._salary)

"""
Output

50000

Explanation:
-------------
The variable starts with a single underscore (_).

It can still be accessed outside the class,
but developers understand it should not be modified directly.
"""

print()

"""
==========================================================
                    Example 3
                Private Variable
==========================================================
"""


class BankAccount:

    def __init__(self):

        # Private Variable
        self.__balance = 10000


account = BankAccount()

print("========== Example 3 ==========")

# print(account.__balance)

"""
If you uncomment the above line, Python will throw:

AttributeError:
'BankAccount' object has no attribute '__balance'

Reason:
-------
Python hides private variables using Name Mangling.
"""

print()

"""
==========================================================
                    Example 4
                Getter Method
==========================================================
"""


class Bank:

    def __init__(self):
        self.__balance = 10000

    # Getter Method
    def get_balance(self):
        return self.__balance


bank = Bank()

print("========== Example 4 ==========")
print("Balance :", bank.get_balance())

"""
Output

Balance : 10000

Explanation:
-------------
Instead of accessing __balance directly,
we use get_balance().

This provides controlled access.
"""

print()

"""
==========================================================
                    Example 5
                Setter Method
==========================================================
"""


class Account:

    def __init__(self):
        self.__balance = 10000

    # Setter Method
    def set_balance(self, balance):
        self.__balance = balance

    # Getter Method
    def get_balance(self):
        return self.__balance


acc = Account()

print("========== Example 5 ==========")

print("Old Balance :", acc.get_balance())

acc.set_balance(20000)

print("New Balance :", acc.get_balance())

"""
Output

Old Balance : 10000
New Balance : 20000

Explanation:
-------------
Setter methods allow controlled modification
of private variables.

Getter methods allow controlled reading
of private variables.
"""

print()

"""
==========================================================
            Public vs Protected vs Private
==========================================================

Public
-------
self.name

Accessible from anywhere.

Protected
----------
self._name

Accessible outside the class,
but should not be accessed directly.

Private
--------
self.__name

Cannot be accessed directly.

==========================================================
                Advantages of Encapsulation
==========================================================

✔ Combines data and methods into one class.

✔ Protects important data.

✔ Prevents accidental modification.

✔ Improves security.

✔ Improves code readability.

✔ Makes code easier to maintain.

✔ Hides implementation details.

==========================================================
                Interview Definition
==========================================================

Encapsulation is the process of wrapping
data (attributes) and methods (functions)
into a single unit called a class while
restricting direct access to the object's
data using protected and private variables.

==========================================================
                     Summary
==========================================================

1. Class contains data and methods.

2. Public Variable
       self.name

3. Protected Variable
       self._name

4. Private Variable
       self.__name

5. Getter
       Read private data.

6. Setter
       Modify private data.

7. Encapsulation improves
       Security
       Maintainability
       Readability
       Data Hiding

==========================================================
"""