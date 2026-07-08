###############################################################################
#                           PYTHON DICTIONARIES
###############################################################################

# A dictionary is a collection of key-value pairs.
#
# Characteristics:
# - Stores data as key : value pairs.
# - Mutable (can add, update, and remove elements).
# - Keys must be unique.
# - Values can be duplicated.
# - Dictionaries maintain insertion order (Python 3.7+).

###############################################################################
# CREATING A DICTIONARY
###############################################################################

employee = {
    "id": 101,
    "name": "Prakash",
    "role": "Python Developer",
    "salary": 50000
}

print(employee)

# Output:
# {
#   'id': 101,
#   'name': 'Prakash',
#   'role': 'Python Developer',
#   'salary': 50000
# }


###############################################################################
# ACCESSING VALUES
###############################################################################

# Access a value using its key.

print(employee["name"])

# Output:
# Prakash

print(employee["salary"])

# Output:
# 50000


###############################################################################
# get()
###############################################################################

# get() is used to retrieve a value safely.
# If the key does not exist, it returns None instead of throwing an error.

print(employee.get("role"))

# Output:
# Python Developer

print(employee.get("city"))

# Output:
# None


###############################################################################
# ADDING A NEW KEY-VALUE PAIR
###############################################################################

employee["city"] = "Chennai"

print(employee)

# Output:
# {
#   'id': 101,
#   'name': 'Prakash',
#   'role': 'Python Developer',
#   'salary': 50000,
#   'city': 'Chennai'
# }


###############################################################################
# UPDATING A VALUE
###############################################################################

employee["salary"] = 65000

print(employee)

# Output:
# Salary becomes 65000


###############################################################################
# REMOVE USING pop()
###############################################################################

# pop() removes a key and returns its value.

employee.pop("city")

print(employee)

# Output:
# city is removed


###############################################################################
# REMOVE USING del
###############################################################################

# del deletes a key completely.

del employee["role"]

print(employee)

# Output:
# role is removed


###############################################################################
# LENGTH
###############################################################################

print("Total Keys:", len(employee))

# Output:
# Total Keys: 3


###############################################################################
# KEYS
###############################################################################

print(employee.keys())

# Output:
# dict_keys(['id', 'name', 'salary'])


###############################################################################
# VALUES
###############################################################################

print(employee.values())

# Output:
# dict_values([101, 'Prakash', 65000])


###############################################################################
# ITEMS
###############################################################################

# items() returns both key and value.

print(employee.items())

# Output:
# dict_items([
# ('id',101),
# ('name','Prakash'),
# ('salary',65000)
# ])


###############################################################################
# ITERATING THROUGH A DICTIONARY
###############################################################################

for key, value in employee.items():

    print(f"{key} : {value}")

# Output:
#
# id : 101
# name : Prakash
# salary : 65000


###############################################################################
# CHECK WHETHER A KEY EXISTS
###############################################################################

if "name" in employee:

    print("Name key exists.")

# Output:
# Name key exists.


###############################################################################
# COPY
###############################################################################

employee_copy = employee.copy()

print(employee_copy)


###############################################################################
# CLEAR
###############################################################################

temp = employee.copy()

temp.clear()

print(temp)

# Output:
# {}


###############################################################################
# NESTED DICTIONARY
###############################################################################

student = {

    "name": "Prakash",

    "marks": {
        "Python": 95,
        "Java": 90,
        "SQL": 88
    }
}

print(student["marks"]["Python"])

# Output:
# 95


###############################################################################
# DICTIONARY COMPREHENSION
###############################################################################

numbers = {
    x: x * x
    for x in range(1, 6)
}

print(numbers)

# Output:
# {
# 1:1,
# 2:4,
# 3:9,
# 4:16,
# 5:25
# }




###############################################################################
# ITERATING THROUGH A DICTIONARY
###############################################################################

# ❌ Wrong Way

# for key, value in employee:
#     print(key, value)

"""
Error:

ValueError:
too many values to unpack (expected 2)

Reason:
-------
Iterating directly over a dictionary returns ONLY the keys.

Python treats it like this:

for key in employee:
    print(key)

Output:
id
name
role
salary

Since each key is a string, Python tries to unpack the string
into two variables (key, value), which causes the error.
"""


# ✅ Correct Way

# Use items() to retrieve both keys and values.

for key, value in employee.items():
    print(f"{key}: {value}")

# Output:
# id: 101
# name: Prakash
# role: Python Developer
# salary: 50000




###############################################################################
# QUICK REVISION
###############################################################################

# dict()
# ------
# Creates a dictionary.

# get()
# -----
# Returns the value safely.
# Returns None if the key is not found.

# pop()
# -----
# Removes a key and returns its value.

# del
# ---
# Deletes a key permanently.

# keys()
# ------
# Returns all keys.

# values()
# --------
# Returns all values.

# items()
# -------
# Returns both keys and values.

# copy()
# -------
# Creates a copy of the dictionary.

# clear()
# --------
# Removes all elements.

# in
# --
# Checks whether a key exists.

###############################################################################
# IMPORTANT INTERVIEW QUESTIONS
###############################################################################

# Difference between [] and get()

employee = {
    "name": "Prakash"
}

# Using []

# print(employee["city"])

"""
Error:

KeyError: 'city'

Reason:
-------
The key does not exist.
"""


# Using get()

print(employee.get("city"))

# Output:
# None

# Therefore,
#
# []  -> Throws KeyError if the key is missing.
#
# get()
# -> Returns None (or a default value) if the key is missing.


###############################################################################
# Difference between List, Tuple, Set and Dictionary
###############################################################################

# List
# ----
# Ordered
# Mutable
# Duplicate values allowed

# Tuple
# -----
# Ordered
# Immutable
# Duplicate values allowed

# Set
# ---
# Unordered
# Mutable
# No duplicate values

# Dictionary
# ----------
# Key-Value pairs
# Mutable
# Keys must be unique
# Values can be duplicated