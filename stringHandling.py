
##############################################################################

### WE HAVE SEE THE STRING HANDLING........

Name = "prakash muthusamy " 
print( "Capitalize : " +  Name.capitalize())
print( "Lower :" + Name.lower())
print( "Upper : " + Name.upper())

mobile_no = "9876543210" 
mask = mobile_no[:3] + "*****" + mobile_no[-2:] 
print("The masked No: " + mask)


song = "shape OF yOu" 
artist = "ED SHERAN ed"
formatted = f"{song.title()} - {artist.title()}"  
print("Formatted: " + formatted)

location = "chennai tambaram" 
fixed_location = location.replace("chennai tamabaram" , "EGMORE")
print(fixed_location) 

message = "Your UBER booking id is : UBER1234. Please keep it safe " 
booking_id = message.split(":")[1] ##O/P -->  UBER1234. Please keep it safe  
booking_id_1 = message.split(":")[1].split("l")[1]
booking_id_2 = message.split(":")[1].split(".")[0].strip() 
print(booking_id) 
print(booking_id_1)
print(booking_id_2) 

# ============================================================
#               PYTHON STRING METHODS - REAL-TIME EXAMPLES
# ============================================================

# ------------------------------------------------------------
# 1. Check whether a substring exists using the 'in' operator
# ------------------------------------------------------------

promo_msg = "Use Zomato 100 to get the offer"

# The 'in' operator checks whether a particular text
# is present inside another string.
if "Zomato 100" in promo_msg:
    print("The offer is applied.")

# Output:
# The offer is applied.


# ============================================================
# 2. Find the position of a substring using find()
# ============================================================

feedback = "The driver was polite and the ride was smooth"

# find() returns the starting index of the given word.
# If the word is not found, it returns -1.

print("Position:", feedback.find("polite"))

# Output:
# Position: 15


# ============================================================
# 3. Generate initials from a full name
# ============================================================

name = "jayaprakash muthusamy"

# split() converts the string into a list.
# ['jayaprakash', 'muthusamy']

# word[0] gets the first letter of each word.

# upper() converts the letter to uppercase.

# join() combines all initials using a space.

initials = " ".join([word[0].upper() for word in name.split()])

print("Initials:", initials)

# Output:
# Initials: J M

# ============================================================
# 4. Remove unwanted spaces using strip()
# ============================================================

dirty_input = "     airport      "

# strip() removes only the spaces at the beginning
# and at the end of the string.

clean = dirty_input.strip()

print(clean)

# Output:
# airport


# ============================================================
# 5. Count the total number of words
# ============================================================

sentence = "The trip is so good and I learned some new things"

# split() converts the sentence into words.
# len() counts the total number of words.

word_count = len(sentence.split())

print("Word Count:", word_count)

# Output:
# Word Count: 10


# ============================================================
# 6. Extract data from a sentence using split()
# ============================================================

text = "Hoi Hoi this is a Prakash and the ID is ALPHAET1123 and it was working"

# ------------------------------------------------------------
# Method 1 (Wrong Approach)
# ------------------------------------------------------------

# Here we split using "is".
# This is NOT recommended because the word "this"
# also contains "is".

wrong_output = text.split("is")[1].split("and")[0]

print("Wrong Output:", wrong_output)

# Output:
# Wrong Output:
#
# (It prints only an empty/blank string because split("is")
# splits at every occurrence of "is", including inside "this".)


# ------------------------------------------------------------
# Let's understand what actually happens
# ------------------------------------------------------------

print(text.split("is"))

# Output:
# ['Hoi Hoi th',
#  ' ',
#  ' a Prakash and the ID ',
#  ' ALPHAET1123 and it was working']

# "is" appears in:
#
# this
# is
# ID is
#
# Therefore, Python splits at ALL occurrences.


# ------------------------------------------------------------
# Method 2 (Correct Approach)
# ------------------------------------------------------------

# Instead of splitting by "is",
# split using a unique text like "ID is".

coupon = text.split("ID is")[1].split("and")[0].strip()

print("Coupon Code:", coupon)

# Output:
# Coupon Code: ALPHAET1123


# ============================================================
# 7. Find the position of the coupon code
# ============================================================

# find() returns the starting position of the coupon.

position = text.find("ALPHAET1123")

print("Coupon Position:", position)

# Output:
# Coupon Position: 39


# ============================================================
# IMPORTANT INTERVIEW NOTE
# ============================================================

sample = "this is Python"

print(sample.split("is"))

# Output:
# ['th', ' ', ' Python']

# Why?
#
# Because "is" exists in:
#
# th(is)
# (is)

print(sample.split(" is "))

# Output:
# ['this', 'Python']

# Notice the difference:
#
# split("is")
# → Splits EVERY occurrence of "is".
#
# split(" is ")
# → Splits only the word "is" (with spaces around it).


# ============================================================
# QUICK REVISION
# ============================================================

# in
# ----
# Checks whether a substring exists.
#
# Example:
# "Python" in "I love Python"
# Output: True


# find()
# ------
# Returns the index of a substring.
# Returns -1 if not found.
#
# Example:
# "Python".find("th")
# Output: 2


# split()
# -------
# Splits a string into a list.
#
# Example:
# "A B C".split()
# Output:
# ['A', 'B', 'C']


# join()
# ------
# Combines a list of strings into a single string.
#
# Example:
# "-".join(["A", "B", "C"])
#
# Output:
# A-B-C


# strip()
# -------
# Removes leading and trailing spaces.
#
# Example:
# "   Hello   ".strip()
#
# Output:
# Hello


# len()
# -----
# Returns the total number of characters
# or the total number of items in a list.
#
# Example:
# len("Python")
#
# Output:
# 6