a = 10 
b = 20 

## 1. Arithmetic Operators : 

c = a + b 
print(c) # It will print 30 because c is the sum of a and b 
d = a - b 
print(d) # It will print -10 because d is the difference of a and b 
e = a * b 
print(e) # It will print 200 because e is the product of a and b 
f = a / b 
print(f) # It will print 0.5 because f is the quotient of a and b 
g = a % b 
print(g) # It will print 10 because g is the remainder of a divided by b 
h = a ** b  
print(h) # It will print 100000000000000000000 because h is a raised to the power of b
i = a // b 
print(i) # It will print 0 because i is the floor division of a and b 

## 2. Comparison Operators : 

x = 5 
y = 10 

print(x == y) # It will print False because x is not equal to y 
print(x != y) # It will print True because x is not equal to y
print(x > y) # It will print False because x is not greater than y
print(x < y) # It will print True because x is less than y 
print(x >= y) # It will print False because x is not greater than or equal to y
print(x <= y) # It will print True because x is less than or equal to y 

## 3. Logical Operators : 

p = True 
q = False 

print(p and q) # It will print False because p and q are not both True 
print(p or q) # It will print True because p is True 
print(not p) # It will print False because p is True
print(not q) # It will print True because q is False 

## Billing caluclations --> problem solve 
## 1.Arithmetic Operators : 
amount = 1200 
tax = amount * 0.18 
total = amount + tax 
print("Total amount after tax:", total) 

if total > 1000 :
    discount = total *0.10
    total  = total - discount 
print("Discount applied. Total amount:", total) 

## 2.Logical and Comparison Operators : 

age = 90
movie_ticket_price = 180 
school_student = 'yes' 

if age >= 60  or  school_student == 'yes'  : 
    print("You are eligible for a movie ticket discount of 20%")
    print ("Original movie ticket price:", movie_ticket_price)
    discount = movie_ticket_price * 0.20 
    movie_ticket_price = movie_ticket_price - discount 
else : 
    print("You are not eligible for a movie ticket discount") 

print ("Final movie ticket price:", movie_ticket_price) 

