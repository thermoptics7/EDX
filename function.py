# This was the original function that I wrote based on my logic.

hungry = None
broughtLunch = None
haveMoney = None

def goOutToLunch(hungry, broughtLunch, haveMoney):

    result = hungry and (not broughtLunch) and haveMoney

    if result:
        printedresult = "You goin out to eat"

    else:
        printedresult = "You ain't goin out to eat"


    return printedresult

# Test code
testHungry = False
testBroughtLunch = False
testHaveMoney = True

print("Result: ", goOutToLunch(testHungry, testBroughtLunch, testHaveMoney))



