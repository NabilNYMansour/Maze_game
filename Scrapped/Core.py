import Screen
import msvcrt


#-------------------|Setting x and y|-------------------#
x = 15
y = 50
place = 10  # Making an initial position
#-------------------------------------------------------#


#------------------|Calling Screen.py|------------------#
Board = Screen.ScreenMaker(x, y, '.')
BoardValues = Screen.ScreenValuer(Board)
Checker = list(BoardValues)
BoardValues[place] = 'O'
Screen.ScreenRefresher(BoardValues, y, Checker, 0)
#-------------------------------------------------------#


#-----------------------|Game Over|----------------------------------------------#
def GameOver(ScreenValues, Screen_y):
    '''
    prints a game over screen given the ScreenValues{list} and Screen_y{int}.
    '''
    
#--------------------------------------------------------------------------------#


#----------------------|Movement|--------------------------------------------------------------------------------------------------------------#
def Movement(ScreenValues, CurrentPosition, Screen_y, trail_horizontal, trail_vertical):  # wasd for movement
    '''
    Allows for the movement of a point on a screen given ScreenValues{list}, the CurrentPosition{int} of the point, and Screen_y{int} values.
    It will also change the point to vʌ<> given the direction input 'wsad' to show a head moving.
    Can leave a trail{single char. str} or trail_vertical{single char. str} behind the point that is moving.
    Will break and output a game over screen if the point hits '_' or '|'.
    '''
    while True:
        Choice = msvcrt.getch()
        if str(Choice) == "b'd'":
            ScreenValues[CurrentPosition] = trail_horizontal
            ScreenValues[CurrentPosition + 1] = '<'
            CurrentPosition = CurrentPosition + 1
        if str(Choice) == "b'a'":
            ScreenValues[CurrentPosition] = trail_horizontal
            ScreenValues[CurrentPosition - 1] = '>'
            CurrentPosition = CurrentPosition - 1
        if str(Choice) == "b's'":
            ScreenValues[CurrentPosition] = trail_vertical
            ScreenValues[CurrentPosition + Screen_y] = 'ʌ'
            CurrentPosition = CurrentPosition + Screen_y
        if str(Choice) == "b'w'":
            ScreenValues[CurrentPosition] = trail_vertical
            ScreenValues[CurrentPosition - Screen_y] = 'v'
            CurrentPosition = CurrentPosition - Screen_y
        Screen.ScreenRefresher(BoardValues, y, Checker, 0)
#---------------------------------------------------------------------------------------------------------------------------------------------#




Movement(BoardValues, place, y, '_', '|')
