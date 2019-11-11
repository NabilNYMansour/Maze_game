import Screen
# Setting x and y:
x = 15
y = 50
place = 10 # Making an initial position
# Calling Screen.py
Board = Screen.ScreenMaker(x, y)
BoardValues = Screen.ScreenValuer(Board)
Checker = list(BoardValues)
BoardValues[place] = 'O'
def Movement(StartingPostion, y_Axis_Length): # wasd for movement
    postion = StartingPostion
    while True:
        Choice = input()
        if Choice == 'd':
            BoardValues[postion] = '.'
            BoardValues[postion + 1] = 'O'
            postion = postion + 1
        if Choice == 'a':
            BoardValues[postion] = '.'
            BoardValues[postion - 1] = 'O'
            postion = postion - 1
        if Choice == 's':
            BoardValues[postion] = '.'
            BoardValues[postion + y_Axis_Length] = 'O'
            postion = postion + y_Axis_Length
        if Choice == 'w':
            BoardValues[postion] = '.'
            BoardValues[postion - y_Axis_Length] = 'O'
            postion = postion - y_Axis_Length
        Screen.ScreenRefresher(BoardValues,y,Checker,0)
Movement(place,y)