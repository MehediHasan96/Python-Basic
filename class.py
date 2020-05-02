

class  DressShop:

    name=" "
    owner=" "


    def details(self):
        print(self.name,self.owner,sep='|')


    def details_with_details(self,address):
        print(self.name + ", "+self.owner +","+address)

kids=DressShop()
kids.name="Baby Zone"
kids.owner="Karim"

kids.details()
kids.details_with_details('Boshundara shopping mall')