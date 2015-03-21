Enter file contents hereimport simplegui

# define global variables
counter = 0
success = 0
ms100 = 0
residual = 0
state = False

# helper function to format time
def format(x):
    minute = str(x // 600)
    sec = str(x % 600 // 10)
    ms = str(x % 10)
    global residual
    residual = x % 10
    if int(sec) < 10:
        sec = "0" + sec
    return minute + ":" + sec + "." + ms

# define handler function for timer 
# to increment every 0.1 second (100 ms)
def increment():
    global ms100
    ms100 += 1
    return ms100
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global state
    state = True
    
def stop():
    global state
    if state == True:
        timer.stop()
        state = False      
        global counter,residual
        counter = counter + 1
        if residual == 0:
            global success
            success = success + 1
        
def reset():
    global counter, success, ms100
    counter = 0
    success = 0
    ms100 = 0

# define draw handler
# use the following two calls to get the pixel length of the 
# desired output. This is to correctly position the output to the center and 
# upper-right corner of the canvas

# print f.get_canvas_textwidth("0:00.0",45)
# print f.get_canvas_textwidth("0/0",30)

def draw_stopwatch(canvas):
    canvas.draw_text(format(ms100), [(500/2-114/2),300/2], 45, "white")
    canvas.draw_text(str(success)+"/"+str(counter), [500-38-20,30], 30, "green")
    
# create frame and register event handlers
f = simplegui.create_frame("stopwatch", 500, 300)

f.set_draw_handler(draw_stopwatch)

f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)

timer = simplegui.create_timer(100,increment)

# start frame
f.start()



