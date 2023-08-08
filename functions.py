#contains all assembled functions

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    if 'S' in menu:
        if menu['S'] == 'Save':
            menu['S'] = 'Save the data'
    if 'R' in menu:
        if menu['R'] == 'Restore':
            menu['R'] = 'Restore data from file'
    if 'Q' in menu:
        if menu['Q'] == 'Quit':
            menu['Q'] = 'Quit this program'
    if 'T' in menu:
        if menu['T'] == 'Total grade':
            menu['T'] = 'Show the total'
    
    print('==========================')
    print('What would you like to do?')
    
    for key, value in menu.items():
        print(key, '-', value )
    
    print('==========================')

def get_grades(info_list):
    """
    param: info_list - a list that contains dictionaries

    Each dictionary in the info_list is supposed to have
    the following string keys:
    - category - the name of each grade category (string)
    - weight - the percentage weight of the category (float)
    - grades - a list of numeric grades for each assignment
    If no grades are stored for a category, the "grades"
    item will store an empty list.

    return:
    The function returns a new (nested) list, which contains
    the extracted grades for each category.
    If the input is an empty list, the function returns
    an empty list.
    """
    new_list = []
    
    if info_list == []:
        return new_list 
        
    for subdict in info_list: 
        new_list.append(subdict['grades'])
        
    return new_list 
    
def get_list_avg(num_list):
    """
    param: num_list - a nested list of lists
    
    The function expects that each nested lists contains
    only the numeric values.
    
    return:
    The function returns a new list that contains the
    average value of each sub-list in num_list.
    If the input is an empty list, the function returns
    an empty list.
    """
    list_avg = []
    
    if num_list == []:
        return list_avg
    
    for sublist in num_list: 
        if len(sublist) == 0:
            list_avg.append(0)
        else:
            avg = sum(sublist) / len(sublist)
            list_avg.append(avg)

    return list_avg

def get_total_grade(info_list, show_steps = False):
    """
    param: info_list - a list that contains dictionaries
    param: show_steps - a Boolean flag (False by default)
            controls whether the function outputs intermediate
            steps, outputting the average scores.

    Each dictionary in the info_list is supposed to have
    the following string keys:
    - category - the name of each grade category (string)
    - weight - the percentage weight of the category (float)
    - grades - a list of numeric grades for each assignment
    If no grades are stored for a category, the "grades"
    item will store an empty list.

    return:
    The function returns a floating-point value that results from
    summing up the product of the weight of each category with the
    average value of each "grades" list.
    The function returns 0 if the info_list is empty.

    Helper functions:
    The function calls the following helper functions:
    - get_grades() to extract the grades from info_list
    - get_list_avg() to compute the average score for each
      extracted grade list
    """
    if info_list == []:
        return 0 

    avg_sum = 0

    only_grades = get_grades(info_list)
    avg_grades = get_list_avg(only_grades)
    
    for index, subdict in enumerate(info_list):
        category_avg = avg_grades[index]
        category_weight = subdict['weight']
        category_grade = (category_avg * (category_weight / 100))
        avg_sum += category_grade

        if show_steps:
            print(f"{subdict['category']} average {category_avg:.2f}%", end = " ")
            print(f"({category_grade:.2f}/{category_weight})")
    
    return avg_sum 
    
