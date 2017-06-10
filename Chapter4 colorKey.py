import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()

ballSurface = pygame.Surface((50, 50)) #create a new surface
ballSurface.set_colorkey((0, 0, 0)) #make black the transparent color (red,green,blue)

pygame.draw.circle(ballSurface, (0, 0, 255), (25, 25), 25)
ballSurface = ballSurface.convert_alpha()

screen.blit(background, (0, 0))

ballx = 20 #left ball position
bally = 240
screen.blit(ballSurface, (ballx, bally)) #将ballSurface 画到screen相应位置

ballx2 = 400
bally2 = 380
screen.blit(ballSurface, (ballx2, bally2))

clock = pygame.time.Clock()
mainLoop = True
FPS = 30
playTime = 0.0

t = 0
color1 = 0
color2 = 0

while mainLoop:
    milliseconds = clock.tick(FPS)
    playTime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    pygame.draw.line(screen, (color1, 255 - color1, color2), (32*t, 0), (0, 480 - 24 * t))
    pygame.draw.line(screen, (255 - color2, color2, color1), (32*t, 480), (640, 480 - 24 * t))
    #screen.blit(ballSurface, (ballx2, bally2))

    t += 1
    if t > 20:
        t = 0
        color1 = random.randint(0, 255) #new color
        color2 = random.randint(0, 255)

    pygame.display.set_caption('Test')
    pygame.display.flip()




