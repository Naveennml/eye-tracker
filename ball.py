import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

cross = pygame.image.load("crosshairs-200-px-copy.png")
crossrect = cross.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    crossrect = crossrect.move(speed)
    if crossrect.left < 0 or crossrect.right > width:
        speed[0] = -speed[0]
    if crossrect.top < 0 or crossrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(cross, crossrect)
    pygame.display.flip()
