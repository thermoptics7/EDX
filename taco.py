# You're craving a late night taco, but you're afraid you won't get to
# Taco Bell before it closes. Your second choice for food is hushpuppies
# from Cookout. As a last resort, you know you can always get hashbrowns
# from Waffle House, since they're open 24 hours.
#
# The function below should determine where you can go, based on what time it
# is. Write the conditional statements necessary to produce the correct
# restaurant output.
#
# Note the following conditions:
#   Taco Bell closes at 2:00am, so if it's 2:00am, we can't get Taco Bell.
#   Cookout closes at 3:00am, so if it's exactly 3:00, we can't get Cookout.
#   Waffle House never closes.
#
# Assume only the hours from 12AM - 7AM will be used. Hour will be an integer
# from 1 to 7 or 12, but 12 is actually the earliest time. Think about the
# best way to handle that special case!

# Function: lateNightNoms(hour, minute)
# Takes as input two integer variables: hour and minute
# representative of the current hour and minute (3:24 would be 3 and 24).
# Returns a string indicating the restaurant available.
def lateNightNoms(hour, minute):
    # Add your code here. You'll have access to two variables: hour and
    # minute. When your code is done, a variable named restaurant should exist
    # with the value "Taco Bell", "Cookout", or "Waffle House" according to
    # the conditions above.

    if (hour == 12 or (hour >= 1 and hour < 2)):
        restaurant = "Taco Bell"

    elif (hour >= 2 and hour < 3):
        restaurant = "Cookout"

    else:
        restaurant = "Waffle House"

    return restaurant


# You may modify the following code to check your work
hour = 1
minute = 45
print("Restaurant:", lateNightNoms(hour, minute))