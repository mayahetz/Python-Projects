#testFile.py
#file containing pytest functions testing the Beverage, Coffee, FruitJuice, and DrinkOrder classes
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    beverage1 = Beverage(24, 8.0)

    assert beverage1.getInfo() == "24 oz, $8.00"
    assert beverage1.getOunces() == 24
    assert beverage1.getPrice() == 8.0
    assert beverage1.updateOunces(16) == None
    assert beverage1.updatePrice(12.0) == None


def test_Coffee():
    coffee1 = Coffee(8, 4.0, "Americano")

    assert coffee1.getInfo() == "Americano Coffee, 8 oz, $4.00"

def test_FruitJuice():
    fj =  FruitJuice(14, 7.2, ["Strawberry", "Pineapple"])

    assert fj.getInfo() == "Strawberry/Pineapple Juice, 14 oz, $7.20"

def test_DrinkOrder():
    coffee1 = Coffee(8, 4.0, "Americano")
    fj =  FruitJuice(14, 7.2, ["Strawberry", "Pineapple"])
    order = DrinkOrder()
    order.addBeverage(coffee1)
    order.addBeverage(fj)

    assert order.addBeverage(coffee1) == None
    assert order.addBeverage(fj) == None

    assert order.getTotalOrder() == 'Order Items:\n* Americano Coffee, 8 oz, $4.00\n* Strawberry/Pineapple Juice, 14 oz, $7.20\n* Americano Coffee, 8 oz, $4.00\n* Strawberry/Pineapple Juice, 14 oz, $7.20\nTotal Price: $22.40'
