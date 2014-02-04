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
        player.velx = 3

    elif keyboard[pygame.K_LEFT] or keyboard[pygame.K_a]:
        player.image = pygame.image.load("assets/images/playerflipped.bmp")
        player.velx = -3

    else:
        player.velx = 0

    if keyboard[pygame.K_UP] or keyboard[pygame.K_w]:
        player.vely = -3

    elif keyboard[pygame.K_DOWN] or keyboard[pygame.K_s]:
        player.vely = 3

    else:
        player.vely = 0

    if keyboard[pygame.K_SPACE]:
        pass

    if keyboard[pygame.K_ESCAPE]:
        pygame.quit() #closes pygame
        sys.exit() #closes actual program
