import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 255, 255, 255
screen = pygame.display.set_mode(size)

class Crosshair(object):
    def __init__(speed = [1, 1]):
        self.speed = speed
        self.cross = pygame.image.load("crosshairs-200-px-copy.png")
        self.crossrect = cross.get_rect()
        self.result = []
        
    def draw():
        screen.fill(white)
        #could maybe edit the crossrect directly for smoother motions
        #The Rect object has several virtual attributes which can be used to move and align the Rect:
        #top, left, bottom, right
        #topleft, bottomleft, topright, bottomright
        #midtop, midleft, midbottom, midright
        #center, centerx, centery
        #size, width, height
        #w,h
        screen.blit(self.cross, self.crossrect)
        pygame.display.flip()
        
    def move():
        self.crossrect = self.crossrect.move(speed)
        if self.crossrect.left < 0 or self.crossrect.right > width:
            speed[0] = -speed[0]
        if crossrect.top < 0 or crossrect.bottom > height:
            speed[1] = -speed[1]
        
    def record(x, y):
        self.result.append([x, y, self.crossrect.centerx, self.crossrect.centery])
        
    def write():
        fo = open("xoffsetyoffsetxy.csv", "w")
        for line in self.result:
            string = ", ".join(line)
            fo.write(string + "\n")
        fo.close()

crosshair = Crosshair([1, 2])
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    crosshair.draw()
    pygame.time.delay(10)#miliseconds
    crosshair.record(xoffset, yoffset)
    crosshair.move()
    
crosshair.write()

    
