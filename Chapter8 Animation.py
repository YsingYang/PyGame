import pygame
import random
import os

pygame.init()
folder = 'resource'
try:
    spriteSheet = pygame.image.load(os.path.join(folder, 'char9.bmp'))
    #这是一张包括Animation所有动画的图片
except:
    raise Exception('unable to load image')

screen = pygame.display.set_mode((800, 480))
spriteSheet.convert()
screenRect = screen.get_rect()
background = pygame.Surface((screen.get_size())).convert()#为什么教程中是先get_rect再 convert()的? 这两者有什么区别吗
backgroundRect = background.get_rect()
background.fill((255, 255, 255))
screen.blit(background, (0, 0))

lions = [] # a list for the lion images

for nbr in range(1, 5):
    lions.append(spriteSheet.subsurface((127 * (nbr -1), 64, 127, 127)))

#第二行
for nbr in range(1, 3):
    lions.append(spriteSheet.subsurface((127*(nbr-1), 262-64, 127, 127)))
print('len :', len(lions))

for nbr in range(len(lions)):
    lions[nbr].set_colorkey((0, 0, 0))#black transparent
    lions[nbr] = lions[nbr].convert_alpha()
    print('converted nbr', nbr)

for nbr in range(len(lions)):
    screen.blit(lions[nbr], (nbr*127, 0))
    print('Blitted nbr', nbr)

#这个nbr是什么??????????????????
print('This nbr val = ', nbr) #好像python循环的变量可以是个全局变量
screen.blit(lions[nbr], (nbr*127, 0))

clock = pygame.time.Clock()
mainLoop = True
FPS = 60
playTime = 0
cycleTime = 0
interval = .15 # how long one single images should be displayed in seconds
pictureIndex = 0

while mainLoop:
    milliseconds = clock.tick(FPS)
    second = milliseconds / 1000.0
    playTime += second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
            elif event.key == pygame.K_PLUS:
                if FPS < 200:
                    FPS += 10
            elif event.key == pygame.K_MINUS:
                if FPS > 0:
                    FPS -= 10
    '''
    TimeBase Animation
    cycleTime += second #基于时间base切换
    if cycleTime > interval:
        myPicture = lions[pictureIndex]
        screen.blit(background.subsurface((300, 300, 128, 66)), (300, 300))#重新填充ackground的subsurface部分
        #取(300, 300的subface width = 128, height = 66
        screen.blit(myPicture, (300, 300))
        pictureIndex  += 1
        if pictureIndex > 5:
            pictureIndex = 0
        cycleTime = 0
    '''
    #FrameBase Animation
    myPicture = lions[pictureIndex]
    screen.blit(background.subsurface((300, 300, 128, 66)), (300, 300))
    screen.blit(myPicture, (300, 300))
    pictureIndex += 1
    if pictureIndex > 5:
        pictureIndex = 0


    pygame.display.set_caption("[FPS]: %.2f picture: %i" % (clock.get_fps(), pictureIndex))
    pygame.display.flip()

print("This 'game' was played for {:.2f} seconds".format(playTime))











