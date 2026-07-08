###############################################################################
#                               PYTHON SETS
###############################################################################

# A set is an unordered collection of unique elements.
#
# Characteristics:
# - Does NOT allow duplicate values.
# - Unordered (elements do not have an index).
# - Mutable (you can add or remove elements).
# - Faster for searching compared to lists.

###############################################################################
# REMOVING DUPLICATES
###############################################################################

numbers = [99, 88, 99]

# Convert the list into a set.
# Duplicate values are automatically removed.

unique_numbers = set(numbers)

print(unique_numbers)

# Output:
# {88, 99}


###############################################################################
# DUPLICATES ARE IGNORED
###############################################################################

values = {99, 8, 8}

print(values)

# Output:
# {8, 99}

# The duplicate value 8 is stored only once.


###############################################################################
# CONVERTING LISTS TO SETS
###############################################################################

uber_cities = [
    "Chennai",
    "Bangalore",
    "Mumbai"
]

uber_cities2 = [
    "Bangkok",
    "Bangalore",
    "Abu Dhabi"
]

unique1 = set(uber_cities)
unique2 = set(uber_cities2)

print("Cities 1:", unique1)
print("Cities 2:", unique2)


###############################################################################
# UNION
###############################################################################

# Combines all unique elements from both sets.

print("Union:")

print(unique1.union(unique2))

# Output:
# {
# 'Chennai',
# 'Bangalore',
# 'Mumbai',
# 'Bangkok',
# 'Abu Dhabi'
# }


###############################################################################
# INTERSECTION
###############################################################################

# Returns only the common elements.

print("Intersection:")

print(unique1.intersection(unique2))

# Output:
# {'Bangalore'}


###############################################################################
# DIFFERENCE
###############################################################################

# Returns the elements that exist in unique1
# but not in unique2.

print("Difference:")

print(unique1.difference(unique2))

# Output:
# {'Chennai', 'Mumbai'}


###############################################################################
# ADD
###############################################################################

# Adds a new element.

unique1.add("Karur")

print("After add():")

print(unique1)


###############################################################################
# REMOVE
###############################################################################

# remove() deletes an element.
# If the element does not exist,
# Python raises a KeyError.

# unique1.remove("Tambaram")

"""
Error:

KeyError: 'Tambaram'

Reason:
-------
'Tambaram' does not exist in the set.
"""


###############################################################################
# DISCARD
###############################################################################

# discard() removes an element if it exists.
# If it doesn't exist, NO error occurs.

unique1.discard("Tambaram")

print("After discard():")

print(unique1)


###############################################################################
# CHECK WHETHER AN ITEM EXISTS
###############################################################################

if "Chennai" in unique1:
    print("Chennai is available.")

# Output:
# Chennai is available.


###############################################################################
# ITERATING THROUGH A SET
###############################################################################

for city in unique1:
    print(city)

# Note:
# Sets are unordered, so the output order may change.


###############################################################################
# QUICK REVISION
###############################################################################

# set()
# -----
# Creates a set.

# add()
# -----
# Adds a new element.

# remove()
# --------
# Removes an element.
# Raises KeyError if the element is not found.

# discard()
# ---------
# Removes an element safely.
# Does NOT raise an error if the element is missing.

# union()
# -------
# Combines two sets.

# intersection()
# --------------
# Returns common elements.

# difference()
# ------------
# Returns elements present in the first set
# but not in the second.

# in
# --
# Checks whether an element exists.