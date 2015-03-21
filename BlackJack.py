# Enter file contents herehttp://www.codeskulptor.org/#user38_6WhBHALztmmGqqK.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = str()

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = "Hand contains "
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + " "
        return s
          
    def add_card(self, card):
        return self.cards.append(card)

    def get_value(self):
        rank = []
        self.hand_value = 0
        for i in range(len(self.cards)):
            rank.append(self.cards[i].get_rank())
        for j in range(len(rank)):
            self.hand_value += VALUES[rank[j]] 
        if ('A' in rank) and (self.hand_value + 10 <= 21):
            return self.hand_value +10
        else:
            return self.hand_value
   
    def draw(self, canvas, pos1):
        for card in self.cards:
            card.draw(canvas, [50 + 100 * self.cards.index(card),pos1])    
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))  

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal_card(self):
        card = self.cards[-1]
        self.cards.pop()
        return card
    
    def __str__(self):
        s = "The deck contains "
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + " "
        return s
player_hand = Hand()
dealer_hand = Hand()
current_deck = Deck()
#define event handlers for buttons
def deal():
    global outcome, in_play, current_deck, player_hand, dealer_hand, message, score
    outcome = ""
    message = str()
    player_hand = Hand()
    dealer_hand = Hand()
    current_deck = Deck()
    current_deck.shuffle()
    print current_deck 
    for i in range(2):
        player_hand.add_card(current_deck.deal_card())
        dealer_hand.add_card(current_deck.deal_card())
        i += 1
    message = "Hit or Stand?"
    in_play = True
    print player_hand,"\n", dealer_hand,"\n", current_deck,"\n",message,"\n",score
        
def hit():
    global outcome, in_play, current_deck, player_hand, dealer_hand, message, score
    if in_play:
        player_hand.add_card(current_deck.deal_card())
        player_value = player_hand.get_value()
        if player_value > 21:
            in_play = False
            message = "You have busted"
            score -= 1 
        else:
            message = "Hit or Stand?"
    print player_hand,"\n", dealer_hand,"\n", current_deck,"\n",message,"\n",score
            
def stand():
    global outcome, in_play, current_deck, player_hand, dealer_hand, message, score
    if in_play:
        while dealer_hand.get_value() < 17:
             dealer_hand.add_card(current_deck.deal_card())
    if 21 >= dealer_hand.get_value() >= player_hand.get_value():
        message = "You have lost"
        score -= 1
    else:
        message = "You have won"
        score += 1
    in_play = False
    print player_hand,"\n", dealer_hand,"\n", current_deck,"\n",message,"\n",score
# draw handler    
def draw(canvas):
    global outcome, in_play, current_deck, player_hand, dealer_hand, message, score
    dealer_hand.draw(canvas, 200)     
    player_hand.draw(canvas, 400)
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50+72/2, 200+96/2], CARD_BACK_SIZE)
    canvas.draw_text('Dealer', (50,150), 25, 'white')
    canvas.draw_text('Player', (50,350), 25, 'white')
    canvas.draw_text('Score '+ str(score), (450,50), 25, 'white')
    canvas.draw_text(message, (350,350), 25, 'white')
    canvas.draw_text('BLACKJACK', (200,100), 40, 'yellow')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


deal()
frame.start()


