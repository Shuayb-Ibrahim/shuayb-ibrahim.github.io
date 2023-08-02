from random import randint

def display_board(board):
    rows = "+-------"
    print(rows * 3, end="+\n")
    for i in range(0, 9, 3):
        print("|       " * 3, end="|\n")
        print("|   ", board[i], "   |" + \
              "   ", board[(i + 1)], "   |" + \
              "   ", board[(i + 2)], "   |", sep="")
        print("|       " * 3, end="|\n")
        print(rows * 3, end="+\n")

def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    print("Available fields:", free_fields)
    pick = int(input("Enter your move: "))

    while pick not in free_fields:
        pick = int(input("Invalid entry, Enter your move: "))
    else:
        board[pick-1] = "O"
    display_board(board)

def make_list_of_free_fields(board):
    free_fields = []
    for f in range(len(board)):
        if type(board[f]) != int:
            continue
        else:
            free_fields.append(board[f])
    return free_fields



def victory_for(board, sign):
    if board[0] == sign and (board[0] == board [1] == board[2] or board[0] == board [3] == board[6]):
        return True
    elif board[4] == sign and (board[4] == board[3] == board[5] or board[4] == board[1] == board[7]):
        return True
    elif board[8] == sign and (board[8] == board[7] == board[6] or board[8] == board[5] == board[2]):
        return True
    elif board[4] == sign and (board[4] == board[0] == board[8] or board[4] == board[2] == board[6]):
        return True
    else:
        return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    print(free_fields)
    pick = randint(0,len(free_fields)-1)
    print(pick)
    board[free_fields[pick]-1] = "X"
    display_board(board)


board = [i+1 for i in range(9)]
board[4] = "X"
display_board(board)

enter_move(board)
draw_move(board)

for i in range(0,8):
    if make_list_of_free_fields(board) == []:
        print("This game has ended as a Draw")
        break
    elif i % 2 == 0:
        enter_move(board)
        if victory_for(board, "O"):
            print("You win!")
            break
    else:
        draw_move(board)
        if victory_for(board, "X"):
            print("You lose :(")
            break
