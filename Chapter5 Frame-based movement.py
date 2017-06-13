import pygame
import random

def randomRGB():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

class PygView(object):
    def __init__(self, width=800, height=600, fps=30):
        pygame.init()
        pygame.display.set_caption('Press ESC to quit')
        self.width = width
        self.height = height
        self.fps = fps

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()

        self.background.fill((255, 255, 255))

        self.actSurface = self.screen
        self.actRGB = 255, 0, 0


    def drawStatic(self):
        self.actSurface = self.background

    def drawDynamic(self):
        self.actSurface = self.screen

    def setColor(self, rgb):
        self.actRGB = rgb

    def circle(self, x, y, radius, width):
        surfaceRadius = 2 * radius
        surface = pygame.Surface((surfaceRadius, surfaceRadius))
        pygame.draw.circle(surface, self.actRGB, (radius, radius), radius, width) #在surface中心画一个圆
        surface.set_colorkey((0, 0, 0))
        self.actSurface.blit(surface.convert_alpha(), (x, y))

    def run(self, draw):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:#有键盘按下
                    if event.type ==pygame.K_ESCAPE:
                        running = False

            self.screen.blit(self.background, (0, 0))
            draw()
            pygame.display.flip()

        pygame.quit()

class Ball(object):
    def __init__(self, x, y, radius, Xspeed=1, speedPulse = 0, color = (0, 0, 255), width = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.actRadius = radius
        self.Xspeed = Xspeed
        self.speedPulse = speedPulse
        self.color = color
        self.width = width
        self.shringking = True

    @property
    def maxX(self):#将该定义为属性getter
        return self.x + self.actRadius * 2

    def moving(self, x, y):
        self.x += x
        self.y += y

    def pulse(self):
        # Shrink or expand ball
        if not self.speedPulse:
            return

        if self.shringking: #shringking = True
            if self.actRadius > self.width:
                self.actRadius -= self.speedPulse
                self.actRadius = max(self.actRadius, self.width)#避免减少之后< width
            else:
                self.shringking = False
        else:
            if self.actRadius < self.radius:
                self.actRadius += self.speedPulse
            else:
                self.shringking = True

    def draw(self, view):
        if self.speedPulse:
            color = randomRGB()
        else:
            color = self.color

        view.setColor(color)
        view.circle(self.x, self.y, self.actRadius, self.width)#调用view类的circle函数绘制circle



def action(balls, width, view):

    rightMoving = [True] * len(balls)
    def animateBalls():
        for i, ball in enumerate(balls):
            if rightMoving[i]:
                if ball.maxX < width:
                    ball.moving(ball.Xspeed, 0)
                else:
                    rightMoving[i] = False
            else:
                if ball.x > 0:
                    ball.moving(-ball.Xspeed, 0)
                else:
                    rightMoving[i] = True

            ball.pulse()
            ball.draw(view)

    return animateBalls


def main(width):
    view = PygView(width)
    view.drawStatic()
    ball01 = Ball(50, 60, 50, 1, 1, (255, 255, 0))
    ball01.draw(view)

    ball02 = Ball(250, 150, 190, 1, 1, (66, 1, 166))
    ball02.draw(view)

    view.drawDynamic()
    ball1 = Ball(15, 130, 100, 5, 0, (255, 0, 0))
    ball2 = Ball(25, 200, 80, 5, 0, (0, 255, 155))
    ball3 = Ball(20, 220, 110, 5, 1, (100, 55, 155))
    ball4 = Ball(20, 400, 70, 5, 0, (250, 100, 255))
    ball5 = Ball(90, 390, 70, 5, 1, (250, 100, 255), 1)
    loopFunc = action((ball1, ball2, ball3, ball4, ball5), width, view)
    view.run(loopFunc)#传一个回调进去

if __name__ == '__main__':
    main(900)
