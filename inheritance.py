
#Basic Calculator

class Calculator:
    def sum(self,x,y):
        return x+y


class Calculator1(Calculator):
    def sub(self,x,y):
        return x-y

class Calculator2:
    def multi(self,x,y):
        return x*y


class Calculator3(Calculator1,Calculator2):
    def div(self,x,y):
        return x/y


    def multi(self,x,y):
        return x*y+2




c=Calculator3()
s=c.sum(4,3)
s1=c.sub(4,3)
m=c.super().multi(3,2)
d=c.div(10,3)
print("Result is:" ,s)
print("Result is:" ,s1)
print("Result is:" ,m)
print("Result is:" ,d)

