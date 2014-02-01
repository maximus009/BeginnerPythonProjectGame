import sys, pygame
pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
