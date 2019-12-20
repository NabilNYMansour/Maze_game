import Screen
import msvcrt


#-------------------|Setting x and y|-------------------#
x = 15
y = 50
place = 10  # Making an initial position
#-------------------------------------------------------#


#------------------|Calling Screen.py|------------------#
Board = Screen.ScreenMaker(x, y, '-')
BoardValues = Screen.ScreenValuer(Board)
Checker = list(BoardValues)
BoardValues[place] = 'O'
Screen.ScreenRefresher(BoardValues, y, Checker, 0)
#-------------------------------------------------------#


#----------------------|Movement|--------------------------------------------------------------------------------------------------------------#
def Movement(ScreenValues, CurrentPosition, Screen_y, trail):  # wasd for movement
    '''
    Allows for the movement of a point on a screen given ScreenValues{list}, the CurrentPosition{int} of the point, and Screen_y{int} values.
    It will also change the point to vʌ<> given the direction input 'wsad' to show a head moving.
    Can leave a trail{single char. str} behind the point that is moving.
    '''
    while True:
        Choice = msvcrt.getch()
        if str(Choice) == "b'd'":
            ScreenValues[CurrentPosition] = trail
            ScreenValues[CurrentPosition + 1] = '<'
            CurrentPosition = CurrentPosition + 1
        if str(Choice) == "b'a'":
            ScreenValues[CurrentPosition] = trail
            ScreenValues[CurrentPosition - 1] = '>'
            CurrentPosition = CurrentPosition - 1
        if str(Choice) == "b's'":
            ScreenValues[CurrentPosition] = trail
            ScreenValues[CurrentPosition + Screen_y] = 'ʌ'
            CurrentPosition = CurrentPosition + Screen_y
        if str(Choice) == "b'w'":
            ScreenValues[CurrentPosition] = trail
            ScreenValues[CurrentPosition - Screen_y] = 'v'
            CurrentPosition = CurrentPosition - Screen_y
        Screen.ScreenRefresher(BoardValues, y, Checker, 0)
#---------------------------------------------------------------------------------------------------------------------------------------------#


Movement(BoardValues, place, y, '*')
