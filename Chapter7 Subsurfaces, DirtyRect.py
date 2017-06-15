import pygame
import random
import os

pygame.init()

folder = 'resource'
try:
    prettyBackground = pygame.image.load(os.path.join(folder, "800px-La_naissance_de_Venus.jpg"))
    uglyBackground = pygame.image.load(os.path.join(folder, "background800x470.jpg"))
    snakeSurface = pygame.image.load(os.path.join(folder, "snake.gif"))
except:
    raise(UserWarning, 'Can not find specified file')

screen = pygame.display.set_mode((800, 470))
screenRect = screen.get_rect()

prettyBackground = prettyBackground.convert()
uglyBackground = uglyBackground.convert()
duplicate = uglyBackground.copy()
snakeSurface = snakeSurface.convert_alpha() #have alpha
snakeRect = snakeSurface.get_rect()

x = y = 1 #stat position
dx, dy = 40, 85
screen.blit(uglyBackground, (0, 0))
screen.blit(snakeSurface, (x, y))
clock = pygame.time.Clock()
mainLoop = True
FPS = 60
playTime = 0.0
painting = False
dirty = False

while mainLoop:
    milliseconds = clock.tick(FPS)
    second = milliseconds / 1000.0
    playTime += second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
            elif event.key == pygame.K_r: #恢复原图
                duplicate = uglyBackground.copy()
                screen.blit(uglyBackground, (0, 0))
                print('uglyBackground restore')
            elif event.key == pygame.K_p:
                painting = not painting
                print("painting is now set to {}".format(painting))
            elif event.key == pygame.K_d:
                dirty = not dirty
                print("dirty is now set to {}".format(dirtyRect)) #为什么程序要把初始化放在这里

    pygame.display.set_caption("FPS: {:.2f} dx:{} dy:{} [p]aint ({}) "
                               "paint, [d]irtyrect ({}), [r]estore".format(clock.get_fps(), dx,
                                                                           dy, painting, dirty))

    if not dirty: #dirty == false时, snake划过的同时, 重新绘制相应的部分, 那么在background不flip的同时, 原图也依旧保持
        dirtyRect = duplicate.subsurface((x, y, snakeRect.width, snakeRect.height))
        #在duplicate下取一个snake rect大小的 subsurface
        screen.blit(dirtyRect, (x, y))

    # 移动轨迹
    x += dx * second
    y += dy * second

    if x < 0:
        x = 0
        dx *= -1
        dx += random.randint(-15, 15)
    elif x + snakeRect.width >= screenRect.width:
        x = screenRect.width - snakeRect.width
        dx *= -1
        dx += random.randint(-15, 15)
    if y < 0:
        y = 0
        dy *= -1
        dy += random.randint(-15, 15)
    elif y + snakeRect.height >= screenRect.height:
        y = screenRect.height - snakeRect.height
        dy *= -1
        dy += random.randint(-15, 15)

    screen.blit(snakeSurface, (x, y)) #blit snake
    try:
        tvScreen = prettyBackground.subsurface((x, y, snakeRect.width, snakeRect.height))
    except:
        print('can not get subsurface')

    screen.blit(tvScreen, (0, 0))
    if painting: #如何paintting为true , 那么会将prettyBackground中的子部分画入tvScreen中
        duplicate.blit(tvScreen, (x, y))
    pygame.display.flip()









