#quiz6_2.py

## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).
def get_year(date_str):
    """
    param: date_str (string) - contains a date in the format
    "MM/DD/YYYY" (where YYYY corresponds to the four digits
    of a year, MM to the two digits of a month, etc.).

    The function validates the string,
    extracts the year, and returns the last
    two digits of it as an integer.

    The validation should happen in the following order:
    If the date is empty, return an empty string.
    If the date does not have 2 slashes, return "/".
    If the year does not contain only digits, return 0.

    Examples:
    Calling the function with "05/25/2021"
    should return 21 as an integer.
    An input of "05/2021" should return a string "/".
    """

    if date_str == '':
        return ''
    if '/' not in date_str:
        return '/'
    if all([i.isdigit() for i in val.split('/', 3)]) == False:
        return 0

    new_date = date_str.split('/')
    month = new_date[0]
    day = new_date[1]
    year = new_date[2] 
    
    ret_year = str(year)[-2:]
    return ret_year 


if __name__ == "__main__":
    ### Write 3 additional assert statements
    assert get_year("2021/05/25") == 21  #shouldnt this be an error wtf
    assert get_year("05/25/2021") == 21
    assert get_year('') == '' 