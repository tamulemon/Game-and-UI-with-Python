Enter file contents here# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper function
def name_to_number(name):
    if name == "rock":
        number = 0
        #return number
    elif name == "Spock":      
        number = 1
        #return number
    elif name == "paper": 
        number = 2
        #return number
    elif name == "lizard":
        number = 3
        #return number
    elif name == "scissors":
        number = 4
        #return number
    else:
        print "Invalid player input!"
        number = 100
    return number
        
    

# helper function        
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Invalid input."
    return name

def rpsls(player_choice): 
    import random 
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    if player_number <100:
        # note here should use (0,5), not (0,4)
        computer_number = random.randrange(0,5)
        computer_play = number_to_name(computer_number)
        print "Computer chooses", computer_play
        diff = player_number-computer_number
        remainder = diff%5
        if (remainder == 1) or (remainder == 2):
            print "Player wins!"
        elif (remainder == 3) or (remainder == 4):
            print "Computer wins!"
        elif remainder == 0:
            print "Play and computer tie!"
#    else:
#        print "invalid user input."
    print ''
    

rpsls("paper")
rpsls("rock")
rpsls("Spock")
rpsls("lizard")
rpsls("scissors")
#Test an invalid play
rpsls("abcd")
