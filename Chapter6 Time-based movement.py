
import pygame
import random

def wildPainting():
    pygame.draw.circle(background, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                       (random.randint(0, screenrect.width), random.randint(0, screenrect.height)), random.randint(50, 500))

pygame.init()
screen = pygame.display.set_mode((640, 480))
screenrect = screen.get_rect()
background = pygame.Surface((screen.get_size()))
background.fill((255, 255, 255))
background = background.convert()

background2 = background.copy()
ballsurface = pygame.Surface((50, 50))
ballsurface.set_colorkey((0, 0, 0))#make black the transparent color (red,green,blue)
pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)
ballsurface = ballsurface.convert_alpha()
ballrect = ballsurface.get_rect()

ballx, bally = 550, 240#start position
dx, dy = 60, 50

screen.blit(background, (0, 0))
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
mainloop = True
FPS = 60
playtime = 0
paintBigCircle = False# 是否调用wildPainting()
cleanup = True #是否每次循环都调用blit(background)

while mainloop:
    milliseoncds = clock.tick(FPS)
    seconds = milliseoncds / 1000.0
    playtime += seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False

            elif event.key == pygame.K_1:
                FPS = 10
            elif event.key == pygame.K_2:
                FPS = 20
            elif event.key == pygame.K_3:
                FPS = 30
            elif event.key == pygame.K_4:
                FPS = 40
            elif event.key == pygame.K_5:
                FPS = 50
            elif event.key == pygame.K_6:
                FPS = 60
            elif event.key == pygame.K_7:
                FPS = 70
            elif event.key == pygame.K_8:
                FPS = 80
            elif event.key == pygame.K_9:
                FPS = 90
            elif event.key == pygame.K_0:
                FPS = 1000  # absurd high value

            elif event.key == pygame.K_x:
                paintBigCircle = not paintBigCircle
            elif event.key == pygame.K_y:
                cleanup = not cleanup
            elif event.key == pygame.K_w:# restore old background
                background.blit(background2, (0, 0))# clean the screen

    pygame.display.set_caption("x: paint ({}) y: cleanup ({}) ,"
                               " w: white, 0-9: limit FPS to {}"
                               " (now: {:.2f})".format(
        paintBigCircle, cleanup, FPS, clock.get_fps()))

    if cleanup:
        screen.blit(background, (0, 0))
    if paintBigCircle:
        wildPainting()

    ballx += dx * seconds #以时间为单位移动
    bally += dy * seconds

    if ballx < 0:
        ballx = 0
        dx *= -1

    elif ballx + ballrect.width > screenrect.width:
        ballx = screenrect.width - ballrect.width #若超出范围, 将球移动回至范围内
        dx *= -1

    if bally < 0:
        bally = 0
        dy *= -1

    elif bally + ballrect.height > screenrect.height:
        bally = screenrect.height - ballrect.height
        dy *= -1

    screen.blit(ballsurface, (round(ballx, 0), round(bally, 0)))
    pygame.display.flip()




