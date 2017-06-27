import pygame
import random

def Text(msg = 'hello world', duration = 5):

    def newColor():
        return (random.randint(10, 250), random.randint(10, 250), random.randint(0, 250))

    def write(msg = 'pygame is cool'):
        myFont = pygame.font.SysFont('None', random.randint(34, 128))#第二个参数为选取字体大小
        myText = myFont.render(msg, True, newColor()) #用定义好的字体渲染文本 , 返回的其实就是一个surface
        myText = myText.convert_alpha()
        return myText

    pygame.init()
    x, y = 60, 60
    dx, dy = 5, 5

    screen = pygame.display.set_mode((640, 480))
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background = background.convert()
    screen.blit(background, (0, 0))
    mainLoop = True
    clock = pygame.time.Clock()
    FPS = 60
    while mainLoop:
        milliseconds = clock.tick(FPS)
        seconds = milliseconds / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainLoop == False
        textSurface = write('hello world')
        x += dx
        y += dy
        if x < 0:
            x = 0
            dx *= -1
        elif x + textSurface.get_width() > screen.get_width():
            x = screen.get_width() - textSurface.get_width()
            dx *= -1
        if y < 0:
            y = 0
            dy *= -1
        elif y + textSurface.get_height() > screen.get_height():
            y = screen.get_height() - textSurface.get_height()
            dy *= -1

        screen.blit(textSurface, (x, y))
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    Text()

