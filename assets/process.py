import pygame, sys

def keystrokes(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #closes pygame
            sys.exit() #closes actual program

    keyboard = pygame.key.get_pressed()

    #Keyboard Commands
    if keyboard[pygame.K_RIGHT] or keyboard[pygame.K_d]:
        player.image = pygame.image.load("assets/images/player.bmp")
        player.velx = 5

    elif keyboard[pygame.K_LEFT] or keyboard[pygame.K_a]:
        player.image = pygame.image.load("assets/images/playerflipped.bmp")
        player.velx = -5

    else:
        player.velx = 0

    if keyboard[pygame.K_SPACE]:
        player.jumping = True

    if keyboard[pygame.K_ESCAPE]:
        pygame.quit() #closes pygame
        sys.exit() #closes actual program

def menu(BaseClass, screen, clock, FPS, MenuImage, Button):
    screen.blit(MenuImage.image, (0,0) )
    screen.blit(Button.image, (280,230) )
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            mouseX, mouseY = pygame.mouse.get_pos()
            if Button.rect.collidepoint(mouseX, mouseY):
                Button.image = pygame.image.load("assets/images/buttonpress.bmp")
                screen.blit(Button.image, (280,230) )
                pygame.display.flip()
                
                pygame.time.delay(100)
                return True

        if event.type == pygame.QUIT:
            pygame.quit() #closes pygame
            sys.exit() #closes actual program
            
    return False

def spike(Spike,screen,clock,FPS,player,pygame,SCREENWIDTH,SCREENHEIGHT,knockback):
    screen.blit(Spike.image, (Spike.x,Spike.y))
    if pygame.sprite.collide_rect(player, Spike):
        player.velx = -20
        player.health -= 10
        player.motion(SCREENWIDTH, SCREENHEIGHT)
        return 5
    else:
        return knockback

def drawText(xpos, ypos, string, COLOUR, font_type, font_size, screen):
    txt = string
    txtfont = pygame.font.SysFont(font_type, font_size)
    displayTxt= txtfont.render(txt, 1, COLOUR)
    screen.blit(displayTxt, (xpos, ypos))