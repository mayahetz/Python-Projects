#DrinkOrder.py
#file containing a class definition of a customer’s drink order containing organizing various beverages

from Beverage import Beverage
from FruitJuice import FruitJuice
from Coffee import Coffee

class DrinkOrder(Beverage):
    def __init__(self):
        self.drinks = []
    
    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        
        total_price = 0
        
        s = "Order Items:" + "\n"
        
        for beverage in self.drinks:
            if self.drinks == []:
                total_price = 0
            else:
                total_price += beverage.getPrice()
                s += f"* {beverage.getInfo()}" + "\n"
        
        s += f"Total Price: ${total_price:.2f}" 
        return s   
        

#c1 = Coffee(8, 3.0, "Espresso")
#juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
#order = DrinkOrder()
#order.addBeverage(c1)
#order.addBeverage(juice)
#print(order.getTotalOrder())
