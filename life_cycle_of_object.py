
class Object:
    def __init__(self,x):
        self.x=x

        print(self.x+" "+"is created")


    def __del__(self):
        print(self.x+" "+"is destroyed")
        


a=Object("X")
b=Object("Y")
print("Hello World")