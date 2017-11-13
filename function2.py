# Second function I had to write based on their logic.

hungry = None
broughtLunch = None
haveMoney = None

def goOutToLunch(hungry, broughtLunch, haveMoney):

    result = hungry and ((not broughtLunch) or haveMoney)

    if result:
        printedresult = "You goin out to eat"

    else:
        printedresult = "You ain't goin out to eat"


    return printedresult

# Test code
testHungry = False
testBroughtLunch = False
testHaveMoney = False

print("Result: ", goOutToLunch(testHungry, testBroughtLunch, testHaveMoney))