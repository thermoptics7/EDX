# In the function below, you have access to the variable temperature. Fill
# the function with a conditional that assigns the value "Freezing" to the
# variable result if temperature is less than or equal to 32 degrees
# Fahrenheit, or "Not Freezing" if the the temperature is greater than
# 32 degrees Fahrenheit.
#
# There's one catch: temperature is actually given in Celsius! So, you'll
# want to convert temperature to Fahrenheit, then check if it's above or
# below freezing. Try to do that directly in the conditional instead of
# before!
#
# Note that to convert from Celsius to Fahrenheit, multiply the temperature
# by 9/5, then add 32.

#tempInF = 0.0
def checkFreezing(temperature):
    # Add your code here. When your code is done running,
    # there should exist a variable called result, with
    # the value "Freezing" or "Not Freezing" depending on
    # the value of temperature.

    tempInF =  (temperature * (9/5)) + 32 #Convert temperature to Fahrenheit

    if tempInF <= 32.0:
        result = "Freezing"
    else:
        result = "Not Freezing"
    return result


# Modify the value of this variable to test your code.
testTemperature = 32

print("At", testTemperature, " Celsius, it is", checkFreezing(testTemperature))
