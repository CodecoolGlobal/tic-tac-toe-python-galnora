# def init_board():
#     """Returns an empty 3-by-3 board (with .)."""
#     board = []
#     return board



def get_move(board, player, row_dictionary):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    acceptable_rows = ['A','a','B','b','C','c']        
    acceptable_cols = [1,2,3] 
    return_message = False
    

    while return_message is False:
        cordinates = input ("cordinates ((A-C)(1-3)):")
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

board = [['.','.','.'],['.','.','.'],['.','.','.']]
player = 'X'
row_dictionary= {'a':0,'b':1,'c':2}
row, col = get_move(board,player,row_dictionary)


# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     row, col = 0, 0
#     return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if player == '0':
        board[row_dictionary[row]][col-1] = '0'
    else:
        board[row_dictionary[row]][col-1] = 'X'
    return board

print(mark(board,player,row,col))    


# def has_won(board, player):
#     """Returns True if player has won the game."""
#     return False


# def is_full(board):
#     """Returns True if board is full."""
#     return False


# def print_board(board):
#     """Prints a 3-by-3 board on the screen with borders."""
#     pass


# def print_result(winner):
#     """Congratulates winner or proclaims tie (if winner equals zero)."""
#     pass


# def tictactoe_game(mode='HUMAN-HUMAN'):
#     board = init_board()

#     # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
#     print_board(board)
#     row, col = get_move(board, 1)
#     mark(board, 1, row, col)

#     winner = 0
#     print_result(winner)


# def main_menu():
#     tictactoe_game('HUMAN-HUMAN')


# if __name__ == '__main__':
#     main_menu()
