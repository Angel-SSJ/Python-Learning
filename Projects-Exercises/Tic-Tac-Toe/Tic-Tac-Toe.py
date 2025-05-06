

def init():
    """
    Initialize the main values to the function main.

    Raises:
        TypeError: The input must be a string  and be a value between "X" and "O"
    Returns:
        string like output: game Dialogues
        one: a value between 'X' or 'O'
        two: a value between 'X' or 'O', it is dependent of one
        board: a list like this style [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    """
    print('Hola, bienvenido a un juego Tic Tac Toe mas, ¿Estas lista para comenzar? ')
    print('Vamos a comenzar escogiendo equipos')
    one = input("Player 1, ¿Que prefieres X o O?: ").upper()
    if type(one) is not type(str) and one not in ['X', 'O']:
        raise TypeError('The input must be a string  and be a value between "X" and "O"')
    else:
        one = one if one in ('O', 'X') else 'O'
        two = 'O' if one == 'X' else 'X'
        board = [[' ' for _ in range(3)] for _ in range(3)]
    return one, two, board


def show(matrix, columns):
    """
    Receive a list of 2 dimensions and one tuple
    Print the numbers of columns (1  2  3)
    Compress the list and tuple with the built-in function zip()
    get a type mixed tuple between this inputs
    print column in columns and join row in matrix
    Coords verticals are the values of column, and places empty are
    the row in matrix, which will change for X or O

    Args:
        matrix (list): The empty values where the play will be able to change for X or O
        columns (tuple): The verticals coods to guide the player

    Raises:
        TypeError: Matrix must be a tuple
        TypeError: Columns must be a tuple
    Returns:
        Dashboard: it is the game place. It is mutable by choices of player
    """

    if type(matrix) is not list:
        raise TypeError('Matrix must be a list')
    elif type(columns) is not tuple:
        raise TypeError('Columns must be a tuple')
    else:
        print("   1   2   3 \n  ---+---+---")
        for column, row in zip(columns, matrix):
            print(f'{column} {" |  ".join(row)} \n  ---+----+---')


def winning(matrix):
    """
    Recieve a matrix (list) partially empty with values " ", "X" or "O"
    Value a possible victory with 3 Methods
        Rows: Evaluates each row in matrix, then within each row evaluates if
              each value is whithin row, if not empty string
              if these conditions are met, return True

        Columns: Unzip the matrix in list(rows), like this
                matrix=[[' ' for _ in range(3)] for _ in range(3)]
                matrix=[['1','2','3'],['1','2','3'],['1','2','3']]
                    row_one=('1','1','1')
                    row_one=('2','2','2')
                    row_one=('3','3','3')
                Then this process, reversed the positions, and them the last step,
                evaluates each c in row, c!=' ' c == row[0]
                if these conditions are met, return True


        Diagonals: set the values of x and y by zip((0,2), (2,0)), then evaluates x and y in matrix
                   the second position of matrix is a set value
                   matrix[0][x] == matrix[1][1] == matrix[2][y] != ' '
                   if these conditions are met, return True

    Args:
        matrix (list): The empty values where the play will be able to change for X or O.

    Raises:
        TypeError: Matrix must be a list

    Returns:
        False: None of these methods detect a winning pattern
        True: One of these methods detect a winning pattern,
              Whether they are by columns, diagonals or rows

    """

    if type(matrix) is not list:
        raise TypeError('Matrix must be a list')
    else:
        # Rows
        for row in matrix:
            if all(c == row[0] and c != ' ' for c in row):
                return True

        # Columns
        rotated = [list(row) for row in zip(*matrix)]
        rotated = [list(reversed(row)) for row in rotated]
        for row in rotated:
            if all(c == row[0] and c != ' ' for c in row):
                return True
        # Diagonals
        for x, y in zip((0, 2), (2, 0)):
            if matrix[0][x] == matrix[1][1] == matrix[2][y] != ' ':
                return True


def draw(matrix):

    """
    Receive a matrix (list), then evaluates all possibilities with the expression:
    if all(c != ' ' for row in matrix for c in row):
        where evaluates each c in row, each row in matrix, c!=' '

    Args:
        matrix (list): The empty values where the play will be able to change it for "X" or "O"

    Raises:
        TypeError: Matrix must be a list

    Returns:
        True: the conditions are met
        False: the conditions are not met

    """

    if all(c != ' ' for row in matrix for c in row):
        return True
    return False


def main():
    """
    Initialize the all game.

    Returns:
        The game xd
    """

    p1, p2, board = init()
    player = p1
    columns = '1', '2', '3'
    while True:
        show(board, columns)
        other_player = p1 if player == p2 else p2
        if winning(board):
            print(f'Player {2 if other_player == p2 else 1}, you won!')
            break
        if draw(board):
            print('Its a draw!')
            break
        while True:
            cords = input(f'Player{1 if player == p1 else 2}, please enter the cords to fill (a,2): ').split(',')
            if len(cords) == 2 and cords[0] in columns and cords[1].isdigit() and 1 <= int(cords[1]) <= 3 and \
                    board[columns.index(cords[0])][int(cords[1]) - 1] == " ":
                board[columns.index(cords[0])][int(cords[1]) - 1] = player
                break
            print('Invalid cords!')
        player = other_player


if __name__ == '__main__':
    main()
