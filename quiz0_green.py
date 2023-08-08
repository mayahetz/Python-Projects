#quiz0_green.py
## Given the stubs for the following functions 
## and the main program, complete them
## to output the result as shown below.
## Finish the assert statement to properly
## assert the result shown below (be careful 
## with the types of the variables).
def get_color(version):
    """
    If version is "green" return True (boolean). Otherwise, return False.
    """
    if version == 'green':
        return True
    else:
        return False

def get_num(version):
    """
    Given a string version, return 2 if version is "green". Otherwise, return -1.
    """
    if version == 'green':
        return 2
    else:
        return -1

if __name__ == "__main__":
    assert get_color('green') == True
    assert get_color('red') == False
    assert get_num('green') == 2
    assert get_num('red') == -1