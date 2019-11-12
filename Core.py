import Screen
import msvcrt

# Setting x and y:
x = 15
y = 50
place = 10  # Making an initial position
# Calling Screen.py
Board = Screen.ScreenMaker(x, y, '-')
BoardValues = Screen.ScreenValuer(Board)
Checker = list(BoardValues)
BoardValues[place] = 'O'
Screen.ScreenRefresher(BoardValues, y, Checker, 0)


def Movement(StartingPostion, y_Axis_Length):  # wasd for movement
    postion = StartingPostion
    while True:
        Choice = msvcrt.getch()
        if str(Choice) == "b'd'":
            BoardValues[postion] = ' '
            BoardValues[postion + 1] = '<'
            postion = postion + 1
        if str(Choice) == "b'a'":
            BoardValues[postion] = ' '
            BoardValues[postion - 1] = '>'
            postion = postion - 1
        if str(Choice) == "b's'":
            BoardValues[postion] = ' '
            BoardValues[postion + y_Axis_Length] = 'ʌ'
            postion = postion + y_Axis_Length
        if str(Choice) == "b'w'":
            BoardValues[postion] = ' '
            BoardValues[postion - y_Axis_Length] = 'v'
            postion = postion - y_Axis_Length
        Screen.ScreenRefresher(BoardValues, y, Checker, 0)


Movement(place, y)
