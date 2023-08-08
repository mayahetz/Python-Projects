#week7_swap.py

def swap_key_val(database):
    ''' the function expects parameter: database (a dictionary)
        assuming that an input dictionary has unique values for
        each key, return a new dictionary with the keys and values 
        swapped '''

    new_dict = {}  #initialize new dictionary to adjust and later return 
    for key in database:
       value = database[key]
       new_dict[value] = key

    return new_dict

if __name__== '__main__':  #main program
    capitals = {"India": "Delhi", "Azerbaijan" : "Baku" }  #the dictionary 
    countries = swap_key_val(capitals) 
    
    #assert statements to check
    assert countries['Baku'] == 'Azerbaijan'
    assert countries['Delhi'] == 'India' 

    print(countries)