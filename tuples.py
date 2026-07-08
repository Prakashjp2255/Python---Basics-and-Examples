###############################################################################
#                              PYTHON TUPLES
###############################################################################

# A tuple is an ordered collection of items.
#
# - Tuples maintain the order of elements.
# - Tuples are immutable, which means their values
#   cannot be modified after creation.
# - Tuples allow duplicate values.
# - Tuples can store multiple data types.

trip = (
    "Kanyakumari",
    "Sivakasi",
    "Thiruthangal",
    "Rajapalayam",
    "Sivakasi"
)

print("Trip Locations:", trip)


###############################################################################
# ACCESSING ELEMENTS
###############################################################################

# Access an element using its index.

position = trip[2]

print("Third Location:", position)

# Output:
# Third Location: Thiruthangal


###############################################################################
# LENGTH OF A TUPLE
###############################################################################

length = len(trip)

print("Total Locations:", length)

# Output:
# Total Locations: 5


###############################################################################
# count()
###############################################################################

# count() returns how many times a value appears.

counts = trip.count("Sivakasi")

print("Count:", counts)

# Output:
# Count: 2


###############################################################################
# index()
###############################################################################

# index() returns the first occurrence of an element.

index_value = trip.index("Rajapalayam")

print("Index:", index_value)

# Output:
# Index: 3


###############################################################################
# TUPLE SLICING
###############################################################################

print("First Two Locations:", trip[:2])

print("Last Two Locations:", trip[-2:])

# Output:
# First Two Locations:
# ('Kanyakumari', 'Sivakasi')
#
# Last Two Locations:
# ('Rajapalayam', 'Sivakasi')


###############################################################################
# ITERATING THROUGH A TUPLE
###############################################################################

for location in trip:
    print(location)

# Output:
# Kanyakumari
# Sivakasi
# Thiruthangal
# Rajapalayam
# Sivakasi


###############################################################################
# MEMBERSHIP OPERATOR
###############################################################################

# Check whether an element exists.

if "Sivakasi" in trip:
    print("Location Found")

# Output:
# Location Found


###############################################################################
# TUPLE UNPACKING
###############################################################################

city1, city2, city3, city4, city5 = trip

print(city1)
print(city2)

# Output:
# Kanyakumari
# Sivakasi


###############################################################################
# SINGLE ELEMENT TUPLE
###############################################################################

# A comma is mandatory for a single-element tuple.

single = ("Python",)
print(type(single))

# Output:
# <class 'tuple'>


###############################################################################
# WHY TUPLES ARE IMMUTABLE?
###############################################################################

# Tuples do not allow item assignment.

# trip[1] = "Karur"

"""
Error:

TypeError:
'tuple' object does not support item assignment

Reason:
-------
A tuple is immutable.
Once created, its elements cannot be changed,
added, or removed.
"""


###############################################################################
# MODIFYING A TUPLE (WORKAROUND)
###############################################################################

# Convert the tuple into a list,
# modify it, then convert it back to a tuple.

trip_list = list(trip)

trip_list[1] = "Karur"

trip = tuple(trip_list)

print(trip)

# Output:
# ('Kanyakumari', 'Karur', 'Thiruthangal',
#  'Rajapalayam', 'Sivakasi')


###############################################################################
# QUICK REVISION
###############################################################################

# Tuple
# -----
# Ordered collection.
# Immutable.
# Allows duplicate values.

# len()
# -----
# Returns the total number of elements.

# count()
# -------
# Counts how many times an element appears.

# index()
# -------
# Returns the index of the first occurrence.

# slicing
# -------
# tuple[start:end]

# in
# --
# Checks whether an element exists.

# unpacking
# ---------
# Assigns tuple values to multiple variables.

# list() and tuple()
# ------------------
# Used to convert between a list and a tuple.