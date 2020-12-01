c = color(0)
x = 0.0
y = 100.0
speed = 1
totalPts = 300
steps = totalPts + 1

car1text = 'Car   1'
car2text = 'Car   2'
welcome = 'Look for random change in Car 2. Press a key to change Car 1' 

class Car(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c   
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed                        
                                                
    def display(self):
        rectMode(CENTER)
        fill(self.c)
        rect(self.xpos, self.ypos,
            20, 10)
        
    def event(self):
        self.c = color(255, 255, 0)

    def drive(self):
        self.xpos += self.xspeed
        if self.xpos > width:
            self.xpos = 0


class Rock(object):
    def __init__(self, c, xpos, ypos):
        self.c = c   
        self.xpos = xpos
        self.ypos = ypos                    
                                                
    def display(self):
        rectMode(CENTER)
        fill(self.c)
        circle(self.xpos, self.ypos, 20)

    def drive(self):
        if self.xpos > width:
            self.xpos = 0
            



myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 150, 1)

def setup():
    size(500, 500)
    background(255)
    global myRock1
    global myRock2
    
    
    
    global myRock3
    myRock1 =Rock(color(102, 51, 0),random(width), random(height))
    myRock2 =Rock(color(102, 51, 0),random(width), random(height))
    myRock3 =Rock(color(102, 51, 0),random(width), random(height))
    
    
frames = 0

target = int (random(170, 1200))
        
def draw():
    global frames, target
    background(255)
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
    myRock1.display()
    myRock2.display()
    myRock3.display()
    
    textSize(15)
    text(car1text, 0,100)
    text(car2text, 0,150)
    text(welcome, 0,300)
    
    if frames == target:
         myCar2.event()
    
    frames = frames + 1
#    print(frames, target)

#    results = [Person(**row) for row in data]
#    print(results)
    
    
    
    if keyPressed == True:
        myCar1.event()


            
