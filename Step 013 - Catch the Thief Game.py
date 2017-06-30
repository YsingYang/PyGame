import pygame
import os
import random

class Config(object):
    screenWidth = 1024
    screenHeight = 600
    thiefx, thiefy = 50, 50 #thief 起始位置

    thiefDx = random.randint(-150, 150)
    thiefDy = random.randint(-150, 150) #x, y的变化情况
    thiefMaxSpeed = 200 #max speed of thief
    erratic = 1 #？？？？？？？？

    policex, policey = 250, 250 #police起始位置
    policedx, policedy = 0, 0 #police speed in pixel per second !

    birdx, birdy = 100, 100 #bird起始位置
    birdDx, birdDy = 0, 0

    snakex, snakey = 200, 200 #snake起始位置
    snakeDx, snakeDy = 0, 0
    crossX, crossY = 150, 150

def write(msg = 'Pygame msg', color = (0, 0, 0), fontSize = 24):
    myFont = pygame.font.SysFont('None', fontSize)
    myText = myFont.render(msg, True, color)
    return myText

def intro(screen):
    '''draw game instructions'''
    screen.fill((255, 255, 255))

    screen.blit(write("Catch the chief - INSTRUCTIONS", (0, 0, 255), 64), (80, 15))#最后一个参数是startpos
    screen.blit(write("control the snake with the cursor keys or WASD (Enter or LCTRLto stop)"), (10, 70))
    screen.blit(write("control the bird with the mouse (left button to stop)"), (10, 100))
    screen.blit(write("the cross is always in the middle between snake and bird"), (10, 130))
    screen.blit(write("the blue circle (police) moves toward the cross"), (10, 160))
    screen.blit(write("catch the red triangle (the thief) with the blue circle to win points"), (10, 190))
    screen.blit(write("click the left mouse button to start"), (50, 290))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            pass
        if pygame.mouse.get_pressed()[0]:
            return #当左键被点击时, 返回（相当于跳出循环）


def draw(sprite, x, y):
    Config.screen.blit(sprite, (round(x, 0)- sprite.get_width() / 2, round(y, 0) - sprite.get_height() / 2))

def bounce(sprite, x, y, dx, dy): #sprite是已中线的x, y为基准？
    if x - sprite.get_width() / 2 < 0:
        x = sprite.get_width() / 2
        dx *= -1

    elif x + sprite.get_width() / 2 > Config.screenWidth:
        x = Config.screenWidth - sprite.get_width() / 2
        dx *= -1

    if y - sprite.get_height() / 2 < 0
        y = sprite.get_height() / 2
        dy *= -1
    elif y + sprite.get_height() / 2 > Config.screenHeight:
        y = Config.screenHeight - sprite.get_height() / 2
        dy *= -1
    return x, y, dx, dy

def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def arrow(sprite, dx, dy):
    midx = sprite.get_width() / 2
    midy = sprite.get_height() / 2

    return sprite #????????????这个函数有个p用？？？？？计算了midx, midy就放在那里？

def playGame():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    try:
        background = pygame.image.load(os.path.join('resource', 'wien.jpg'))
        snake = pygame.image.load(os.path.join('resource', 'snake.gif'))
        bird = pygame.image.load(os.path.join('resource', 'babytux.png'))
        over = pygame.mixer.Sound(os.path.join('resource', 'time_is_up_game_over.ogg'))
        spring = pygame.mixer.Sound(os.path.join('resource', 'spring.wav'))

    except:
        raise (UserWarning, 'Unable to find files')

    screen = pygame.display.set_mode((1024, 600))
    Config.screen = screen
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    background = background.convert()
    Config.background = background
    snake = snake.conver_alpha()
    bird = bird.conver_alpha()

    police = pygame.Surface((50, 50))
    pygame.draw.circle(police, (0, 0, 255), (25, 25), 25)# blue police
    police.set_colorkey((0, 0, 0)) #black transparent
    police.blit(write('P', (255, 255, 255), 48), (12, 10))
    police = police.convert_alpha()

    cross = pygame.Surface((10, 10))
    cross.fill((255, 255, 255))

    pygame.draw.line(cross, (0, 0, 0), (0, 0), (10, 10)) # black lines
    pygame.draw.line(cross, (0, 0, 0), (0, 10), (10, 0))
    #在Surface中连了两条对角线
    cross.set_colorkey((255, 255, 255)) #white transParent
    cross = cross.convert_alpha()

    thief = pygame.Surface((26, 26))
    thief.set_colorkey((0, 0, 0))
    pygame.draw.polygon(thief, (255, 0, 0), [(0, 0), (25, 0), (12, 25)])
    thief.blit(write('T', (0, 0, 0), 32), (6, 3))
    thief = thief.convert_alpha()

    catchInLastFrame = False
    catchInCurrentFrame = False

    pygame.draw.rect(background, (200, 200, 200), ((screen.get_width()-360,
                     screen.get_height()-25), (360,25))) #?????????

    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    mainLoop = True
    FPS = 60
    playTime = 0.0
    gameOver = False
    gameOverSound = True
