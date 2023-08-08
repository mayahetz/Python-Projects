#Animal.py

'''
we will define the animal attributes as follows... 
species - str that represents the species of the animal. Your program should ensure that 
this field will be stored in all upper-case characters.
weight - float that represents the weight (in lbs) of an animal.
age - int that represents the age (in years) of an animal.
name - str that represents the name of the animal. Your program should ensure this field 
will be stored in all upper-case characters.
'''

class Animal:
    species = None
    weight = None
    age = None
    name = None
    
    def __init__(self, species=None, weight=None, age=None, name=None):
        if species != None:
            if species != '':
                self.species = species.upper()
        if weight != None:
            self.weight = float(weight)
        if age != None:
            self.age = int(age)
        if name != None:
            if species != '':
                self.name = name.upper()
    
    def setSpecies(self, species): 
        self.species = species.upper()

    def setWeight(self, weight): 
        self.weight = weight
    
    def setAge(self, age):
        self.age = age
    
    def setName(self, name):
       self.name = name.upper()

    def toString(self):  #return the string of the animal
        output = f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"
        return output

#a = Animal("dog", 12.2, 2, "Ruffles")
#print(a.toString()) #== Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2