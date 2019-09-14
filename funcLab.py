def arg(x):
    '''
    Description: This function prints the type of the argument passed.

    Parameters: x - variable; what the user enters in the argument

    Example:
    >>> arg(5)
    '''
    print(type(x))


def no_ret(x,y):
    var = x + y

print(no_ret(2,4))
'''
The output is none because the function is called wrong and print shoudl be in
the function definition
'''

def draw():
    '''
    Description: This function draws a grid represented on page 33 of the book
    in exercise 3-3.

    Parameters: None
    '''
    print('+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+')


def draw2():
    '''
    Description: This function draws a grid similar to the one in the function
    draw() but it has 4 rows and columns.

    Parameters: None
    '''
    print('+', '- '*4, '+','- '*4, '+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+', '- '*4, '+','- '*4, '+')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('|', ' '*8, '|', ' '*8, '|', ' '*8, '|', ' '*8, '|')
    print('+', '- '*4, '+','- '*4, '+', '- '*4, '+','- '*4, '+')


def nameAge(x, y):
    '''
    Description: This function prints the name of someone and how old they are
    days

    Parameters: x - name of the user's choice
                y - age of the name of the user's choice

    Example:
    >>> nameAge(Adi, 14)
    '''
    n = y*(365.25)
    print( x + ' is ' + str(n) + ' days old' )


def lenList(myList):
    '''
    Description: This function prints the length of a list that is passed in
    the argument

    Parameters: myList - The list that the user passes
    Example:
    >>> thisList=('apples, oranges, kiwis')
    >>> lenList(thisList)

    '''
    length = len(myList)
    print(length)

def squareCube(n):
    x = n**2
    y = n**3
    print('Number', '    ', 'Square', '    ', 'Cube')
    print(' '*(5 - len(str(n))), n, '    ' ' '*(6 - len(str(x))), x, '    ', ' '*(4 - len(str(y))), y)

squareCube(4)
