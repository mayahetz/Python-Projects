#Beverage.py

class Beverage:

    def __init__(self, ounces, price):
        if ounces != None:
            self.ounces = int(ounces)
        if price != None:
            self.price = float(price)
    
    def updateOunces(self, newOunces):
         #updates the ounces of the beverage
         self.ounces = newOunces

    def updatePrice(self, newPrice): 
        #updates the price of the beverage
        self.price = newPrice

    def getOunces(self):
        #returns the ounces of the beverage
        return self.ounces
    
    def getPrice(self):
        #returns the price of the beverage
        return self.price

    def getInfo(self):
        #returns a str with the current beverage’s ounces and price
        return f"{self.ounces} oz, ${self.price:.2f}"

#b1 = Beverage(16, 20.5)
#print(b1.getInfo()) -- this prints "16 oz, $20.50" which is correct 