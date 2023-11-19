# Creating a 3x3 2D array
array_2d = [
    [" ", "A", "B", "C"],
    ["1", " ", " ", " "],
    ["2", " ", " ", " "],
    ["3", " ", " ", " "]
]

def checkForWinner(board, marker):
    # Check rows
    for row in board[1:]:
        if row[1:] == [marker, marker, marker]:
            return True

    # Check columns
    for col in range(1, 4):
        if [board[i][col] for i in range(1, 4)] == [marker, marker, marker]:
            return True

    # Check diagonals
    if [board[i][i] for i in range(1, 4)] == [marker, marker, marker] or \
       [board[i][4-i] for i in range(1, 4)] == [marker, marker, marker]:
        return True

    return False

def isBoardFull(board):
    for row in board[1:]:
        for cell in row[1:]:
            if cell == " ":
                return False
    return True

def get_empty_cells(board):
    return [(i, j) for i in range(1, 4) for j in range(1, 4) if board[i][j] == " "]
    

def minimax(board, depth, maximizingPlayer):
    scores = {'X': -1, 'O': 1, 'tie': 0}

    if checkForWinner(board, 'X'):
        return scores['X'] 

    if checkForWinner(board, 'O'):
        return scores['O']

    if isBoardFull(board):
        return scores['tie']
    
    if maximizingPlayer:
        max_eval = float('-inf') #iniltiziers 
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        
        return max_eval

    else:
        min_eval = float('inf') #iniltiziers 
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True) 
            board[i][j] = ' '
            min_eval = min(min_eval, (eval))
        return min_eval
    
    
    
    
def findBestMove(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    # If it's the first move, set the move to B2


    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        print(f"Eval for move {chr(j + ord('A') - 1)}{i}: {move_val}")
        currentMove = f"{chr(j + ord('A') - 1)}{i}"
        if currentMove == "B2":
            move_val = 1


        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move


# Function to get user input and validate errors
def get_input(player):
    if player == 1:
        marker = "X"
        placement = input(f"Player {player}, pick a grid location to place your {marker}: ")
    else:
        marker = "O"
        print(f"Player {player} is thinking...")
        move = findBestMove(array_2d)
        placement = f"{chr(move[1] + ord('A') - 1)}{move[0]}"

    # Check if the input is in the valid format (e.g., A1, C2)
    if len(placement) == 2 and placement[0].isalpha() and placement[1].isdigit():
        col = ord(placement[0].upper()) - ord("A") + 1
        row = int(placement[1])

        # Check if the selected cell is within the valid range
        if 1 <= row <= 3 and 1 <= col <= 3:
            return placement, marker

    print("Invalid input. Please enter a valid grid location like A1, B2, etc.")
    return get_input(player)

# Updates the game board based on user input
def update_board(user_input, marker):
    upperCol = user_input[0].upper()
    row = int(user_input[1])  # Extract the row index (convert to integer)
    col = ord(upperCol) - ord("A") + 1  # Extract the column index (convert letter to ASCII and adjust)

    # Check if the selected cell is empty
    if array_2d[row][col] == " ":
        array_2d[row][col] = marker
    else:
        print("Invalid move. Cell is already occupied. Try again.")

# Prints the game
def print_game():
    for row in array_2d:
        for element in row:
            print(element, end=' ')
        print()  # Move to the next line after printing each row

# Main game loop, runs until spots are filled
def start_game():
    welcome = '''
Welcome to Ryan's Tic Tac Toe.

The game is simple. Each player will have a turn placing either an X or O in a location of their choosing.
The goal of the game is to get three of your markers either up, down, or diagonal.
'''
    print(welcome)

    # Play until all spots are filled
    for turn in range(1, 10):  # There are 9 spots on the board
        print_game()
        user_input, marker = get_input(turn % 2 + 1)  # Alternate between player 1 and player 2
        update_board(user_input, marker)

        if checkForWinner(array_2d, marker):
            print_game()
            print(f"Game over. Player {turn % 2 + 1} ({marker}) wins!")
            return

    print("Game over. It's a tie!")

# Start the game
start_game()
