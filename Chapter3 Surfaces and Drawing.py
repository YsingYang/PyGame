
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))

# create a rectangular surface for the ball
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
# draw blue filled circle on ball surface
pygame.draw.circle(background, (0, 0, 255), (25, 25), 25)
pygame.draw.rect(background, (0, 255, 0), (50, 50, 100, 25)) #RGB, topleft, width, height
pygame.draw.circle(background, (0, 200, 0), (200, 50), 35) #RGB, 圆心, 半径
pygame.draw.polygon(background, (0, 180, 0), ((250, 100), (300, 0), (350, 50))) #RGB + 3个顶点坐标
pygame.draw.arc(background, (0, 150, 0), (400, 10, 150, 100), 0, 2 * math.pi, 3)
 #RGB, RECT, startAngle, stopAngle, width

#ideas Question
#1. Paint a giant pink circle on the middle of the screen
pygame.draw.circle(background, (255, 128, 255), (screen.get_rect().centerx, screen.get_rect().centery), 100)

#2. Find out wich line you must out-comment (using #) to remove the blue ball and the black square
#....这是啥子问题
#3. Can you use the pygame.draw.polygon function to draw a pentagram: (五角星)
#思路, 画三个三角形
#连续画5个三角形, 和一个5边形

screen.blit(background, (0, 0))
clock = pygame.time.Clock()
mainLoop = True
FPS = 30
playTime = 0.0
while mainLoop:
    milliseconds = clock.tick(FPS)
    playTime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:0.2} seconds".format(
                               clock.get_fps(),playTime))
    screen.blit(background, (0, 0))
    pygame.display.flip()


