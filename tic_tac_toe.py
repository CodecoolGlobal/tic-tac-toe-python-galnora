def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    win = True

    for row in board:
        if row[0] == player:
            for i in range(1,3):
                if row[i] != player:
                    win = False
    
    for col in range(0,3):
        if col[0] == player:
            for i in range(1,3):
                if col[i] != player:
                    win = False


    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
    return win  


def is_full(board):
    is_board_full = True
    for row in board:
        for position in row:
            if position == '.':
                is_board_full = False
                break
    return is_board_full

# print(is_full([ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]))
# print(is_full([ [ '','','' ],[ '','','' ],[ '','','' ] ]))
print(is_full([ [ '','.','' ],[ '','','' ],[ '','','' ] ]))

def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