def get_selection(action, suboptions):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
            The keys are assumed to be in upper-case.

    The function displays a submenu for the user to choose from. 
    Asks for user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection as an upper-case string
            (should be a valid key in the suboptions)
    """
    selection = None
    while selection not in suboptions:
        print(f"What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        selection = input("::: Enter your selection\n> ")
        selection = selection.upper() # to allow us to input lower- or upper-case letters
    print(f"You selected {selection} to",
          f"{action.lower()} {suboptions[selection].lower()}.")
    return selection

def print_grade_info(info_list, show_grades = True):
    """
    param: info_list - a list that contains dictionaries
    param: show_grades - a Boolean flag (True by default)
            controls whether the function outputs the grades
            for each assignment; if set to False, only displays
            category information
    Each dictionary in the info_list is supposed to have
    the following string keys:
    - category - the name of each grade category (string)
    - weight - the percentage weight of the category (float)
    - grades - a list of numeric grades for each assignment
    If no grades are stored for a category, the "grades"
    item will store an empty list.
    The function prints the grade information in the
    following format (if show_grades is True):
        {N} - {Category name} ({category percentage}%)
        {list of grades}
        ---
    where N is each category's ordinal number
    (note that numbering starts at 1)
    Example:
    for an input list with a single category
    [ { "category": "PA", "weight" : 5,
        "grades" : [100.0, 100.0]} ]
    the function outputs the following:
        1 - PA (5%)
        [100.0, 100.0]
        ---
    The function prints a single line with "---"
    if the provided list is empty.
    
    return:
    The function does not return anything.
    """
    if info_list == []:
        print('---')
        
    
    for index, subdict in enumerate(info_list):
        N = index + 1 
        category_name = subdict['category']
        category_percentage = subdict['weight']
        list_of_grades = subdict['grades']
        print(f'{N} - {category_name} ({category_percentage}%)')
        if show_grades == True:
            print(f'{list_of_grades}')

    print('---')

def is_num(val):
    ''' The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise. '''

    if type(val) == str:
        if '.' in val:
            if all([i.isdigit() for i in val.split('.', 1)]) == True:
               return True
            else: 
                return False
        else:
            if val.isdigit() == True:
                return True
            else:
                return False
    else: 
        return False

def is_num_str_list(main_list):
    
    if len(main_list) == 0:  #returns False is list is empty 
            return False
    
    for item in main_list: # check each element of the provided parameter
        if type(item) != str:
            return False
        if is_num(item) == False: # call the helper function and check if it returned False
            return False
    return True # if none of the above returns got triggered, we have a numeric string as each element

def create_category(info_str):
    """
    param: info_str (string) is expected to contain two
            space-separated items:
            a category name (ideally, a single word)
            and its numeric grade weight.
    The function splits the input string and validates its
    components (see the errors and helper functions).

    return:
    If the validation passes, return a new dictionary with 
    the following string keys are assigned to the values that
    were extracted from the info_str parameter:
    - category - the name of each grade category (string)
    - weight - the percentage weight of the category (float)
    - grades - an empty list (for storing future grades)
    Example: an input string "Quiz 25" results in a dictionary
    { 'category': 'Quiz', 'weight': 25.0, 'grades': [] }

    Errors:
    If any of the errors occur, a new dictionary is not created.    
    If info_str.split() does not result in a two-element list,
    then return -2.
    If a category name is less than 2 characters or contains a
    comma, then return -1.
    If the weight (the percentage) in info_str is not numeric
    (int or float), return 0.

    Helper functions:
    The function calls the following helper functions:
    - is_num() to verify that the weight is a numeric value.
    """
    
    str_list = info_str.split()
    
    if len(str_list) != 2:
        return -2
    
    if (len(str_list[0]) < 2) or (',' in str_list[0]):
        return -1
    
    if is_num(str_list[1]) == False:
        return 0
        
    new_dict = {'category': str_list[0], 'weight': float(str_list[1]), 'grades': []}
    
    return new_dict
    
def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that the provided index
    idx is a valid positive index that can retrieve
    an element from in_list.

    returns:
    - True, if idx is a positive numeric index
    that can retrieve an element from in_list.
    - False if idx is not an integer value, is negative
    or exceeds the size of in_list.
    """
    
    if is_num(idx) == True:
        if ((int(idx) >= 0) 
            and (int(idx) < (len(in_list) + start_idx)) 
            and (int(idx) >= start_idx)):
                return True 
        else:
            return False
    else:
        return False

def update_category(info_list, idx, info_str):
    """
    param: info_list - a list that contains dictionaries
    param: idx (int) - a valid positive zero-based index
            that retrieves a dictionary from in_list
    param: info_str (string) is expected to contain two
            space-separated items:
            a category name (ideally, a single word)
            and its numeric grade weight.

    The function first calls its helper function
    create_category() and stores its return value.
    If create_category() successfully returned a new
    dictionary with the info provided in the info_str,
    then the function proceeds to update info_list[idx]
    with the information from the returned dictionary.
    The function does not update the values for "grades".
    
    return:
    If create_category() validation passes,
    return info_list[idx].
    Otherwise, return the error from create_category().

    Errors:
    See create_category()

    Helper functions:
    The function calls the following helper functions:
    - create_category() to split the input string and validate
    its components.

    Known vulnerability:
    The function assumes that the caller provided 
    a valid info_list index, so it does not run the validation
    of idx.
    """
    str_list = info_str.split()
    
    if len(str_list) != 2:
        return -2
    
    if (len(str_list[0]) < 2) or (',' in str_list[0]):
        return -1
    
    if is_num(str_list[1]) == False:
        return 0
    
    return_val = create_category(info_str) 
    
    if type(return_val) == type({}):
        info_list[idx]['category'] = return_val['category']
        info_list[idx]['weight'] = return_val['weight']
        return info_list[idx]

def delete_item(info_list, idx, start_idx = 0):
    """
    param: info_list - a list from which to remove
            an item
    param: idx (str) - a string that is expected to
            contain an integer index of an item in
            the in_list
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function first checks if info_list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from info_list.

    returns:
    If info_list is empty, return 0.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from info_list.

    Helper functions:
    - is_valid_index()
    """
    
    if info_list == []:
        return 0
    
    if is_valid_index(idx, info_list, start_idx):
        deleted_item = info_list[int(idx) - start_idx]
        info_list.pop(int(idx) - start_idx)
        return deleted_item
    else:
        return -1
        