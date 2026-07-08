###############################################################################
#                               PYTHON LISTS
###############################################################################

# A list is an ordered collection of items.
#
# - Lists maintain the order of elements.
# - Lists are mutable, which means we can add, remove,
#   update, or modify elements after creation.
# - List elements are accessed using their index.

playlist = ["Shape of You", "Naa Ready", "Kala Makkara", "Kalyani"]
favourite_food = [ "Chicken Biriyani","Shawarma", "Egg Noodles" ]
recent_locations = ["Home", "Airport", "Work", "Zoo" ]

print("Spotify Playlist:", playlist)
print("Favourite Foods:", favourite_food)
print("Recent Locations:", recent_locations)


###############################################################################
#                           LIST METHODS
###############################################################################

# append()
# --------
# Adds a new element to the end of the list.

playlist.append("Oo Antava")
print("After append():", playlist)


###############################################################################

# insert()
# --------
# Inserts an element at a specific index.

playlist.insert(1, "Rathinamo")
print("After insert():", playlist)


###############################################################################

# remove()
# --------
# Removes the first matching element from the list.

playlist.remove("Kala Makkara")
print("After remove():", playlist)


###############################################################################

# pop()
# -----
# Removes the last element by default.
# You can also pass an index.

favourite_food.pop()
print("After pop():", favourite_food)


###############################################################################

# reverse()
# ---------
# Reverses the order of the list.

playlist.reverse()
print("After reverse():", playlist)


###############################################################################

# count()
# -------
# Returns how many times an element appears in the list.

print("Count:", playlist.count("Kala Makkara"))

# Output:
# Count: 0

# Why is the output 0?
#
# Because "Kala Makkara" was already removed using:
#
# playlist.remove("Kala Makkara")
#
# Therefore, it no longer exists in the list.


###############################################################################
# Example of count()
###############################################################################

# Example 1

songs = [
    "Shape of You",
    "Naa Ready",
    "Kala Makkara",
    "Kalyani"
]

print(songs.count("Kala Makkara"))

# Output:
# 1


# Example 2

songs = [
    "Shape of You",
    "Kala Makkara",
    "Naa Ready",
    "Kala Makkara",
    "Kalyani",
    "Kala Makkara"
]

print(songs.count("Kala Makkara"))

# Output:
# 3


# Example 3

print(songs.count("Leo"))

# Output:
# 0


###############################################################################
# LIST SLICING
###############################################################################

# List slicing is used to retrieve a portion of the list.

print("Top 2 Songs:", playlist[:2])

print("Last 2 Songs:", playlist[-2:])

print("Last 2 Locations:", recent_locations[-2:])


###############################################################################
# LIST ITERATION
###############################################################################

# Loop through each food item.

for food in favourite_food:
    print("Food:", food)

# Loop through each song.

for song in playlist:
    print(song + " - By Prakash")


###############################################################################
# CHECK WHETHER AN ITEM EXISTS
###############################################################################

# The 'in' operator checks whether an element
# exists inside the list.

if "Shawarma" in favourite_food:
    print("Yes, Shawarma is available.")

# Output:
# Yes, Shawarma is available.


###############################################################################
# UPDATE AN ELEMENT
###############################################################################

# Lists are mutable.
# We can change an element using its index.

favourite_food[1] = "Dosa"

print("Updated Food List:", favourite_food)


###############################################################################
# LIST WITH MULTIPLE DATA TYPES
###############################################################################

# A list can store different data types.

mixed = [
    "Prakash",
    99.0,
    88,
    True
]

print("Mixed List:", mixed)


###############################################################################
# ENUMERATE
###############################################################################

# enumerate() returns both the index and the value.

for index, food in enumerate(favourite_food):

    print(f"Index: {index} | Food: {food}")

# Output:
# Index: 0 | Food: Chicken Biriyani
# Index: 1 | Food: Dosa
# Index: 2 | Food: Egg Noodles


###############################################################################
# QUICK REVISION
###############################################################################

# append(item)
# ------------
# Adds an item to the end of the list.

# insert(index, item)
# -------------------
# Inserts an item at a specific position.

# remove(item)
# ------------
# Removes the first matching element.

# pop()
# -----
# Removes and returns the last element.

# reverse()
# ---------
# Reverses the list.

# count(item)
# -----------
# Returns how many times an item appears.

# index(item)
# -----------
# Returns the position of the first occurrence.

# slicing
# -------
# list[start:end]

# Example:
#
# numbers = [10, 20, 30, 40, 50]
#
# numbers[:2]
# Output:
# [10, 20]
#
# numbers[-2:]
# Output:
# [40, 50]

# enumerate()
# -----------
# Returns both the index and the value while looping.

# Example:
#
# for index, value in enumerate(list_name):
#     print(index, value)