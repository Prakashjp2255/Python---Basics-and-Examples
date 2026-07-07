# --------------------
# L --> E --> G --> B 
# --------------------

# L : Local
# E : Enclosing 
# G : Global
# B : Built-in

############################################################## 
# L -->  Local Variable : Variable defined inside a function 

def local() : 
    food = "Pizza" # Local Variable 
    print("My favorite food is " + food)

local(); # O/P:  My favorite food is Pizza 

#print (food) O/P:  NameError: name 'food' is not defined

############################################################## 

# E --> Enclosing Variable : Variable defined in the enclosing function 

# Example 1 : 
def enclosing() : 
    food = "Burger" # Enclosing Variable 
    def local() : 
        print("My favorite food is " + food)
    local()

enclosing(); # O/P:  My favorite food is Burger 

# Example 2 : 
def office() :
    employee = "Prakash" 
    def department() : 
        print ("Employee name is " + employee) 
    department() 
office(); # O/P:  Employee name is Prakash

##############################################################  

# G --> Global Variable : Variable defined outside a function 

car = " BMW" # Global Variable
def globalVar() :
    print("My favorite car is " + car)  

def globalVar1() : 
    print("I like Audi but also i like : " + car)
    
def globalVar2() : 
    print("I like Mercedes but also i like : " + car) 

globalVar(); # O/P:  My favorite car is  BMW
globalVar1(); # O/P:  I like Audi but also i like :  BMW
globalVar2(); # O/P:  I like Mercedes but also i like :  BMW

############################################################## 

# B --> Built-in Variable : Variable defined in the built-in module 

print (__file__) # It will print the path of the current file 

############################################################## 
"""
Special Built‑in Variables in Scripts
When you run a Python script, some special variables are automatically defined:

Variable	Purpose
__name__	Name of the current module ("__main__" if run directly).
__file__	Path to the current file (not available in interactive mode).
__doc__	Module’s docstring.
__package__	Package name of the module.
__loader__	Loader used to load the module.
__spec__	Module specification object.
__builtins__	Reference to the built‑in namespace.
How to See All Built‑in Names
Python

Copy code
import builtins

# List all built-in names
print(dir(builtins))
✅ Tip:
If you want to check if a name is a built‑in variable or function:

Python

Copy code
import builtins
print(hasattr(builtins, 'None'))  # True
print(hasattr(builtins, 'len'))   # True

"""
############################################################## 

## UseCase 1: 

PenDesign = "Ben 10 Designed" 

def student(): 
    item = "Pen" # Local Variable 
    def order(): 
        quantity = 10 # Local Variable 
        print("I want to buy a " + item + " with quantity " + str(quantity) + " which is " + PenDesign) # Enclosing Variable and Global Variable
        print(f"I have a {item} with quantity {quantity} which is {PenDesign}") # Enclosing Variable and Global Variable
        
    order()
student(); # O/P:  I want to buy a Pen with quantity 10 which is Ben 10 Designed 

## UseCase 2: 

River = "vaigai" # Global Variable 

def village() : 
    name = "madurai" # Local Variable 
    def town() : 
        town_status = "beautiful" # Local Variable
        print("My village name is " + name + " which is located near the river " + River + " and it is a " + town_status + " town") # Enclosing Variable and Global Variable
        print(f"My village name is {name} which is located near the river {River} and it is a {town_status} town") # Enclosing Variable and Global Variable
    town() 
village(); # O/P:  My village name is madurai which is located near the river vaigai and it is a beautiful town

############################################################## 