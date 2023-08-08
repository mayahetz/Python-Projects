# Lab00, CS 9, Maya Hetz

def areElementsInList(list1, list2):
    ''' This function takes two lists as its parameters (list1 and
        list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, True is
        returned.
    '''
    #if list1 empty returns false
    if list1 == []:
        return True 

    #if element is not in list2 then returns false
    for element in list1:
        if element not in list2:
            return False
    
    #this means no errors in what fxn is trying to find so returns true
    return True


assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True

#assert statements all work yay so function passes tests

def alternateCase(s):
    ''' This function takes a string parameter (s) and returns a new
        string that flips the case of each alpha character in s.
    '''

    #s = s.split(), no need to split actually the for statement iterates over

    swapped_character = "" #create new empty string for the swaps

    for character in s:
        if character.isupper() == True:
            swapped_character += character.lower()  #add new char to empty string
        else:
            swapped_character += character.upper()  #same as above
    
    return swapped_character  #want to return new strings with swaps
    

assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"

#all the given assert statements pass! 

def getCharacterCount(s):
    ''' This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''
    the_dict = {}  #make dict to add to

    s = s.upper()  #to make case insensitive
    
    for character in s:
       #if character == ' ':
          #  the_dict[character] += 1
        if character in the_dict: 
            the_dict[character] += 1
        else:
            the_dict[character] = 1  
            #DOES NOT WORK WITH ZERO AHHH
            #changed to one and works. doesnt matter bc it only shows the letters called
    
    return the_dict  #return that dict


x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None

#no assertion errors!