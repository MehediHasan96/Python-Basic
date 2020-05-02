
class Singer:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def change_name(self,name):
        self.name=name


    def introduction(self):
        print('Name:'+self.name, 'Age:'+str(self.age),sep='\n')




rock=Singer(name='Tanzir',age=40)
rock.name=" Tuhin"
rock.change_name("kamal")
rock.introduction()

print(rock.name+" , "+str(rock.age))
print(" ")
rock1=Singer("Safin",48)
rock1.introduction()
