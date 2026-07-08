###############################################################################
#                           PYTHON FUNCTIONS
###############################################################################

# ============================================================================
# 1. Importing a Function from Another File
# ============================================================================

# Import the function 'imp' from the file 'func_import.py'.

from func_import import imp

result = imp(99, 88)
print(result)


###############################################################################
# 2. Function Without Parameters
###############################################################################

# A simple function that prints a greeting message.

def hello():
    print("Hello!")

# Calling the function.
hello()

# Output:
# Hello!


###############################################################################
# 3. Function With Parameters
###############################################################################

# Parameters are variables defined in the function definition.
# They receive values when the function is called.

def greet(name):
    print(f"Your name is {name}")

# If you call the function without an argument,
# Python throws the following error:

# greet()

# TypeError:
# greet() missing 1 required positional argument: 'name'

# Correct way
greet("Prakash")

# Output:
# Your name is Prakash


###############################################################################
# 4. Function With Multiple Parameters
###############################################################################

# Arguments are the actual values passed to a function.

def multiply(a, b):
    print(a * b)

multiply(99, 99)

# Output:
# 9801


###############################################################################
# 5. Function Using return
###############################################################################

# return sends the result back to the function caller.
# We use return when we want to store the result
# in another variable or use it later in the program.

def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(8, 9)

print(result)

# Output:
# 72


###############################################################################
# Difference Between print() and return()
###############################################################################

# print()
# -------
# Displays the result on the screen only.

# return
# -------
# Sends the value back to the caller.
# The returned value can be stored in a variable,
# passed to another function, or used in calculations.

# Example:

value = multiply_numbers(5, 10)

print(value)

# Output:
# 50


###############################################################################
# 6. *args (Variable-Length Positional Arguments)
###############################################################################

# *args allows a function to accept any number of positional arguments.
# Inside the function, args is stored as a tuple.

def add_numbers(*args):

    total = 0

    for number in args:
        total += number

    return total

print(add_numbers(1, 2, 3))

# Output:
# 6

print(add_numbers(10, 20, 30, 40, 50))

# Output:
# 150


###############################################################################
# 7. **kwargs (Variable-Length Keyword Arguments)
###############################################################################

# **kwargs allows a function to accept any number
# of keyword arguments.

# Inside the function, kwargs is stored as a dictionary.

def create_profile(**kwargs):

    print("User Profile")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(
    name="Prakash",
    job="Engineer",
    age=19
)

# Output:
# User Profile
# name: Prakash
# job: Engineer
# age: 19


###############################################################################
# QUICK REVISION
###############################################################################

# Function
# --------
# A function is a reusable block of code that performs a specific task.

# Syntax:
#
# def function_name():
#     statements


# Parameters
# ----------
# Variables defined in the function declaration.
#
# Example:
#
# def greet(name):
#     print(name)


# Arguments
# ---------
# Actual values passed when calling the function.
#
# Example:
#
# greet("Prakash")
#
# "Prakash" is the argument.


# return
# ------
# Returns a value from a function.
#
# Example:
#
# def add(a, b):
#     return a + b


# *args
# -----
# Accepts any number of positional arguments.
#
# Example:
#
# add_numbers(1, 2, 3, 4, 5)


# **kwargs
# --------
# Accepts any number of keyword arguments.
#
# Example:
#
# create_profile(
#     name="Prakash",
#     age=22,
#     city="Chennai"
# )