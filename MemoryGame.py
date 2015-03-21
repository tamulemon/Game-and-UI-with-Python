Enter file contents hereimport simplegui	
import random
ls1 = ls2 = range(0,8)
ls = ls1 + ls2
turns = 0
state = 0 
index1 = index2 = 0

exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# new game
def new_game():
    global state, turns
    random.shuffle(ls)
    turns = state = 0
    for i in range(0,len(ls)):
        exposed[i] = False
                   
# define event handlers
def mouseclick(pos):
    global state, index1, index2, turns
    
    def set_index():
        for i in range(0,len(ls)):
            if pos[0] in range (50*i, 50*(i+1)+1) and exposed[i] == False:
                exposed[i] = True
                return int(i)
    
    if state == 0:
        state = 1
        index1 = set_index() 
        #print "index1", index1
    elif state == 1:
        state = 2
        turns += 1
        index2 = set_index()
        #print "index2",index2
    else:
        state = 1
        if ls[index1] == ls[index2]:
            exposed[index1] = exposed[index2] = True
        else: 
            exposed[index1] = exposed[index2] = False
        index1 = set_index()
        #print "index1", index1
    #print "state",state, "turns",turns
    label.set_text("Turns = " + str(turns))
    
# draw cards or number    
def draw(canvas):
    for i in range(0,len(ls)):
        x = ls[i]
        canvas.draw_line((50*i, 0), (50*i, 99), 2, "white")
        if exposed[i] == True:
            canvas.draw_text(str(x), (i*50+3,85),90, "white")
        else:
            canvas.draw_polygon([(50*i,0), (50*(i+1),0), (50*i, 99), (50*(i+1),99)], 2, "white", "green")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
import simplegui	
import random
ls1 = ls2 = range(0,8)
ls = ls1 + ls2
turns = 0
state = 0 
exposed_index = []

# all cards are covered
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# new game
def new_game():
    global state, turns,exposed_index 
    random.shuffle(ls)
    turns = state = 0
    exposed_index = []
    for i in range(0,len(ls)):
        exposed[i] = False
    label.set_text("Turns = " + str(turns))
    
# define event handlers
def mouseclick(pos):
    global state, turns, exposed_index
    
    # a function to find which card is clicked
    def set_index():
        for i in range(0,len(ls)):
            if pos[0] in range (50*i, 50*(i+1)+1) and exposed[i] == False:
                exposed[i] = True
                return int(i)
    index = set_index()
    
    # state control
    if state == 0:
        state = 1
        exposed_index.append(index) 
        #print exposed_index
    elif state == 1:
        if index != None:
            exposed_index.append(index)
            state = 2
            turns += 1   
        #print exposed_index
    else:
        if index != None and index not in exposed_index:
            if ls[exposed_index[0]] == ls[exposed_index[1]]:
                exposed[exposed_index[0]] = exposed[exposed_index[1]] = True
            elif ls[exposed_index[0]] != ls[exposed_index[1]]:
                exposed[exposed_index[0]] = exposed[exposed_index[1]] = False
            exposed_index = []
            exposed_index.append(index)
            state = 1
        #print exposed_index
    #print "state",state, "turns",turns
    label.set_text("Turns = " + str(turns))
    
# draw cards or number    
def draw(canvas):
    for i in range(0,len(ls)):
        x = ls[i]
        canvas.draw_line((50*i, 0), (50*i, 99), 2, "white")
        if exposed[i] == True:
            canvas.draw_text(str(x), (i*50+3,85),90, "white")
        else:
            canvas.draw_polygon([(50*i,0), (50*(i+1),0), (50*i, 99), (50*(i+1),99)], 2, "white", "green")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()

