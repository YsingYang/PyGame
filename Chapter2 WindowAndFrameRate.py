import pygame


pygame.init()

screen = pygame.display.set_mode((640, 480))#Set size of windows

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()#Convert Surface to make blitting faster
#来自另一篇教程的介绍, 这个convert理解起来有点模糊
#convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（
#事实上因为 它太常用了，如果你不写pygame也会帮你做）；
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。

#screen.blit(background, (0, 0))  # 后面那个参数是top, left
## Copy background to screen (position (0, 0) is upper left corner).
clock = pygame.time.Clock()
mainLoop = True
FPS = 30
playtime = 0.0
while mainLoop:
    screen.blit(background, (0, 0))  # 后面那个参数是top, left
    #放在这里的原因是, 每一帧都重新刷新屏幕, 不然后面填充的字体会不断覆盖之前的的

    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN:#加这句干嘛?
            if event.key == pygame.K_ESCAPE:#ESC
                mainLoop = False

    #想写个字体
    font = pygame.font.Font(None, 48)
    text = font.render('Score : {0:.2f}'.format(clock.get_fps()), True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery - 24

    text2 = font.render('Playtime : {0:.2f}'.format(playtime), True, (255, 0, 0))
    text2Rect = text2.get_rect()
    text2Rect.centerx = screen.get_rect().centerx
    text2Rect.centery = screen.get_rect().centery


    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    #text = "FPS : {0:.2f} Playtime : {1:.2f}".format(clock.get_fps(), playtime)
    #pygame.display.set_caption(text)
    #pygame.display.update()
    pygame.display.flip()

pygame.quit()