#You're going on a long run, and want to calculate what time you'll be home.
#The problem is, the running app on your phone only gives you the estimated
#length of your run in minutes.
#
#We've provided the following variables you should not change:
#hour and minute below represent 3:48 on an analog clock.
#
#Using the provided variables, calculate the time you should arrive home,
#if your run is estimated to take 172 minutes.

#Do not modify these two lines of code
hour = 3
minute = 48

#Add your code here!

#Here is where i'm trying to actually design an algorithm to solve this
estimateInHours = (172 // 60)
minutesToBeAdded = (172 % 60)

minute += minutesToBeAdded
#Debug Code print("MinuteBefore Loop: ", minute)

if minute >= 60:
    hour += estimateInHours + 1
    minute -= 60

    #Debug code
    #print(minutesToBeAdded)
    #print("Hour: ", hour)
    #print("Minute: ", minute)
    #Debug code

else:
    hour += estimateInHours

    # Debug code
    #print("Minutes To be Added: ", minutesToBeAdded)
    #print("Hour: ", hour)
    #print("Minute: ", minute)

#Do not modify the code below this line
print("Expected to arrive home at " + str(hour) + ":" + str(minute))