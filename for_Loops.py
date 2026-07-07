###############################################################################
#                           PYTHON LOOPS
#                    for loop | while loop | break
#                    continue | pass
###############################################################################

# ============================================================================
# 1. FOR LOOP
# ============================================================================

# A for loop is used to iterate through each item in a list, tuple, string,
# dictionary, or any iterable object.

names = [" prakash ", " Muthusamy ", " sakthi ", " hema "]

for name in names:
    # strip() removes unwanted spaces.
    # upper() converts the text to uppercase.
    print(name.strip().upper())

# Output:
# PRAKASH
# MUTHUSAMY
# SAKTHI
# HEMA


###############################################################################

# ============================================================================
# 2. WHILE LOOP
# ============================================================================

# A while loop keeps executing as long as the condition is True.

correct_pin = "8808"
entered_pin = ""

# Keep asking for the PIN until the correct PIN is entered.

while correct_pin != entered_pin:
    entered_pin = input("Enter your PIN: ")

print("Access Granted")

# Sample Output:
#
# Enter your PIN: 1234
# Enter your PIN: 5678
# Enter your PIN: 8808
# Access Granted


###############################################################################

# ============================================================================
# 3. BREAK STATEMENT
# ============================================================================

# break immediately exits the loop when the condition becomes True.

for i in range(10):

    if i == 7:
        break

    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6


###############################################################################

# Another Example

numbers = [1, 2, 3, 4, 5, 6, 7]

for j in numbers:

    if j == 3:
        break

    print(j)

# Output:
# 1
# 2


###############################################################################

# ============================================================================
# 4. CONTINUE STATEMENT
# ============================================================================

# continue skips the current iteration and moves to the next iteration.

arr = [2, 3, 4, 4, 6, 8, 9, -10]

for value in arr:

    if value <= 0:
        continue

    print(value)

# Output:
# 2
# 3
# 4
# 4
# 6
# 8
# 9


###############################################################################

# ============================================================================
# 5. PASS STATEMENT
# ============================================================================

# pass is a placeholder.
# It is used when you want to leave the block empty
# and implement the logic later.

for value in arr:
    pass

# Nothing is printed because pass does nothing.


###############################################################################

# ============================================================================
# 6. WHILE LOOP - Countdown Example
# ============================================================================

count = 5

# Keep running while count is greater than zero.

while count > 0:

    print(f"Countdown: {count}")

    count -= 1

print("Time is up!")

# Output:
# Countdown: 5
# Countdown: 4
# Countdown: 3
# Countdown: 2
# Countdown: 1
# Time is up!


###############################################################################

# ============================================================================
# 7. WHILE TRUE + BREAK
# ============================================================================

# This program keeps accepting items until the user types "done".

items = []

while True:

    item = input("Enter an item (type 'done' to stop): ")

    # lower() converts the input to lowercase
    # so Done, DONE, done all work the same.

    if item.lower() == "done":
        break

    items.append(item)

print("Items in Cart:", items)

# Sample Output:
#
# Enter an item (type 'done' to stop): Apple
# Enter an item (type 'done' to stop): Mango
# Enter an item (type 'done' to stop): Orange
# Enter an item (type 'done' to stop): done
#
# Items in Cart:
# ['Apple', 'Mango', 'Orange']


###############################################################################
#                             QUICK REVISION
###############################################################################

# for loop
# --------
# Used when you know how many items you want to iterate over.

# Example:
#
# for item in items:
#     print(item)


# while loop
# ----------
# Used when you don't know how many times the loop should run.
# It continues until the condition becomes False.

# Example:
#
# while condition:
#     statement


# break
# -----
# Immediately exits the loop.

# Example:
#
# for i in range(10):
#     if i == 5:
#         break


# continue
# --------
# Skips the current iteration and continues with the next one.

# Example:
#
# for i in range(5):
#     if i == 2:
#         continue


# pass
# ----
# Placeholder for future code.
# It does nothing.

# Example:
#
# if True:
#     pass


# while True
# ----------
# Creates an infinite loop.
# Usually combined with break to exit when required.

# Example:
#
# while True:
#     if condition:
#         break