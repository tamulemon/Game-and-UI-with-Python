Enter file contents hereimport simplegui
import random
import math

# define global variables 
num_range = 100
counter = int()
secret_number = int()

# define helper functions
def new_game():
    global num_range
    global secret_number    
    global counter
    secret_number = random.randrange(0,num_range)
    counter = int(math.ceil(math.log(num_range,2)))
    print ""
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", counter 

# define event handlers
def range100():
    ''' button that changes the range to [0,100) and starts a new game''' 
    global num_range
    num_range = 100
    new_game()
   
def range1000():
    '''button that changes the range to [0,1000) and starts a new game''' 
    global num_range 
    num_range = 1000
    new_game()

def input_guess(guess):
    '''user input number'''
    global counter
    user_guess=int(guess)
    print ""
    print "Guess was", user_guess
    counter = counter - 1
    print "Number of remaining guesses is", counter
    if counter > 0: 
        if secret_number > user_guess:
            print "Higher!"            
        elif secret_number < user_guess:
            print "Lower!"
        else:
            print "Correct!"
            new_game()
    elif counter == 0:
        if secret_number == user_guess:
            print "Correct!"
            new_game()
        else:
            print "You ran out of guesses.  The number was", secret_number
            new_game()
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

# create control elements and register event handlers
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
f.start()
new_game()

