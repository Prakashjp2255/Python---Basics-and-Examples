### basic 


class student() : 
    def name(self) :
        print("My name is prakash ")

s1 = student() 
s1.name()


## orey class ku multiple objects create pannlam 

class animal :
    def __init__(self ,  fname , age ) :  ## ithu tha constructo
        self.name = fname
        self.age = age 

    def display(self) : 
        print(f"Name : {self.name} , Age: {self.age}" ) 


class myclass : 
    x = 5 
    x = 8
    x = 0 

ss = myclass().x 
s1 = myclass().x 
s3 = myclass().x 

print(ss , s1 , s3 )


