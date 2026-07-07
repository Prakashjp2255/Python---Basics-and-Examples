a =  "10"
b = 11.0
c = True 
d = c + b 
e = "Hello hi"

print(int(e)) # It will throw an error because e is a string and cannot be converted to an integer  
                         
"""
  File "c:\Xyz\Python - Basics\typeCasting.py", line 7, in <module>
    print(int(e)) # It will throw an error because e is a string and cannot be converted to an integer
          ~~~^^^
ValueError: invalid literal for int() with base 10: 'Hello hi'
"""

print(d) # It will print 12.0 because c is converted to 1 and added to b
print(int(c)) # It will print 1 because c is converted to an integer
print(int(a)) # It will print 10 because a is converted to an integer
print(int(b)) # It will print 11 because b is converted to an integer
print(str(b)) # It will print "11.0" because b is converted to a string

