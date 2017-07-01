import pygame
import os
import random

class Config(object):
    screenWidth = 1024
    screenHeight = 600
    thiefx, thiefy = 50, 50 #thief 起始位置
    screen = pygame.Surface((0, 0))

    thiefDx = random.randint(-150, 150)
    thiefDy = random.randint(-150, 150) #x, y的变化情况
    thiefMaxSpeed = 200 #max speed of thief
    erratic = 1 #弹性范围， 用于控制thief的移动

    policex, policey = 250, 250 #police起始位置
    policedx, policedy = 0, 0 #police speed in pixel per second !

    birdx, birdy = 100, 100 #bird起始位置
    birdDx, birdDy = 0, 0

    snakex, snakey = 200, 200 #snake起始位置
    snakeDx, snakeDy = 0, 0
    crossX, crossY = 150, 150


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

def write(msg = 'Pygame msg', color = (0, 0, 0), fontSize = 24):
    myFont = pygame.font.SysFont('None', fontSize)
    myText = myFont.render(msg, True, color)
    return myText


def draw(sprite, x, y):
    Config.screen.blit(sprite, (round(x, 0)- sprite.get_width() / 2, round(y, 0) - sprite.get_height() / 2))

def bounce(sprite, x, y, dx, dy): #sprite是已中线的x, y为基准？
    if x - sprite.get_width() / 2 < 0:
        x = sprite.get_width() / 2
        dx *= -1

    elif x + sprite.get_width() / 2 > Config.screenWidth:
        x = Config.screenWidth - sprite.get_width() / 2
        dx *= -1

    if y - sprite.get_height() / 2 < 0:
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

    # ------------start--------------#
    screen = pygame.display.set_mode((1024, 600))
    Config.screen = screen
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    background = background.convert()
    Config.background = background
    snake = snake.convert_alpha()
    bird = bird.convert_alpha()

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
    playTime = 60.0
    points = 0.0
    gameOver = False
    gameOverSound = True
    while mainLoop:
        millisecond = clock.tick(FPS)
        second = millisecond / 1000.0
        playTime -= second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.K_DOWN:
                if event.key == pygame.K_ESCAPE:
                    mainLoop = False
            pygame.display.set_caption("[FPS]: %.2f Snake: dx %i dy %i Bird:"
                                       " dx %i dy %i police: dx %.2f dy %.2f " %
                                       (clock.get_fps(), Config.snakeDx, Config.snakeDy,
                                        Config.birdDx, Config.birdDy, Config.policedx, Config.policedy))
        if playTime < 0:
            gameOver = True
        screen.blit(background, (0, 0 ))
        if gameOver:
            if gameOverSound:
                over.play()
                gameOverSound = False
            screen.blit(write("Game Over. %.2f points. Press ESCAPE" % points, (128, 0, 128), 64), (20, 250))

        else:
            screen.blit(write("points: %.2f time left: %.2f seconds" % (points, playTime)), (screen.get_width()-350,screen.get_height()-20))

            ''' 计算bird移动路径 '''
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX < Config.birdx:
                Config.birdx -= 1

            elif mouseX > Config.birdx:
                Config.birdx += 1

            if mouseY > Config.birdy:
                Config.birdy += 1

            elif mouseY < Config.birdy:
                Config.birdy -= 1


            if pygame.mouse.get_pressed()[0] == True:# stop movement by mouseclick (left button)
                Config.birdx = 0
                Config.birdy = 0


            '''计算snake的移动'''
            pressedKeys = pygame.key.get_pressed() # all keys that are pressed now
            if pressedKeys[pygame.K_LEFT] or pressedKeys[pygame.K_a]:
                Config.snakeDx -= 1
            if pressedKeys[pygame.K_RIGHT] or pressedKeys[pygame.K_d]:
                Config.snakeDx += 1

            if pressedKeys[pygame.K_UP] or pressedKeys[pygame.K_w]:
                Config.snakeDy -= 1
            if pressedKeys[pygame.K_DOWN] or pressedKeys[pygame.K_s]:
                Config.snakeDy += 1
            if pressedKeys[pygame.K_RETURN] or pressedKeys[pygame.K_LCTRL]: #???这是什么键
                Config.snakeDy = 0
                Config.snakeDx = 0

            #取snake bird的中间点, 二分计算mid的公式
            Config.crossX = min(Config.birdx, Config.snakex) + (max(Config.birdx, Config.snakex) - min(Config.birdx, Config.snakex)) / 2 - cross.get_width() / 2
            Config.crossY = min(Config.birdy, Config.snakey) + (max(Config.birdy, Config.snakey) - min(Config.birdy, Config.snakey)) / 2 - cross.get_height() / 2

            if Config.crossX < Config.policex:
                Config.policedx -= 1 #police移动的方向总是往中线靠拢
            elif Config.crossX > Config.policex:
                Config.policedx += 1

            if Config.crossY < Config.policey:
                Config.policedy -= 1
            elif Config.crossY > Config.policey:
                Config.policedy += 1

            Config.thiefDx += random.randint(-Config.erratic, Config.erratic)
            Config.thiefDy += random.randint(-Config.erratic, Config.erratic)

            Config.thiefDx = max(Config.thiefDx, -Config.thiefMaxSpeed) #控制最大速度， 注意符号
            Config.thiefDx = min(Config.thiefDx, Config.thiefMaxSpeed)

            Config.thiefDy = max(Config.thiefDy, -Config.thiefMaxSpeed)
            Config.thiefDy = min(Config.thiefDy, Config.thiefMaxSpeed)

            Config.policedx *= 0.995
            Config.policedy *= 0.995
            Config.snakeDx *= 0.995
            Config.snakeDy *= 0.995
            Config.birdDx *= 0.995
            Config.birdDy *= 0.995

            ''' New Position '''
            Config.policex += Config.policedx * second
            Config.policey += Config.policedy * second

            Config.birdx += Config.birdDx * second
            Config.birdy += Config.birdDy * second

            Config.snakex += Config.snakeDx * second
            Config.snakey += Config.snakeDy * second
            Config.thiefx += Config.thiefDx * second
            Config.thiefy += Config.thiefDy * second

            Config.policex, Config.policey, Config.policedx, Config.policedy = bounce(police, Config.policex, Config.policey, Config.policedx, Config.policedy)
            Config.birdx, Config.birdy, Config.birdDx, Config.birdDy = bounce(bird, Config.birdx, Config.birdy, Config.birdDx, Config.birdDy)
            Config.snakex, Config.snakey, Config.snakedx, Config.snakedy = bounce(snake, Config.snakex, Config.snakey, Config.snakeDx, Config.snakeDy)
            Config.thiefx, Config.thiefy, Config.thiefDx, Config.thiefDy = bounce(thief, Config.thiefx, Config.thiefy, Config.thiefDx, Config.thiefDy)

            distx = max(Config.policex + police.get_width() / 2, Config.thiefx +
                        thief.get_width() / 2) - min(Config.policex +
                                                     police.get_width() / 2, Config.thiefx + thief.get_width() / 2)
            disty = max(Config.policey + police.get_height() / 2, Config.thiefy +
                        thief.get_height() / 2) - min(Config.policey + police.get_width() / 2,
                                                      Config.thiefy + thief.get_width() / 2)

            catchInLastFrame = catchInCurrentFrame
            catchInCurrentFrame = False
            if (distx < police.get_width() / 2) and (disty < police.get_height() / 2):
                catchInCurrentFrame = True #如果在police的Surface中
                points +=  second
                screen.fill(randomColor())
                if not pygame.mixer.get_busy():
                    spring.play()
            else:
                if catchInLastFrame:
                    screen.blit(background, (0, 0)) #将原图绘制
            draw(bird, Config.birdx, Config.birdy)
            draw(snake, Config.snakex, Config.snakey)
            pygame.draw.line(screen, randomColor(), (Config.snakex, Config.snakey), (Config.birdx, Config.birdy), 1)
            pygame.draw.line(screen, randomColor(), (Config.crossX, Config.crossY), (Config.policex, Config.policey),1)
            draw(police, Config.policex, Config.policey)
            draw(cross, Config.crossX, Config.crossY)
            draw(thief, Config.thiefx, Config.thiefy)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    playGame()






