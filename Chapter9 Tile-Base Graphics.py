def mazegame():
    import pygame
    import random

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screenRect = screen.get_rect()
    background = pygame.Surface((screen.get_size()))
    #为什么这里不直接用screen.get_rect()
    backgroundRect = background.get_rect()
    background.fill((255, 255, 255))
    background = background.convert()
    backgroundBackup = background.copy()
    #background的副本

    screen.blit(background, (0, 0))
    ballSurface = pygame.Surface((10, 10))
    #player (ball)
    ballSurface.set_colorkey((0, 0, 0))#black transparent
    pygame.draw.circle(ballSurface, (255, 0, 0 ), (5, 5), 5)#在ballSurface中画一个半径为5的球
    ballSurface = ballSurface.convert_alpha()
    ballRect = ballSurface.get_rect()

    dx = 0
    dy = 0 # delta x ... x moving vector of ball surface  # delta y ... y moving vector of ball surface

    # startlevel: 24 x 15
    startlevel = ["xxx.xxxxxxxxxxxxxxxxxx",
                  ".s.....x..............",
                  "xxxx.........xx......x",
                  "x......x....x.x......x",
                  "x......x......x......x",
                  "x......x......x......x",
                  "x...xxxxxx....x......x",
                  "x......x.............x",
                  "x......x......xxxxxxxx",
                  "xxxxxx.x.............x",
                  "x......x.............x",
                  "x......x.............x",
                  "x..........xxxx...xxxx",
                  "x..........x.........x",
                  "xxxxxxxxxxxxxxxxx.xxnx"]

    # middlelevel = 15 x 16
    middlelevel = ["xxxxxxxxxxxxxxx",
                   "xs............x",
                   "x.........x...x",
                   "x.........x...x",
                   "x......x..x...x",
                   "x.....x...x...x",
                   "x..p.xxxxxx...x",
                   "x.....x.......x",
                   "x.x....x......x",
                   "x.x...........x",
                   "x.x...x.......x",
                   "x.x....x......x",
                   "x.xxxxxxx..n..x",
                   "x......x......x",
                   "x.....x.......x",
                   "xxxxxxxxxxxxxxx"]

    # smilelevel: 32 x 18
    winlevel = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "xs.............................x",
                "x..............................x",
                "x..............................x",
                "x............xxx....xxx........x",
                "x...........xx.xx..xx.xx.......x",
                "x............xxx....xxx........x",
                "x..............................x",
                "x................x.............x",
                "x................x.............x",
                "x................x.............x",
                "x..............................x",
                "x................r.............x",
                "x............xx....xxx.........x",
                "x.............xxxxxxx..........x",
                "x..............................x",
                "x..............................x",
                "xxxxxxpxxxxxxxxxxxnxxxxxxxxxxxex"]


    def createBlock(width, height, color):
        tmpBlock = pygame.Surface((width, height))
        tmpBlock.fill(color)
        tmpBlock.convert()
        return tmpBlock

    def addLevel(level):
        lines = len(level)
        columns = len(level[0])

        width = screenRect.width // columns
        height  = screenRect.height // lines

        wallBlock = createBlock(width, height, (20, 0, 50))
        nextBlock = createBlock(width, height, (255, 50 ,50))
        preBlock = createBlock(width, height, (255, 50, 255))
        endBlock = createBlock(width, height, (100, 100, 100))
        randomBlock = createBlock(width, height, (0, 0, 200))

        background = backgroundBackup.copy()

        #将相应的surface添入到background中
        for y in range(lines):
            for x in range(columns):
                if level[y][x] == 'x':
                    background.blit(wallBlock, (width * x, height * y))

                elif level[y][x] == 'n':#next level
                    background.blit(nextBlock, (width * x, height * y))

                elif level[y][x] == 'p':
                    background.blit(preBlock, (width * x, height * y))

                elif level[y][x] == 'r':
                    background.blit(randomBlock, (width * x, height * y))

                elif level[y][x] == 'e':
                    background.blit(endBlock, (width * x, height * y))

                elif level[y][x] == 's':#起始点
                    ballx = width * x
                    bally = height * y

        screen.blit(backgroundBackup, (0, 0))
        return width, height, ballx, bally, lines, columns, background

    allLevels = [startlevel, middlelevel, winlevel] #相应level的模型
    maxLevels = len(allLevels) #level数量
    maze = allLevels[0]
    width, height, ballx, bally, lines, columns, background = addLevel(maze)

    clock = pygame.time.Clock()
    mainLoop = True
    FPS = 60
    playTime = 0

    while mainLoop:
        milliSeconds = clock.tick(FPS)
        seconds = milliSeconds / 1000.0
        playTime +=  seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainLoop = False
                elif event.key == pygame.K_UP:
                    dy -= 1
                elif event.key == pygame.K_DOWN:
                    dy += 1
                elif event.key == pygame.K_LEFT:
                    dx -= 1
                elif event.key == pygame.K_RIGHT:
                    dx += 1
        pygame.display.set_caption("[FPS]: %.2f dx: %i dy %i press cursor keys to move ball" % (clock.get_fps(), dx, dy))
        screen.blit(background, (0, 0))
        if dx > 0:
            pointx = ballx + ballRect.width
        else:
            pointx = ballx

        if dy > 0:
            pointy = bally + ballRect.height
        else:
            pointy = bally

        # ------- find out if ball want to leave screen
        if pointx + dx < 0:
            ballx = 0
            pointx = 0
            dx = 0
        elif pointx + dx > screenRect.width:
            ballx = screenRect.width - ballRect.width
            pointx = screenRect.width - ballRect.width
            dx = 0

        if pointy + dy > screenRect.height:
            bally = screenRect.height - ballRect.height
            pointy = screenRect.height - ballRect.height
            dy = 0
        elif pointy + dy < 0:
            bally = 0
            pointy = 0
            dy = 0

        y1 = int(pointy // height)
        y1 = max(0, y1)
        y1 = min(y1, lines - 1)

        x1 = int((pointx + dx)/ width)
        x1 = max(0, x1)
        x1 = min(x1, columns - 1)

        y2 = int((pointy + dy) / height)
        y2 = max(0, y2)
        y2 = min(y2, lines - 1)

        if maze[y1][x1] == 'x':
            dx = 0
        else:
            ballx += dx
        if maze[y2][x1] == 'x':
            dy = 0
        else:
            bally += dy

        screen.blit(ballSurface, (ballx, bally))
        bline = int(bally // height) # a line where ball is currently
        bcolumn = int(ballx // width)  # column where ball is currently

        if maze[bline][bcolumn] == 'n':
            actual = allLevels.index(maze) #获取当前元素最早出现的index
            maze = allLevels[(actual + 1) % maxLevels]
            width, height, ballx, bally, lines, columns, background = addLevel(maze)
        elif maze[bline][bcolumn] == 'p':
            actual = allLevels.index(maze)
            maze = allLevels[(maxLevels + actual - 1) % maxLevels]
            width, height, ballx, bally, lines, columns, background = addLevel(maze)

        elif maze[bline][bcolumn] == 'r':
            maze = random.choice(allLevels)#随机选取level中的任意一个元素
            width, height, ballx, bally, lines, columns, background = addLevel(maze)

        elif maze[bline][bcolumn] == 'e':
            print("---*** congratulation, you escaped the maze ! ***-------")
            mainLoop = False

        pygame.display.flip()
    print("This maze game was played for {:.2f} seconds".format(playTime))

if __name__ == '__main__':
    mazegame()












