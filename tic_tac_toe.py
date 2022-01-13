from colorama import Fore
import random


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
    return board

def get_move():
    cordinates = input("cordinates ((A-C)(1-3)) or 'quit' for quit:\n")
    return cordinates

def get_ai_move_easy_to_lose(board, player):
    """Returns the coordinates of a valid move for player on board."""
    if player == 'X':
        first_step = ['c1']
        second_step_corner = ['a3','b3']
        second_step = ['a1','c3']
        third_step_corner_a3 = ['a1','a2','b1']
        third_step_corner_b3 = ['a3','c2','c3']
        third_step = ['b2','c3']
        forth_step = ['a3','b1','c2']
        first_return = random.choice(first_step)
        if board[1][1] == '0':
            second_return = random.choice(second_step_corner)
            if board[0][2] == 'X':
                third_return = random.choice(third_step_corner_a3)
            else:
                third_return = random.choice(third_step_corner_b3)
            forth_return = random.choice(forth_step)
        else:
            second_return = random.choice(second_step)
            third_return = random.choice(third_step)
            forth_return = random.choice(forth_step)
        
        return first_return, second_return, third_return, forth_return

def ai_win(board,player):
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == '.':
            if i == 0:
                return f"a",3
            if i == 1:
                return f"b",3
            if i == 2:
                return f"c",3
        elif board[i][0] == player and board[i][2] == player and board[i][1] == '.':
            if i == 0:
                return f"a",2
            if i == 1:
                return f"b",2
            if i == 2:
                return f"c",2
        elif board[i][1] == player and board[i][2] == player and board[i][0] == '.':
            if i == 0:
                return f"a",1
            if i == 1:
                return f"b",1
            if i == 2:
                return f"c",1

    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == '.':
            return f"c",j+1
        elif board[0][j] == player and board[2][j] == player and board[1][j] == '.':
            return f"b",j+1
        elif board[1][j] == player and board[2][j] == player and board[0][j] == '.':
            return f"a",j+1
 
def get_move_format (cordinates, board, row_dictionary):
    acceptable_rows = ['A','a','B','b','C','c']        
    acceptable_cols = [1,2,3]
    invalid_cordinates = "Invalid cordinates, please try ((A-C)(1-3))\n"
    taken_cordinates = "This cordinate isn't free, please try an other one\n"
    if not cordinates == "quit":
        if len(cordinates) == 2:
            cordinates_list=[]
            for n in cordinates:
                cordinates_list.append(n)
            try:
                col = int(cordinates_list[1])
                row = cordinates_list[0].lower()
                if row in acceptable_rows and col in acceptable_cols:
                    if board[row_dictionary[row]][col-1] == '.':
                        return row, col
                    else: 
                        return False, taken_cordinates 
                else:
                    return False, invalid_cordinates
            except ValueError:
                return False, invalid_cordinates
        else: 
            return False, invalid_cordinates
    else:
        goodbye = "Goodbye"
        return goodbye

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

def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    abc = [ 'A', 'B', 'C' ]
    print( '\n  1   2   3 ')
    for row in range(len(board)):
        print(abc[row], " | ".join(board[row]))
        if row < 2:
            print(' ---+---+---')

def print_result(board,player):
    """Congratulates winner or proclaims tie (if winner equals zero)."""

    if has_won(board, player) and player == 'X':
        return print(Fore.RED + "X has won!\n")
    elif has_won(board, player) and player == '0':
        return print(Fore.BLUE + "0 has won!\n")
    elif is_full(board):
        return print(Fore.GREEN + "It's a tie!\n")

def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    won = False
    row_dictionary= {'a':0,'b':1,'c':2}
    player_value = 0

    while not won:
        print_board(board)

        player_value += 1
        input = [False,' ']
        while input[0] is False:
            if player_value % 2 == 1:
                player = 'X'
                ai_win_cordinates = ai_win(board,player)
                ai_lose_cordinates = ai_win(board,'0')
                if ai_win_cordinates != None:
                    cordinates = ai_win_cordinates
                elif ai_lose_cordinates != None:
                    cordinates = ai_lose_cordinates
                else:
                    cordinates = get_ai_move_easy_to_lose(board,player)[player_value // 2]
            else:
                player = '0'
                cordinates = get_move()
            input = get_move_format(cordinates, board, row_dictionary)
            if input[0] == False:
                print(input[1])
        if len(input) == 2:     
            row, col = input
            board = mark(board, player, row, col, row_dictionary)
            won = has_won(board, player)
            is_full_value = is_full(board)
            if won is True or is_full_value is True:
                return print_board(board), print_result(board,player)

        else:
            return print(input)
tictactoe_game(mode='HUMAN-HUMAN')
        

 
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

