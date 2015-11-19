from random import randint
# Creates a blank board to start with
board = []
# Fills in the blank board above with a 5 x 5 grid of O's
for x in range(5):
	board.append(["O"] * 5)
# 	Concatenates the rows into 5 different rows instead of 1 row of the board repeating 5 times
def print_board(board):
	for row in board:
		print " ".join(row)
# Prints out a heading for the game along with the board we have just made
print ("Let's play Battleship!")
print_board(board)
# Randomly selects 2 integers between 0 and the length of the board minus 1 to get the game into the same set of numbers
def random_row(board):
	return randint(0, len(board) - 1)
def random_col(board):
	return randint(0, len(board[0]) - 1)
# Sets 
ship_row = random_row(board)
ship_col = random_col(board)
# Remove the comments to the 2 lines below to print the coordinates and debug.
#print ship_row
#print ship_col
# Comment again before playing.
for turn in range(4):
# Prints the turn number that you are on
	print ("Turn"), turn + 1
# Where you put your guesses in
	guess_row = int(raw_input("Guess Row (between 0 & 4):"))
	guess_col = int(raw_input("Guess Col (between 0 & 4):"))
# What to do if the guesses are correct	(Break closes the loop)
	if guess_row == ship_row and guess_col == ship_col:
		print ("Congratulations! You sunk my battleship!")
		break
# What to do if the guess is not a valid option
	elif(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
		print ("Oops, that's not even in the ocean.")
# What to do if the guess has already been guessed
	elif(board[guess_row][guess_col] == "X"):
		print ("You guessed that one already.")
# What to do if the guess is incorrect
	else:
		print ("You missed my battleship!")
		board[guess_row][guess_col] = "X"
# Says that if you're on the 4th turn (0,1,2,3), it ends the game
		if turn == 3:
			print ("Game Over")
			break
	print_board(board)
