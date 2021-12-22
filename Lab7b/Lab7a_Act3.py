# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Maxine Woods, Katherine Stevens, Michael Tyrrell, Yida Zou
# Section: 462
# Assignment: Lab7a_Act3.py
# Date: 10 October 2020

# INSTRUCTIONS: Please enter the column and row using 0-7 to choose the piece you want to move. 0-7 from top to bottom and 0-7 from left to right. Do the same for the space that you want to move the piece to. For example, if you want to move the piece from the space column 0, row 1 to the space column 0, row 7, enter it in the format: 01 07. Type "stop" when you are done playing.  
board = [["R","N","B","Q","K","B","N","R"], ["P","P","P","P","P","P","P","P"], [".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".","."], ["p", "p", "p", "p", "p", "p", "p", "p", ], ["r","n","b","q","k","b","n","r"]]

#01 07

for i in range(len(board)):#to print the board with pieces use 2 loops
  for j in range(len(board[i])):
    print(board[i][j], end="")
  print()


while True:
  move = input("Please enter your move: ")
  if move == "stop": #stop the game when they input stop
    break
  a1 = int(move[1:2])
  b1 = int(move[0:1])
  a2 = int(move[4:5])
  b2 = int(move[3:4])
  if board[a1][b1] != ".":
    board[a2][b2] = board[a1][b1]
    board[a1][b1] = "."
  else:#print error if they choose empty space to move from
    print("ERROR: there is not a piece on that spot")
  for i in range(len(board)): #print the new board after move
    for j in range(len(board[i])):
      print(board[i][j], end="")
    print()



