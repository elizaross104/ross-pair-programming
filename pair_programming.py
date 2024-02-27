# Author: Eliza Ross
# Feb. 22, 2024
# Pair programming assignment

# Editor: Anna Melega
# Everything looks really good, easy to follow with all of the comments. 


# Write a function that takes two values (feet and inches) and converts to meters

def convert_meters(array): #input should be array with format [feet, inches]
    feet = array[0] #pulls feet value from the 0 index of the input array
    inches = array[1] #pulls inches value from the 1st index of the input array
    decimal = inches/12.0 #converts inches to feet by dividing by 12
    total_feet = feet + decimal #adds the value for feet to the value of inches converted to feet to find total feet
    meters = total_feet / 3.281 #converts total feet to meters, 3.281 found from online calculator
    return meters #returns number of meters

def test_convert_meters():
    assert convert_meters([0, 0]) == 0
    assert convert_meters([3, 3.37]) == 1
    print("Passed tests")
    
test_convert_meters()
