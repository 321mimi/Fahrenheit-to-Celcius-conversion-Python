# Convert Temperature
# By Michelle Cantin

import math

# The function
def convertTemperature(typeOfConversion, temp):
    # Fahrenheit to Celcius
    if (typeOfConversion == 0):
        result = float((temp - 32) * (5/9))
    # Celcius to Fahrenheit
    else:
        result = float((temp * (9/5)) + 32)
    result = round(result,2)
    return result

# Prompts 
temp = float(input("What is the temperature? "))
typeOfConversion = int(input("What is the type of conversion?\nPlease type 0 for Fahrenheit to Celcius, 1 for Celcius to Fahrenheit "))

# Calls the function and prints it
print(convertTemperature(typeOfConversion, temp))
