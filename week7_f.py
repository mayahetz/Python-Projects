#week7_f.py
## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).

def get_list_even(old_list):
    """ Given a list of numerical values,
    return a **new list** that contains 
    the even elements (numbers) of the list.
    If the list is empty, return -1.
    For example, if the list contains
    [10, 1, 6, 3, 8, -1, 5, 4, 9]
    the function returns
    [10, 6, 8]
    """
    
    new_list = []

    if old_list == []:
        return -1
    
    for element in old_list:
        if element % 2 == 0:
            num = element 
            new_list.append(num)
        return new_list 

if __name__ == "__main__":
    ### Write 2 assert statements
    ### to test the function
    
    assert get_list_even([]) == -1  #passes test
    assert get_list_even([10, 1, 6, 3, 8, -1, 5, 4, 9]) == [10, 6, 8]