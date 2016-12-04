import pygame
pygame.init()

GRANDEUR = 64


class World:
    def __init__(self):
        self.surface = pygame.display.set_mode([30 * GRANDEUR, 15 * GRANDEUR])
        pygame.display.flip()

