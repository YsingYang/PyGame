
import pygame
import os


def getAlphaSurface(surf, alpha = 128, red = 128, green = 128, blue = 128, mode = pygame.BLEND_RGBA_MULT):
#接受一个surface, 返回一个有alpha的surface
    tmp = pygame.Surface(surf.get_size(), pygame.SRCALPHA, 32)
    tmp.fill((red, green, blue, alpha))
    tmp.blit(surf, (0, 0), surf.get_rect(), mode)#将原surface放在alpha surfaceshagn
    return tmp

def bounce(value, direction, bouncing = True, valuemin = 0, valuemax = 255):
    """bouncing a value (like alpha or color) between 00
           baluemin and valuemax. 
           When bouncing is True,
           direction (usually -1 or 1)  is inverted when reaching valuemin or valuemax"""
    value += direction #increase or decrase value by direction
    if value <= valuemin:
        value = valuemin
        if bouncing:
            direction *= -1
    elif value >= valuemax:
        value = valuemax
        if bouncing:
            direction *= -1
    return value, direction #这样的返回是返回一个元组吗?

def write(msg = 'pygame is cool', size = 24, color=(255, 255, 255)):
    myfont = pygame.font.SysFont('None', size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext

def alphademo(width = 800, height = 600):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size()).convert()

    venus = pygame.image.load(os.path.join('resource', '800px-La_naissance_de_Venus.jpg')).convert()
    #载入图片

    ## transform venus and blit on background in one go,首先要将图片大小scale
    pygame.transform.scale(venus, (width, height), background)
    pngMoster = pygame.image.load(os.path.join('resource', "colormonster.png")).convert_alpha()#png格式能直接convert_alpha()

    pngMoster0 = pngMoster.copy() #a deep copy
    pngMoster3 = pngMoster.copy() #copy for per-pixel alpha()

    #---------------------jpg image ---------------------

    jpgMonster = pygame.image.load(os.path.join('resource', "colormonster.jpg")).convert()
    jpgMonster0 = jpgMonster.copy() #copy of jpg
    jpgMonster1 = jpgMonster.copy() # another copy to demonstrate colorkey

    jpgMonster1.set_colorkey((255, 255, 255))
    #例如，给 colorkey 设定一个RGB值 (255, 255, 255)，则加载后的图片中，
    # 原来像素值为 (255, 255, 255) 的点，都会变得透明。上面的代码中，
    # 如果给 colorkey 传的值为 -1则会以原图最左上角的那个点的颜色值作为色键。
    jpgMonster1.convert_alpha()

    jpgMonster2  = jpgMonster.copy()# another copy for surface alpha
    jpgMonster3 = jpgMonster.copy()

    # -----------------text surface ----------------------
    png0text = write("png (has alpha)")
    png3text = write("png with pixel-alpha")
    jpg0text = write("jpg (no alpha)")
    jpg1text = write("jpg with colorkey")
    jpg2text = write("jpg with surface alpha")
    jpg3text = write("jpg with pixel-alpha")

    # ------- for bitmap-alpha --------
    alpha = 128
    direction = 1
    # ---------- for per-pixel-alpha---------------
    r, g, b, a  = 255, 255, 255, 255
    modeNr = 7
    # index 7, int-value 8, name="BLEND_RGB_MULT" ,usage = pygame.BLEND_RGB_MULT

    paper = pygame.Surface((400, 100))
    #paper.fill((0, 0, 0))
    paper.set_alpha(128)

    modelist = ["BLEND_ADD",
                "BLEND_SUB",
                "BLEND_MULT",
                "BLEND_MIN",
                "BLEND_MAX",
                "BLEND_RGBA_ADD",
                "BLEND_RGBA_SUB",
                "BLEND_RGBA_MULT",
                "BLEND_RGBA_MIN",
                "BLEND_RGBA_MAX"]


    # -------  mainloop ----------
    clock = pygame.time.Clock()
    mainloop = True
    effects = False
    while mainloop:
        clock.tick(30)
        screen.blit(background, (0, 0))
        pygame.display.set_caption(
            "insert/del=red:%i, home/end=green:%i, pgup/pgdwn=blue:%i, +/-=pixalpha:%i press ESC" % (r, g, b, a))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # modeNr += 1
                    # if modeNr > 9:
                    #    modeNr = 0 # cycle throug number 0 to 9
                    modeNr = (modeNr + 1) % len(modelist)

        mode = pygame.constants.__dict__[modelist[modeNr]]

        dr, dg, db, da = 0, 0, 0, 0
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_PAGEUP]:
            db = 1  # blue up
        if pressedKeys[pygame.K_PAGEDOWN]:
            db = -1  # blue down
        if pressedKeys[pygame.K_HOME]:
            dg = 1  # green up
        if pressedKeys[pygame.K_END]:
            dg = -1  # green down
        if pressedKeys[pygame.K_INSERT]:
            dr = 1  # red up
        if pressedKeys[pygame.K_DELETE]:
            dr = -1  # red down
        if pressedKeys[pygame.K_u]:
            da = 1  # alpha up
        if pressedKeys[pygame.K_MINUS]:
            da = -1  # alpha down

        alpha, direction  = bounce(alpha, direction) #change alpha
        r, dr = bounce(r, dr, False)  # red for per-pixel
        g, dg = bounce(g, dg, False)  # green for per-pixel
        b, db = bounce(b, db, False)  # blue for per-pixel
        a, da = bounce(a, da, False)  # alpha for per-pixel


        # ------- change color and alpha values --------
        screen.blit(jpgMonster0, (0, 300))
        screen.blit(jpg0text, (0, 550))

        # ------blit jpgMonster1 with the colorkey set to white ------
        screen.blit(jpgMonster1, (200, 300))
        screen.blit(jpg1text, (200, 550))

        # ----- blit jpgmonster2 with alpha for whole  surface  --------
        jpgMonster2.set_alpha(alpha)# alpha for whole surface
        screen.blit(jpgMonster2, (400, 300)) #blit on screen
        screen.blit(jpg2text, (400, 550))
        screen.blit(write("surface-alpha: %i" % alpha), (400, 570))

        # ----- blit jpgmonster3 with per-pixel alpha-------
        tmp = getAlphaSurface(jpgMonster3, a, r, g, b, mode)# get current alpha
        screen.blit(tmp, (600, 300))
        screen.blit(jpg3text, (600, 550))

        # ----- blit pngMonster0 as it is, with transparency from image ---
        screen.blit(pngMoster0, (0, 10))
        screen.blit(png0text, (0, 200))

        tmp = getAlphaSurface(pngMoster3, a, r, g, b, mode)
        screen.blit(tmp, (600, 10))
        screen.blit(png3text, (600, 200))

        screen.blit(paper, (188, 150))##  semi-transparent background for instructions

        screen.blit(write("press [INS] / [DEL] to change red value: %i" % r, 24, (255, 255, 255)), (190, 150))
        screen.blit(write("press [HOME] / [END] to change green value: %i" % g), (190, 170))
        screen.blit(write("press [PgUp] / [PgDwn] to chgange blue value: %i" % b), (190, 190))
        screen.blit(write("press [Enter] for mode: %i (%s)" % (mode, modelist[modeNr])), (190, 230))
        screen.blit(write("press [+] / [-] (Keypad) to chgange alpha value: %i" % a), (190, 210))

        pygame.display.flip()


if __name__ == '__main__':
    alphademo()















