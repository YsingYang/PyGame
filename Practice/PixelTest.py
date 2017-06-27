import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

def createScales(height):
    redScaleSurface = pygame.Surface((640, height))
    #为什么原文中是pygame.surface.Surface((640, height)), 这两者有什么区别?
    greenScaleSurface = pygame.Surface((640, height))
    blueScaleSurface = pygame.Surface((640, height))

    for x in range(640):
        c = int((x / 640.)*255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        lineRect = pygame.Rect(x, 0, 1, height)
        pygame.draw.rect(redScaleSurface, red, lineRect)
        pygame.draw.rect(greenScaleSurface, green, lineRect)
        pygame.draw.rect(blueScaleSurface, blue, lineRect)

    return redScaleSurface, greenScaleSurface, blueScaleSurface

redScale, greenScale, blueScale = createScales(80)

color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    screen.blit(redScale, (0, 0))
    screen.blit(greenScale, (0, 80))
    screen.blit(blueScale, (0, 160))

    x, y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if component * 80 and y < (component + 1) * 80:
                color[component] = int((x/639.)*255.)
        pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    for component in range(3):
        pos = (int ((color[component]/255.) * 639), component * 80 + 40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.update()


