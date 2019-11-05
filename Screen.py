def ScreenMaker(Screen_x, Screen_y):
    ScreenAxis = []
    Screen = {}
    # The grid starts at (1,1) and ends at (ScreenSize, ScreenSize)
    for x in range(Screen_x):
        for y in range(Screen_y):
            ScreenAxis.append((x, y))
    for counter in range(len(ScreenAxis)):
        Screen[ScreenAxis[counter]] = '.'
    return Screen


def ScreenValuer(Screen):
    ScreenValues = list(Screen.values())
    return ScreenValues


def ScreenPrinter(ScreenValues, Screen_y):
    for counter_print in range(0, len(ScreenValues), Screen_y):
        print(str(ScreenValues[counter_print:(counter_print + Screen_y)]).replace(
            '[', '').replace(',', '').replace(']', '').replace("'", ''))


def ScreenRefresher(ScreenValues, Screen_y, ScreenChecker):
    # When placing the ScreenChecker, remember that it musts be equal to list(ScreenValues).
    if ScreenChecker != ScreenValues:
        ScreenPrinter(ScreenValues, Screen_y)

'''
In order to use these commands, you first declare x and y then run
(1) ScreenMaker --> (2) ScreenValuer --> (3) declare checker = list(ScreenValues) --> Then do the code for the Screen Change and implement
ScreenRefresher at the end of each code that changes something in the screen.
'''

# The following is a test/example:

'''
x = 15
y = 30
Screen = ScreenMaker(x, y)
ScreenValues = ScreenValuer(Screen)
Checker = list(ScreenValues)
def SampleChange_Screen():
    ScreenValues[5] = 'X' # This is the change that will occur on the Screen (u place the functions that change the screen here) 
    ScreenRefresher(ScreenValues, y, Checker) # U intigrate this at the end of the function
SampleChange_Screen()
'''

# Import as necessary.