import  pygame
import  os

try:
    background = pygame.image.load(os.path.join('resource', "background640x480_a.jpg"))
    snake = pygame.image.load(os.path.join('resource', "snake.gif"))
except:
    raise (UserWarning, '无法打开图片')

pygame.init()
screen = pygame.display.set_mode((640, 480))
background = background.convert()
snake = snake.convert_alpha()
snakeDuplicate = snake.copy()
startX, startY = 250, 240
dx, dy = 0, 0
speed = 60

angle = 0 #旋转角度
zoom = 1.0 #放大比例
zoomSpeed = 0.01
turnSpeed = 180

screen.blit(background, (0, 0))
screen.blit(snake, (startX, startY))
clock = pygame.time.Clock()
mainLoop = True
FPS = 60

while mainLoop:
    milliseconds = clock.tick(FPS)
    second = milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
    pygame.display.set_caption("press cursor keys and w a s d - fps:"
                               "%.2f zoom: %.2f angle %.2f" % (clock.get_fps(), zoom, angle))
    try:

        snakeRect = pygame.Rect(round(startX, 0), round(startY, 0), snake.get_width(), snake.get_height())
    #round第二个参数表示精确到小数多少位
        dirty = background.subsurface(snakeRect.clip(screen.get_rect()))
    #Returns a new rectangle that is cropped to be completely inside the argument Rect.
    # If the two rectangles do not overlap to begin with, a Rect with 0 size is returned.
    #当snake图片越界后 background糊了可能就是因为这个函数原因
        dirtyRect = dirty.get_rect()
        if dirtyRect != snakeRect :
            screen.blit(background, (0, 0))
        else:
            screen.blit(dirty, (round(startX, 0), round(startY, 0)))
    except:
        startX = 0
        startY = 0

    pressedKeys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if pressedKeys[pygame.K_LEFT]:
        dx -= speed
    if pressedKeys[pygame.K_RIGHT]:
        dx += speed
    if pressedKeys[pygame.K_UP]:
        dy -= speed
    if pressedKeys[pygame.K_DOWN]:
        dy += speed

    #重新计算snake的位置
    startX += dx * second
    startY += dy * second

    #计算snake旋转
    turnFactor = 0 # neither a nor d, no turning
    if pressedKeys[pygame.K_a]:
        turnFactor += 1
    if pressedKeys[pygame.K_d]:
        turnFactor -= 1

    #计算放大比例
    zoomFactor = 1.0
    if pressedKeys[pygame.K_w]:
        zoomFactor += zoomSpeed
    if pressedKeys[pygame.K_s]:
        zoomFactor -= zoomSpeed

    if turnFactor != 0 or zoomFactor != 1.0:
        angle += turnFactor * turnSpeed * second #Time-based
        zoom *= zoomFactor

        oldRect = snake.get_rect()

        #重新计算snake 变换后的形状, pygame提供了一个 transform.rotozoom的方法
        snake = pygame.transform.rotozoom(snakeDuplicate, angle, zoom)#传入角度与放大倍数
        newRect = snake.get_rect()

        startX += oldRect.centerx - newRect.centerx #计算变化后的起始x
        startY += oldRect.centery - newRect.centery

    screen.blit(snake, (round(startX, 0), round(startY, 0)))
    pygame.display.flip()




