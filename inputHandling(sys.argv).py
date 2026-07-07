
####################################################################################

# why sys.argv? 
# sys.argv is a list that stores command-line arguments passed to a Python script. 
# The first element, sys.argv[0], represents the script name, while the remaining elements are the actual arguments provided by the user. 
# These arguments are always treated as strings, so they may need to be converted to the appropriate data types when working with numbers or other values.

"""
Syntax for sys.argv in Python is:

import sys   

# Accessing command-line arguments   
arguments = sys.argv  # List of arguments   
script_name = sys.argv[0]  # Name of the script   

# Checking if an argument is provided before accessing it   
if len(sys.argv) > 1:   
  first_argument = sys.argv[1]  # First argument   
else:   
  first_argument = None  # No argument provided 

"""
################################################################################

import sys 

# if len(sys.argv == 2) : 
#     print("Usage: Python email_generator.py 'Full name and last name ' ")
#     sys.exit() 

'''
Why 3 instead of 2?

When you run:

python inputHandling(sys.argv).py jayaprakash muthusamy

sys.argv contains:

[
    "inputHandling(sys.argv).py",   # argv[0]
    "jayaprakash",                  # argv[1]
    "muthusamy"                     # argv[2]
]

So:

       len(sys.argv)

returns

3

Since you're accessing both:

sys.argv[1]
sys.argv[2]

you must ensure there are 3 elements.

'''


# Here what i mistake means len(sys.argv != 3) -->  This is wrong , len(sys.argv) !=3 
# A simple trick to remember

# ✅ len(sys.argv) != 3
# "The length of sys.argv is not equal to 3."
# ❌ len(sys.argv != 3)
# "Take the length of whether sys.argv is not equal to 3." (This doesn't make sense because the result is just True or False.)

if len(sys.argv)!= 3:  
    print("Usage: python email_generator.py <first_name> <last_name>")
    sys.exit()
    
full_name = sys.argv[1]  # Accessing the first command-line argument
last_name = sys.argv[2]  # Accessing the second command-line argument 
## Why we use sys.argv[1] instead of sys.argv[0]? 
## Because sys.argv[0] is the name of the script itself, while sys.argv[1] is the first argument provided by the user.
## python ".\inputHandling(sys.argv).py" jayaprakash muthusamy --->  like argv[1] is a jayaprakash , argv[2] is a muthusamy
email = full_name.lower().replace(" ", ".") +  last_name  +"@gcitsolutions.com"  # Generating email address

print("\n --- Your Profile Details --- \n ")
print("Full Name:", full_name)  # Printing the full name
print("Last Name:", last_name)  # Printing the last name
print("Email Address:", email)  # Printing the generated email address


################################################################################

# 1. Another method

full_name_1 = sys.argv[1:]
print(full_name_1)

# By using sys.argv[1:], we get all the command-line arguments
# starting from index 1 until the end of the list.

# Output:
# PS C:\Xyz\Python - Basics> python ".\inputHandling(sys.argv).py" jayaprakash muthusamy ss ss kk
# ['jayaprakash', 'muthusamy', 'ss', 'ss', 'kk']


# 2. Another method

full_name_2 = " ".join(sys.argv[1:])
print(full_name_2)

# The join() method combines all the arguments into a single string,
# separating each argument with a space.

# Output:
# jayaprakash muthusamy ss ss kk 

##############################################################################

''''
Explanation
sys.argv[1:] → Returns all command-line arguments except the script name.
" ".join(sys.argv[1:]) → Joins all those arguments into one string with a space between each argument.

For example:

python inputHandling.py jayaprakash muthusamy ss ss kk

sys.argv[1:] returns:

['jayaprakash', 'muthusamy', 'ss', 'ss', 'kk']

" ".join(sys.argv[1:]) returns:

jayaprakash muthusamy ss ss kk

'''
