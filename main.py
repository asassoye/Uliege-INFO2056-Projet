import pygame
pygame.init()

GRANDEUR = 64


class World:
    def __init__(self):
        self.surface = pygame.display.set_mode([30 * GRANDEUR, 15 * GRANDEUR])
        pygame.display.flip()


class Carte:
    def __init__(self, elements, portes):
        self.elements = elements
        self.portes = portes

    def afficheCarte(self):
        i=0

        for lines in self.elements:
            j=0

            for element in lines:
                imageBlock[element].dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()
