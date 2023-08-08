#week5_activity
 
#Given the radius of a sphere as input, write two functions:
#volume() calculates the volume of a sphere, rounded to two decimal places and returns this rounded value.
#area() calculates the surface area of a sphere, rounded to two decimal places and returns this rounded value.


import math


def volume(radius): 
    ''' this function takes radius as parameter, calculates volume, returns volume '''
    volume_sphere = (4/3) * math.pi * (math.pow(radius,3))
    result = round(volume_sphere, 2)
    return result

def area(radius): 
    ''' this function takes radius as parameter, calculates area, returns area '''
    area_sphere = 4 * math.pi * (math.pow(radius, 2))
    result = round(area_sphere, 2)
    return result

if __name__ == '__main__': 
    radius = float(input())
    print(f'A sphere has radius {radius} inches.')
    print(f'It has volume {volume(radius)} inches cubed.')
    print(f'It has surface area {area(radius)} inches squared.')
