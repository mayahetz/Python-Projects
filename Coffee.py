#Coffee.py
#file containing a class definition of a coffee beverage that inherits from the Beverage class

from Beverage import Beverage

class Coffee(Beverage):

    def __init__(self, ounces=None, price=None, style=None):
        '''
        constructor that extends the parent class (Beverage) constructor and sets 
        the style of coffee (for example, Cappuccino, Americano, Espresso, etc.) as
        an attribute to the Coffee class
        '''
        super().__init__(ounces, price)
        self.style = str(style)

    def getInfo(self):
        ''' 
        method that overrides the inherited getInfo method in the Beverage class, 
        and returns a str with the properties of a Coffee object
        '''
        
        s = Beverage(self.ounces, self.price).getInfo()
        q = "{} Coffee,".format(self.style)
        return q + ' ' + s

#c1 = Coffee(8, 3.0, "Espresso")
#result = c1.getInfo()
#print(result)  #the result is "Espresso Coffee, 8 oz, $3.00"