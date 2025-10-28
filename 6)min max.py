import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('---------')
    print()

# Check if board is full
def is_full(brd):
    return ' ' not in brd

# Check winner
def check_winner(brd, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combinations:
        if all(brd[i] == player for i in combo):
            return True
    return False

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Player move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken! Try again.")
        else:
            print("Invalid input! Enter a number from 1 to 9.")

# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    print_board()
    while True:
        player_move()
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        print("AI's turn:")
        ai_move()
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

main()
