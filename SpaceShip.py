Enter file contents hereFull version peer
http://www.codeskulptor.org/#user38_mYYHdxFDvoWyQjd_10.py

my version
http://www.codeskulptor.org/#user38_nHSZR0DfGr_4.py
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
FRICTION = 0.01
score = 0
lives = 3
time = 0
ship_acc = 0.1
ship_angle_vel = 0.05
missile_acc = 3
start = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
#ship_thrust_info = ImageInfo([135, 45],[90,90],35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = angle
        self.acc = float()
        self.angle_vel = float()
        self.image = image
        self.info = info
        self.image_center = self.info.get_center()
        self.image_size = self.info.get_size()
        self.radius = self.info.get_radius()
        self.thrust = False
        self.collision = False
        
    def turn_thrust(self, switch):
        if start:
            self.thrust = switch
            if self.thrust:
                self.acc = ship_acc
                ship_thrust_sound.rewind()
                ship_thrust_sound.play()
            else:
                self.acc = 0
                ship_thrust_sound.pause()
    
    def shoot(self):
        global missiles, start
        if start == True:
            forward = angle_to_vector(self.angle)
            missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
            missile_vel = [self.vel[0] + forward[0] * missile_acc, self.vel[1] + forward[1] * missile_acc] 
            a_missile = Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound)
            missiles.add(a_missile)
        
    def set_collide(self,flag):
        self.collision = True
    
    def update_lives(self):
        global lives, start
        if self.collision == True:
            lives -= 1
            self.collision = False                     

    def draw(self, canvas):    
        if self.thrust == True:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        if start:
            forward = angle_to_vector(self.angle)
            self.angle += self.angle_vel
            self.vel[0] = (self.vel[0] + forward[0] * self.acc) * (1 - FRICTION)
            self.vel[1] = (self.vel[1] + forward[1] * self.acc) * (1 - FRICTION)
            self.pos[0] += self.vel[0] 
            self.pos[1] += self.vel[1]   
            self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
            self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, angle, angle_vel, image, info, sound):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = angle
        self.angle_vel = angle_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.collision = False
        self.remove = False
        
        if sound:
            sound.rewind()
            sound.play()
  
    def draw(self, canvas):
         canvas.draw_image(self.image, self.image_center,self.image_size, self.pos, self.image_size,self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age >= self.lifespan:
            self.remove = True

    def set_collide(self,flag):
        self.collision = True
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def collide(self, a_object):
        object_pos = a_object.get_position()
        object_radius = a_object.get_radius()
        sum_radius = self.radius + object_radius
        distance = dist(self.pos, object_pos)
        if distance <= sum_radius:
           self.set_collide(True)
           a_object.set_collide(True)
           return True
        else:
            return False
        
def group_collide(group, a_object):
    toremove = set([])
    for i in group:
        if i.collide(a_object):
            toremove.add(i)
    group.difference_update(toremove)
    
def group_group_collide(group1, group2):
    global score
    toremove1 = set([])
    toremove2 = set([])
    for i in group1:
        for j in group2:
            i.collide(j)
            if i.collide(j):
                toremove1.add(i)
                toremove2.add(j)
    score += len(toremove1) * 10
    group1.difference_update(toremove1)
    group2.difference_update(toremove2)
    
def process_sprite_group(group, canvas):
    toremove = set([])
    for i in group:
        i.draw(canvas)
        i.update()
        if i.remove == True:
            toremove.add(i)
    group.difference_update(toremove)
        
#def keydown(key):
def keydown(key):
    global ship_acc, ship_angle_vel
    if key == simplegui.KEY_MAP["up"]:
        my_ship.turn_thrust(True)
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -ship_angle_vel
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = ship_angle_vel
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()

def keyup(key):
    global accelerate, angle_vel
    if key == simplegui.KEY_MAP["up"]:
        my_ship.turn_thrust(False)
        ship_thrust_sound.rewind()
    elif key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]:     
        my_ship.angle_vel = 0
    
# timer handler that spawns a rock at a random position and velocity. maxium 12 rocks at a time.   
def rock_spawner():
    global rocks, start
    if start == True and len(rocks) < 12:
        rock_pos = [random.randrange(0, WIDTH),random.randrange(0, HEIGHT)]
        rock_vel = [random.random()*random.choice([-1,1]),random.random()*random.choice([-1,1])] 
        rock_angle = random.random()*random.choice([-1,1])* 2 * math.pi
        rock_angle_vel = random.random()*random.choice([-1,1]) / 10
        a_rock = Sprite(rock_pos, rock_vel, rock_angle, rock_angle_vel, asteroid_image, asteroid_info, None)
    # make sure the rock is not spawn on top of the ship       
        if not a_rock.collide(my_ship):
            rocks.add(a_rock)

def click_start(pos):
    global start,lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not start) and inwidth and inheight:
        start = True
        lives = 3
        score = 0
        my_ship.vel = [0,0]
        soundtrack.play()
    
def draw(canvas):
    global time, a_missile, score, lives, start, rocks, my_ship
    
    # animiate background
    time += 1
    wtime = (time/4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    # end a game if lives are exhausted
    if lives <= 0:
        start = False
        rocks = set([]) 
        my_ship.pos = [WIDTH / 2, HEIGHT / 2]
        soundtrack.rewind()
    # draw splash before start
    if start == False:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), (WIDTH / 2, HEIGHT / 2), splash_info.get_size())
    
    # draw lives and score
    canvas.draw_text('Lives',(20, 30), 25, 'white')
    canvas.draw_text(str(lives),(20, 60), 25, 'white')
    canvas.draw_text('Score',(700, 30), 25, 'white')
    canvas.draw_text(str(score),(700, 60), 25, 'white')
   
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rocks, canvas)
    process_sprite_group(missiles, canvas)
    group_collide(rocks, my_ship)
    group_group_collide(rocks, missiles)
   
    
    # update ship and sprites
    my_ship.update()
    my_ship.update_lives()
 

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprite sets
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rocks = set([])
missiles = set([])   

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click_start)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
