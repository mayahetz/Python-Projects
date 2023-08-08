#FruitJuice.py
#file containing a class definition of a fruit juice beverage that inherits from the Beverage class

from Beverage import Beverage 

class FruitJuice(Beverage):
    def __init__(self, ounces=None, price=None, fruits=None):
        super().__init__(ounces, price)
        self.fruits = fruits  #list of strings

    def getInfo(self):
        flavors = ""
        slash = "/"
        
        for i in self.fruits:
            flavors += i + slash 
            slash = ""
       # return flavors -- dont do this we dont need a return here

        s = Beverage(self.ounces, self.price).getInfo()
        q = "{} Juice,".format(flavors)
        return q + ' ' + s

#juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
#print(juice.getInfo()) #--  prints "Apple/Guava Juice, 16 oz, $4.50"
