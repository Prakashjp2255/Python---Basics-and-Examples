### In python, 
# the type() function is used to determine the type of an object. 
# It returns the type of the specified object. 
# Here are some examples:


x = 88 
print(type(x)) # It will print <class 'int'> because x is an integer 

y = 99.0 
print(type(y)) # It will print <class 'float'> because y is a float

z = "Hello, World!" 
print(type(z)) # It will print <class 'str'> because z is a string 

a = [1, 2, 3, 4, 5] 
print(type(a)) # It will print <class 'list'> because a is a list

b = (1, 2, 3, 4, 5) 
print(type(b)) # It will print <class 'tuple'> because b is a tuple

c = {1, 2, 3, 4, 5} 
print(type(c)) # It will print <class 'set'> because c is a set 
 
d = {'name': 'John', 'age': 30}
print(type(d)) # It will print <class 'dict'> because d is a dictionary

e = True 
print(type(e)) # It will print <class 'bool'> because e is a boolean 

f = None 
print(type(f)) # It will print <class 'NoneType'> because f is None

g = lambda x: x + 1
print(type(g)) # It will print <class 'function'> because g is a function

h = complex(1, 2)
print(type(h)) # It will print <class 'complex'> because h is a complex number 