#AnimalShelter.py

'''
An AnimalShelter object will contain a dictionary structure where the keys of the dictionary 
will be a str type representing an Animals species (all upper-case characters).
The dictionary value will be a list of Animal objects that the AnimalShelter contains. Note 
that the order of the Animals in the list is based on when the Animal object was inserted 
into the dictionary structure (most recent Animal inserted will be at the end of the list).
'''

class AnimalShelter:
    
    def __init__(self): 
        '''
        initializes the dictionary structure of the AnimalShelter class. 
        initially, this dictionary should be empty.
        ''' 
        self.AnimalShelter = {}

    def addAnimal(self, animal): 
        if self.AnimalShelter.get(animal.species) == None:  #if species exists in dict
            self.AnimalShelter[animal.species] = [animal]
        else:    
            self.AnimalShelter[animal.species].append(animal)  #append methods adds the animal to end of list

    def removeAnimal(self, animal):
        if self.doesAnimalExist(animal):  #can i call does animal exist already? -- yes it works
            for i in self.AnimalShelter[animal.species]:  #now check if all parameters match 
                if i.species == animal.species and i.weight == animal.weight and i.age == animal.age and i.name == animal.name:
                    self.AnimalShelter[animal.species].remove(i)

    def removeSpecies(self, species):
        s = self.AnimalShelter.get(species.upper())
        if s != None:
            del self.AnimalShelter[species.upper()]  #delete species entry from shelter
    
    def getAnimalsBySpecies(self, species):
        the_result = ""  #initialize the result to eventually return 
        s = self.AnimalShelter.get(species.upper())
        if s != None:
            newline = ""
            for i in s:  #for loop makes it run thru for each animal
                the_result += newline + i.toString()  #used toString method 
                newline = "\n"
        
        return the_result

    def doesAnimalExist(self, animal): 
        species = self.AnimalShelter.get(animal.species)
        if species == None: 
            return False
        else:
            for i in species:  #now check if all parameters match 
                if i.species == animal.species and i.weight == animal.weight and i.age == animal.age and i.name == animal.name:
                    return True   #means animal exists in animal shelter yay
        
        return False #return false if not none or all paramters don't match 
