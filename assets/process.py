import pygame, sys

try:
    import urllib.request as urllib2
except:
    import urllib2
#This function checks if the user has pressed a keyboard key
def keystrokes(player, playing, update_version,bullet):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #closes pygame
            sys.exit() #closes actual program

    keyboard = pygame.key.get_pressed()

    #Keyboard Commands
    if keyboard[pygame.K_RIGHT] or keyboard[pygame.K_d]:
        player.image = pygame.image.load("assets/images/playerRight.bmp")
        player.velx = 5

    elif keyboard[pygame.K_LEFT] or keyboard[pygame.K_a]:
        player.image = pygame.image.load("assets/images/playerLeft.bmp")
        player.velx = -5

    else:
        player.velx = 0

    if keyboard[pygame.K_UP] or keyboard[pygame.K_w]:
        player.image = pygame.image.load("assets/images/playerUp.bmp")
        player.vely = -5

    elif keyboard[pygame.K_DOWN] or keyboard[pygame.K_s]:
        player.image = pygame.image.load("assets/images/playerDown.bmp")
        player.vely = 5

    else:
        player.vely = 0

    if keyboard[pygame.K_SPACE]:
        player.shoot(bullet)

    if keyboard[pygame.K_ESCAPE]:
        pygame.quit() #closes pygame
        sys.exit() #closes actual program

    if keyboard[pygame.K_TAB]:
        print("WOOT")

    if keyboard[pygame.K_LCTRL] and keyboard[pygame.K_d]:
        option = input()
        if option.lower() == "update":
            update_version()
        elif option.lower() == "god": #not true god, but damn close enough just for fun ;)
            player.health = 1000000
        option = ""
#This function is what displays the mainmenu. It handles anything related to it such as the mouse clicking buttons etc...
#This also handles version checking
def mainMenu(BaseClass, screen, clock, FPS, MenuImage, Button, ExitButton,update_check):
    screen.blit(MenuImage.image, (0,0) )
    screen.blit(Button.image, (280,230) )
    screen.blit(ExitButton.image, (280,260) )
    pygame.display.flip()

    if update_check == False:
        url = "http://zipy124.github.io/BeginnerPythonProjectGame/v/version.txt"
        file = urllib2.urlopen(url, None, 2.5)
        data = file.read()
        with open("v.txt", "wb") as code:
            code.write(data)
        my_file = open("v.txt","r")
        txt = my_file.readline()
        my_file.close()
        
        my_file = open("version.txt","r")
        txt2 = my_file.readline()

        if float(txt) == float(txt2) : #this is the current file version number (0.0 followed by number of commits atm 170)
            print("Up to date")
        elif float(txt) < float(txt2):
            print("Web version file needs updating")
        else:
            print("Please update from our github repositry!")
        my_file.close()

    for event in pygame.event.get(): #This checks if the user has clicked on the button or not
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            mouseX, mouseY = pygame.mouse.get_pos()
            if Button.rect.collidepoint(mouseX, mouseY):
                Button.image = pygame.image.load("assets/images/buttonpress.bmp")
                screen.blit(Button.image, (280,230) )
                pygame.display.flip()
                
                pygame.time.delay(100)
                return True

            elif ExitButton.rect.collidepoint(mouseX, mouseY):
                pygame.quit()
                sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit() #closes pygame
            sys.exit() #closes actual program
            
    return False
#This is like the main menu function but instead is for the in-game menu for if you die or eventually if you pause the game.
def inGameMenu(BaseClass, screen, clock, FPS, MenuImage, Button, ExitButton, player, SCREENHEIGHT):
    screen.blit(MenuImage.image, (0,0) )
    screen.blit(Button.image, (280,230) )
    screen.blit(ExitButton.image, (280,260) )
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            mouseX, mouseY = pygame.mouse.get_pos()
            if Button.rect.collidepoint(mouseX, mouseY):
                Button.image = pygame.image.load("assets/images/tryAgainButton.bmp")
                screen.blit(Button.image, (280,230) )
                pygame.display.flip()

                reset(player, SCREENHEIGHT)
                
                pygame.time.delay(100)
                return True

            elif ExitButton.rect.collidepoint(mouseX, mouseY):
                pygame.quit()
                sys.exit()


        if event.type == pygame.QUIT:
            pygame.quit() #closes pygame
            sys.exit() #closes actual program
            
    return False
#This function handles collision checking for the spike which will eventually be adapted into an obstacle class
def spike(Spike,screen,clock,FPS,player,pygame,SCREENWIDTH,SCREENHEIGHT,knockback,background):
    screen.blit(Spike.image, (Spike.x,Spike.y))
    if pygame.sprite.collide_rect(player, Spike):
        if pygame.sprite.collide_mask(player, Spike):
            print("collision at",pygame.sprite.collide_mask(player, Spike))
            if player.velx > 0:
                player.velx = -20
            elif player.velx < 0:
                player.velx = 20
            elif player.vely > 0:
                player.vely = -20
            else:
                player.vely = 20

            player.health -= 10
            player.motion(SCREENWIDTH, SCREENHEIGHT,background,Spike)
            return 5
        else:
            return knockback
    else:
        return knockback
#This is an example function for a wall object. It is currently not in use
def wall(wall,screen,clock,FPS,player,pygame,SCREENWIDTH,SCREENHEIGHT,Spike):
    screen.blit(wall.image, (wall.x,wall.y))
    if pygame.sprite.collide_rect(player, wall):
        if pygame.sprite.collide_mask(player, wall):
            print("collision at",pygame.sprite.collide_mask(player, wall))
            player.velx = 0
            player.vely = 0
            player.motion(SCREENWIDTH, SCREENHEIGHT,background,Spike)
#this is the function to draw text
def drawText(xpos, ypos, string, COLOUR, font_style, font_size, screen):
    txt = string
    txtfont = pygame.font.SysFont(font_style, font_size)
    displayTxt= txtfont.render(txt, 1, COLOUR)
    screen.blit(displayTxt, (xpos, ypos))

#Places player back at the default spawn point and resets health
def reset(player, SCREENHEIGHT):
    player.health = 100
    player.rect.x = 0
    player.rect.y = SCREENHEIGHT - 128
    player.image = pygame.image.load("assets/images/playerRight.bmp")
