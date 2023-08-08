#housing_score_lab.py
#Author: Maya Hetz


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
    
    #check if 0 or 1 periods 
    #isdigit make sure int
    #split at period, check each side int, only two parts 

#assert statements to check if is_num function works 
#no assertion errors come up so yes
assert is_num("8") == True
assert is_num(8) == False
assert is_num("3.95") == True
assert is_num("8.apple") == False
assert is_num("8.1.1") == False


def compute_housing_score(academic_year, needs, age):
    ''' this function takes a students academic year (str), age (int), and needs (str) as 
        parameters to assign points and compute a housing score based on user input. 
        students who are older and who indicate that they need housing will receive a 
        higher housing score '''
    
    current_score = 0

    #check academic year, add points accordingly
    if academic_year == '1':
        current_score += 1
    elif academic_year == '2':
        current_score += 2
    elif academic_year == '3':
        current_score += 3
    elif academic_year == '4':
        current_score += 4

    #check if student needs housing, if answer is yes add one point
    if needs == "yes":
        current_score += 1
    else:
        current_score

    #check if older than 23, if yes add one point to score
    if int(age) >= 23:
        current_score += 1
    
    return current_score

#assert statements to check if compute_housing_score function works
#no assertion errors come up so yes
assert compute_housing_score('3', 'yes', 19) == 4
assert compute_housing_score('1', 'no', 18) == 1
assert compute_housing_score('2', 'yes', 20) != 2

if __name__ == "__main__":
    total_score = 0 # for the final housing score
    age = None
    student_year = input("What year are you? (1, 2, 3, 4): ")
    student_needs = input("Do you need this housing? (yes or no): ")

    # A header to start the program
    print("-------------------------------")
    print("   HOUSING SCORE CALCULATOR")
    print("-------------------------------")
    print()

    #calls is_num(age) until a valid age is entered 
    while is_num(age) == False:
        age = input("Enter your age: ")

    #computes total housing score using above function
    total_score = compute_housing_score(student_year, student_needs, age) 

    # At the end of the program, tell the user their score
    print()
    print("------YOUR HOUSING SCORE----------")
    print("Your housing points score is", total_score)
    print("----------------------------------")
