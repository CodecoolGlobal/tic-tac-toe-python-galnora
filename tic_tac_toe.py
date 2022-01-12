def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    return board

def get_move(board, row_dictionary):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    acceptable_rows = ['A','a','B','b','C','c']        
    acceptable_cols = [1,2,3] 
    return_message = False
    while return_message is False:
        cordinates = input ("cordinates ((A-C)(1-3)) or 'quit' for quit:")
        if not cordinates == "quit":
            if len(cordinates) == 2:
                cordinates_list=[]
                for n in cordinates:
                    cordinates_list.append(n)
                row = cordinates_list[0].lower()
                try:
                    col = int(cordinates_list[1])
                except ValueError:
                    continue
                if row in acceptable_rows and col in acceptable_cols:
                    if board[row_dictionary['a']][col-1] == '.':
                        return row, col
                    if board[row_dictionary['b']][col-1] == '.':
                        return row, col
                    if board[row_dictionary['c']][col-1] == '.':
                        return row, col
        else:
            goodbye = "Goodbye"
            return goodbye
# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     row, col = 0, 0
#     return row, col


def mark(board, player, row, col, row_dictionary):
    """Marks the element at row & col on the board for player."""
    if player == '0':
        board[row_dictionary[row]][col-1] = '0'
    else:
        board[row_dictionary[row]][col-1] = 'X'
    return board

def has_won(board, player):
    win = False
    
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            win = True

    for i in range(len(board)):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            win = True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            win = True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            win = True

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
# print(is_full([ [ '','.','' ],[ '','','' ],[ '','','' ] ]))


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    abc = [ 'A', 'B', 'C' ]
    print( '  1   2   3 ')
    for row in range(len(board)):
        print(abc[row], " | ".join(board[row]))
        if row < 2:
            print(' ---+---+---')
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    won = False
    row_dictionary= {'a':0,'b':1,'c':2}
    player_value = 0
    while won:
        player_value += 1
        if player_value % 2 == 1:
            player = 'X'
        else:
            player = '0'
        if len(get_move(board, row_dictionary)) == 1:
            return print(get_move(board, row_dictionary))
        else:
            row, col = get_move(board, row_dictionary)
        mark = mark(board, player, row, col, row_dictionary)
        won = has_won(board, player)
        is_full = is_full(board)
        if won is True or is_full is True:

        
# tictactoe_game()
        

 
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
   




#     print_board(board)
#     row, col = get_move(board, 1)
#     mark(board, 1, row, col)

#     winner = 0
#     print_result(winner)


# def main_menu():
#     tictactoe_game('HUMAN-HUMAN')


# if __name__ == '__main__':
#     main_menu()
