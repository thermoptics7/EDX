#Write a function called snowedIn that will determine
#whether a store is open or not based on the weather and
#temperature. This function should return True if a store is
#currently open, and False if it is not.
#
#The function will have three parameters: store (a string),
#temperature (an integer), and weather (a string). If no
#argument is supplied for weather, assume the weather is
#"sunny". The other possible values for weather are
#"sunny", "raining", "snowing", and "end of the world".
#
#Here are the conditions under which each restaurant closes:
#
#  - Cookout closes if it's below 10 degrees, if it's snowing,
#    or if it's both below 32 degrees and raining.
#  - Taco Bell closes if it's below 0 degrees, if it's snowing,
#    or if it's both below 32 degrees and raining.
#  - Waffle House only closes if it's the end of the world.
#
#For example, snowedIn("Cookout", 20) should return True
#because Cookout would be open if it was 20 degrees and sunny.
#snowedIn("Taco Bell", 30, "snowing") should return False
#because Taco Bell would be closed if it was snowing.
#
#Function: snowedIn
#Parameters: store (a string)
#            temperature (an integer)
#            weather (a string)
#Returns: True if the restaurant is open, False if it is not

#Write your function here!
def snowedIn(store,temperature,weather = "sunny"):
    if store == "Cookout":
        if (temperature < 10) or weather == "snowing" or (temperature < 32 and weather == "raining"):
            return False
        else:
            return True

    if store == "Taco Bell":
        if (temperature < 0) or weather == "snowing" or (temperature < 32 and weather == "raining"):
            return False
        else:
            return True

    if store == "Waffle House":
        if weather == "end of the world":
            return False
        else:
            return True

#When your code works, these two lines should run successfully.
#The first should print True, the second should print False.
#You can change these if you want to test your code.
print(snowedIn("Cookout", 10))
print(snowedIn("Taco Bell", 30, "snowing"))
print(snowedIn("Waffle House", 15))