def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()


def game_over(board, index):
    print_board(board)
    # current_player = board[]
    print("GAME OVER")
    print(board[index], "has won")
    exit()


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if board[0] == board[1] and board[1] == board[2]:
        game_over(board, 0)
    elif board[3] == board[4] and board[4] == board[5]:
        game_over(board, 3)
    elif board[6] == board[7] and board[7] == board[8]:
        game_over(board, 6)
    elif board[0] == board[3] and board[3] == board[6]:
        game_over(board, 0)
    elif board[1] == board[4] and board[4] == board[7]:
        game_over(board, 1)
    elif board[2] == board[5] and board[5] == board[8]:
        game_over(board, 2)
    elif board[0] == board[4] and board[4] == board[8]:
        game_over(board, 0)
    elif board[2] == board[4] and board[4] == board[6]:
        game_over(board, 2)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
