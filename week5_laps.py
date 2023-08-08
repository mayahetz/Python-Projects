def meters_to_laps(length):
    ''' this function takes in number of meters and returns number of laps '''
    num_laps = length / 50
    return num_laps 

if __name__ == "__main__":
    meters = float(input())
    num_laps = meters_to_laps(meters)
    print(f'{num_laps:.2f}')
