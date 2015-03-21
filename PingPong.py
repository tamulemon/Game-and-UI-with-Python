
# http://www.codeskulptor.org/#user38_Ii5WHXOysf_5.py


#Version 1
#Paddle keeps moving at a constant speed and only stops when an opposite key is pressed (harder to control). Press the opposite key again, then paddle start moving at opposite direction. 
#http://www.codeskulptor.org/#user38_8Shxn3aKtp_7.py

#Version 2
#Final version, change paddle behavior. Paddle only moves when a key is pressed down. When key is released, paddle stops moving. 
#http://www.codeskulptor.org/#user38_8Shxn3aKtp_10.py




# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# define right bottom corner of paddle1 to be paddle1_pos
# define left bottom corner of paddle2 to be paddle2_pos
# the initial position for both paddles are in the middle
paddle1_vel = 0
paddle2_vel = 0

paddle1_pos = HEIGHT/2 + HALF_PAD_HEIGHT 
paddle2_pos = HEIGHT/2 + HALF_PAD_HEIGHT 

score1 = 0 
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT :
        ball_vel[0] = 1
        ball_vel[1] = -1
#        ball_vel[0] = random.randrange(120, 240)/60
#        ball_vel[1] = -random.randrange(60, 180)/60
    else:
        ball_vel[0] = -1
        ball_vel[1] = -1
#        ball_vel[0] = -random.randrange(120, 240)/60
#        ball_vel[1] = -random.randrange(60, 180)/60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2  
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT/2 + HALF_PAD_HEIGHT
    paddle1_vel = paddle2_vel = 0
    spawn_ball(RIGHT)
# define restart button
def button_handler():
    new_game()
    
# draw elements on the canvas
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")   
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # ball bounce on paddles and bounce on top and bottom of the screen
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
       if (ball_pos[1] <= paddle1_pos <= (ball_pos[1] + PAD_HEIGHT)):
           ball_vel[0] = -ball_vel[0]
           ball_vel = [x * 1.1 for x in ball_vel]
       else:
            score2 += 1
            ball_vel = [0, 0]
            spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS):
        if (ball_pos[1] <= paddle2_pos <= (ball_pos[1] + PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]
            ball_vel = [x * 1.1 for x in ball_vel]
        else:
            score1 += 1
            ball_vel = [0, 0]
            spawn_ball(LEFT)
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]   

    # update paddle's vertical position, keep paddle on the screen
 #    if paddle1_pos <= PAD_HEIGHT and paddle1_vel < 0: 
#       paddle1_vel = 0
#    elif paddle1_pos >= HEIGHT and paddle1_vel > 0:
#        paddle1_vel = 0
#    if paddle2_pos <= PAD_HEIGHT and paddle2_vel < 0: 
#       paddle2_vel = 0
#    elif paddle2_pos >= HEIGHT and paddle2_vel > 0:
#        paddle2_vel = 0
#    paddle2_pos += paddle2_vel
#    paddle1_pos += paddle1_vel   

# This is also ok
    if paddle1_pos + paddle1_vel in range (PAD_HEIGHT-1, HEIGHT + 2):
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel in range (PAD_HEIGHT-1, HEIGHT + 2):
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos - PAD_HEIGHT),(HALF_PAD_WIDTH,paddle1_pos),PAD_WIDTH,"white")
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - PAD_HEIGHT),(WIDTH-HALF_PAD_WIDTH, paddle2_pos),PAD_WIDTH,"white")     
    
    # draw scores
    canvas.draw_text(str(score1),(WIDTH/4, HEIGHT/8), 30, "white")
    canvas.draw_text(str(score2),(WIDTH*0.75, HEIGHT/8), 30, "white")
    
# Version 1 define key to control paddles    
def keydown(key):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    acc = 1 
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
        
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
button1 = frame.add_button("Restart", button_handler,200)

# start frame
frame.start()
new_game()




Version 2
def keydown(key):
    global paddle1_vel, paddle2_vel 
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 7
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 7
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 7
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 7
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("Restart", button_handler,200)

# start frame
frame.start()
new_game()
