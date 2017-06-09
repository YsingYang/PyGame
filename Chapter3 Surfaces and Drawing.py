
import pygame
import math
'''
# Simple Programming
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
'''

#OO Style Programming
class PyView(object):
    def __init__(self, width = 640, height = 400, fps = 30):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #初始化screen与background
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255)) #fill with white color
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playTime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold = True, )#设置字体

    def paint(self):
        pygame.draw.line(self.background, (0, 255, 0), (10, 10), (50, 100))
        pygame.draw.rect(self.background, (0, 255, 0), (50, 50, 100, 25))
        pygame.draw.circle(self.background, (0, 200, 0), (200, 50), 35)
        pygame.draw.polygon(self.background, (0, 180, 0), ((250,100),(300,0),(350,50)))
        pygame.draw.arc(self.background, (0, 150, 0), (400, 10, 150, 100), 0, 3.14)
        # draw a pentagram
        pygame.draw.line(self.background, (255, 0, 0), (320, 200), (260, 330))
        pygame.draw.line(self.background, (255, 0, 0), (260, 330), (410, 245))
        pygame.draw.line(self.background, (255, 0, 0), (410, 245), (230, 245))
        pygame.draw.line(self.background, (255, 0, 0), (230, 245), (380, 330))
        pygame.draw.line(self.background, (255, 0, 0), (380, 330), (320 ,200))

        myball = Ball()
        myball.blit(self.background)

    def run(self):
        self.paint()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            milliseconds = self.clock.tick(self.fps)
            self.playTime += milliseconds / 1000.0
            self.drawText("FPS: {:6.3f}{}PLAYTIME: {:3.1f} SECONDS".format(
                           self.clock.get_fps(), " "*5, self.playTime))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def drawText(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (50, 150))

class Ball(object):
    def __init__(self, radius = 50, color = (0, 0, 255), x = 320, y = 240):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        #Surface((width, height), flags=0, depth=0, masks=None) -> Surface
        self.surface = pygame.Surface((2 * self.radius, 2 * self.radius))
        #Ball 这里单独又建了一个suface, 且底为黑色的,
        pygame.draw.circle(self.surface, (0, 0, 255), (25, 25), 25)
        # pygame.draw.circle(Surface, color, pos, radius, width=0)
        self.surface = self.surface.convert()

    def blit(self, background):
        #background.blit(self.surface, (self.x, self.y))
        #pygame.draw.circle(background, (0, 0, 255), (self.x, self.y), 25)
        #blit the ball in the background
        pass


if __name__ == '__main__':
    PyView().run()