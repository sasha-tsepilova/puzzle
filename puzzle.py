'''
'''
def validate_rows(board: list):
    '''
    Gets board configuration and returns True if all rows has not repeating
    numbers
    >>> validate_rows(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    '''
    for row in board:
        numbers = set()
        for element in row:
            if element not in('*', ' '):
                if element in numbers:
                    return False
                numbers.add(element)
    return True

def validate_columns(board: list):
    '''
    Gets board configuration and returns True if all columns has not repeating
    numbers
    >>> validate_columns(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    '''
    for i in range(9):
        numbers = set()
    
        for j in range(9):
            element = board[j][i]
            if element not in('*', ' '):
                if element in numbers:
                    return False
                numbers.add(element)
    return True

def validate_corner(board: list):
    '''
    Gets board configuration and returns True if all corners has not repeating
    numbers
    >>> validate_corner(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    '''
    for i in range(5):
        numbers = set()
        for j in range(4-i, 9-i):
            element = board[j][i]
            if element not in('*', ' '):
                if element in numbers:
                    return False
                numbers.add(element)
        
        for j in range(i, i + 5):
            element = board[8-i][j]
            if element not in('*', ' '):
                if element in numbers:
                    return False
                numbers.add(element)

    return True

import doctest
doctest.testmod()
