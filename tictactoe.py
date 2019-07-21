import turtle
import time
import random
import math

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

width = turtle.window_width()
height = turtle.window_height()

def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    """
    turtle.clear()
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.up()
    turtle.right(90)
    turtle.color("black")
    for i in [-width/6,width/6]: # draws vertical lines of grid
        turtle.goto(i,height/2)
        turtle.down()
        turtle.forward(height)
        turtle.up()
    turtle.left(90)
    for i in [-height/6,height/6]: # draws horizontal lines of grid
        turtle.goto(-width/2,i)
        turtle.down()
        turtle.forward(width)
        turtle.up()
    turtle.pensize(5)
    count = 0
    for position in board:
        if position == "O": # draws 'O' for user move
            counter1 = 0
            counter2 = 0
            for i in [0,3,6]:
                for j in [0,1,2]:
                    if count == i + j:
                        x1 = -width/3 + (counter1 - 3 * counter2) * width/3
                    counter1 += 1
                counter2 += 1
            counter3 = 0
            counter4 = 0
            for i in [0,1,2]:
                for j in [0,3,6]:
                    if count == i + j:
                        y1 = height/6 - (counter3 - 3 * counter4) * height/3
                    counter3 += 1
                counter4 += 1
            turtle.goto(x1,y1)
            turtle.color("pink")
            turtle.down()
            turtle.circle(height/6)
            turtle.up()
        if position == "X": # draws 'X' for computer move
            counter1 = 0
            counter2 = 0
            for i in [0,3,6]:
                for j in [0,1,2]:
                    if count == i + j:
                        x2 = -width/2 + (counter1 - 3 * counter2) * width/3
                        x3 = -width/6 + (counter1 - 3 * counter2) * width/3
                    counter1 += 1
                counter2 += 1
            counter3 = 0
            counter4 = 0
            for i in [0,1,2]:
                for j in [0,3,6]:
                    if count == i + j:
                        y2 = height/2 - (counter3 - 3 * counter4) * height/3
                    counter3 += 1
                counter4 += 1
            turtle.goto(x2,y2)
            turtle.right(45)
            turtle.down()
            turtle.color("yellow")
            turtle.forward((height/3)*math.sqrt(2))
            turtle.up()
            turtle.goto(x3,y2)
            turtle.right(90)
            turtle.down()
            turtle.forward((height/3)*math.sqrt(2))
            turtle.up()
            turtle.left(135)
        count += 1
    turtle.update()
    
def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. The
    code translates the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    holder = 0
    position = 0
    for i in [-width/2, -width/6, width/6]:
        if not i <= x <= i + (width/3): # checks for range of x-coordinate
            holder += 1
        else:
            position = holder
            if (-height/6) <= y <= (height/6): # checks for range of y-coordinate
                position += 3
            elif (-height/2) <= y <= (-height/6):
                position += 6
    if board[position] == "_": # checks if the position is unoccupied
        board[position] = "O"
    return True

turtle.onscreenclick(do_user_move)

def test(init, add, piece, board = the_board):
    """
    signature: list(int), list(int), str -> bool
    Tests whether there is a horizontal, vertical,
    or diagonal pattern. Returns True if pattern
    exists, False otherwise.
    """
    for i in init:
        if board[i] == board[i+add[0]] == board[i+add[1]] == piece: # checks for a horizontal, vertical or diagonal pattern
            turtle.goto(0,0)
            turtle.color("black")
            if piece == "X":
                phrase = "Computer won!"
            else:
                phrase = "You won!"
            turtle.write(phrase, True, align = "center",font=("Arial",30,"normal")) # prints message to the turtle screen
            return True
    return False

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    total = 0
    for i in range(9): # checks for a stalemate
        if board[i] != "_":
            total += 1
    if total == 9:
        turtle.goto(0,0)
        turtle.color("black")
        turtle.write("No winner!", True, align = "center", font=("Arial",30,"normal")) # prints message to the turtle screen
        return True
    count = 0
    tests = [
        test([0,3,6],[1,2],"X"),
        test([0,3,6],[1,2],"O"),
        test([0,1,2],[3,6],"X"),
        test([0,1,2],[3,6],"O"),
        test([0],[4,8],"X"),
        test([0],[4,8],"O"),
        test([2],[2,4],"X"),
        test([2],[2,4],"O"),
        ]
    for gameOver in tests: # returns True if pattern exists
        if gameOver:
            count += 1
    if count > 0:
        return True
    return False # returns False if pattern does not exist

def comp(init, add, piece, board = the_board):
    """
    signature: list(int), list(int), str -> str
    Tests if computer could either win in the
    next move or block a user from winning
    in the next move.
    """
    for i in init:
        holder = 0
        for addition in add:
            if board[i + addition] == piece:
                holder += 1
            else:
                position = i + addition
        if holder == 2 and board[position] == "_":
            return str(position) # returns string value of the winning position if winning is possible in the next move
    return "a" # returns the non-numeric string value of "a" otherwise

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    s = comp([0,3,6],[0,1,2],"X") + \
    " " + comp([0,1,2],[0,3,6],"X") + \
    " " + comp([0],[0,4,8],"X") + \
    " " + comp([2],[0,2,4],"X") + \
    " " + comp([0,3,6],[0,1,2],"O") + \
    " " + comp([0,1,2],[0,3,6],"O") + \
    " " + comp([0],[0,4,8],"O") + \
    " " + comp([2],[0,2,4],"O")
    output = s.split()
    newoutput = []
    for char in output:
        if char.isdigit(): # only includes numerical values (when winning is possible in the next move)
            newoutput.append(char)
    if len(newoutput) > 0: # checks if winning is possible in the next move
        position = int(newoutput[0])
        board[position] = "X" # changes value of the first possible winning position (to ensure that computer prioritizes winning over blocking user)
        return
    occupied = True
    while occupied: # if winning is not possible in the next move, choose a random position for computer move that is unoccupied
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "X"
            occupied = False
        
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()
main()
