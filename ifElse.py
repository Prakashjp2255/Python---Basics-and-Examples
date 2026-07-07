###############################################################################
#                     Python if, elif, else Examples
###############################################################################

# ============================================================================
# 1. Example - Simple if...else
# ============================================================================

age = 30

# Check whether the person is eligible to vote.
# If the age is 18 or above, the person can vote.
# Otherwise, they are not eligible.

if age >= 18:
    print("Yes, you are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Output:
# Yes, you are eligible to vote.


###############################################################################

# ============================================================================
# 2. Example - if...elif...else
# ============================================================================

marks = 100

# The conditions are checked from top to bottom.
# As soon as one condition becomes True,
# Python skips the remaining conditions.

if marks >= 95:
    print("Grade: Excellent++")

elif marks >= 90:
    print("Grade: Excellent")

elif marks >= 70:
    print("Grade: Average")

elif marks >= 50:
    print("Grade: Average+")

elif marks >= 35:
    print("Grade: Just Pass")

else:
    print("Grade: Fail")

# Output:
# Grade: Excellent++


###############################################################################

# ============================================================================
# 3. Example - Nested if Statement
# ============================================================================

age = 18
has_license = "No"

# First, check the person's age.
# If the age condition is satisfied,
# then check whether they have a driving license.

if age >= 18:

    if has_license == "Yes":
        print("Yes, you can drive a car.")

    else:
        print("You are eligible by age, but you need a driving license.")

else:
    print("You are too young to drive.")

# Output:
# You are eligible by age, but you need a driving license.


###############################################################################

# ============================================================================
# 4. Example - Logical OR Operator
# ============================================================================

marks = 80
attendance = 20

# The student is allowed if
# either the marks are 55 or above
# OR the attendance is 70% or above.

if marks >= 55 or attendance >= 70:
    print("Yes, you are allowed to attend the exam.")
else:
    print("You are not allowed to attend the exam.")

# Output:
# Yes, you are allowed to attend the exam.


###############################################################################

# ============================================================================
# 5. Example - Recharge Offer
# ============================================================================

recharge_amount = 399
data_balance = 1.5

# The user is eligible if
# recharge amount is at least ₹399
# OR the remaining data balance is at least 1.5 GB.

if recharge_amount >= 399 or data_balance >= 1.5:
    print("You are eligible for bonus data.")
else:
    print("You are not eligible for bonus data.")

# Output:
# You are eligible for bonus data.


###############################################################################

# ============================================================================
# 6. Example - AND + OR Operators
# ============================================================================

ordered_amount = 1044
special_day = "sat"
gold_member = "yes"

# Discount Rules:
#
# Rule 1:
# Order amount should be greater than ₹1000
# AND today should be Saturday or Sunday.
#
# OR
#
# Rule 2:
# The customer is a Gold Member.
#
# If either rule is satisfied,
# the customer gets a 20% discount.

if (ordered_amount > 1000 and special_day in ["sat", "sun"]) or gold_member == "yes":

    discount = ordered_amount * 0.20

    # Convert the float value to a string using str()
    # or use an f-string (recommended).

    print("Your discount amount: " + str(discount))

    # Better way:
    # print(f"Your discount amount: {discount}")

else:
    print("OOPS!! You don't have any discounts.")

# Output:
# Your discount amount: 208.8


###############################################################################
# Important Note
###############################################################################

"""
Common Beginner Mistake

❌ Wrong:

print("Your discount amount: " + discount)

Error:

TypeError:
can only concatenate str (not "float") to str

Reason:
-------
The '+' operator can only join strings.

Here:
"Your discount amount: "  --> String
discount                  --> Float

Python cannot concatenate a string with a float.

Correct Ways:

1.
print("Your discount amount: " + str(discount))

2.
print("Your discount amount:", discount)

3. (Recommended)
print(f"Your discount amount: {discount}")
"""