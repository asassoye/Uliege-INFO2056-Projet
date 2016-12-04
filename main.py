import pygame
pygame.init()

time = pygame.time.Clock()
fini = False

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


class ImageBlock:
    def __init__(self, nom, obstacle):
        self.nom = nom
        self.url = './imageBlock/' + nom + '.png'
        self.obstacle = obstacle
        self.surface = pygame.image.load(self.url)
        self.surface = pygame.transform.scale(self.surface, (GRANDEUR, GRANDEUR))

    def dessine(self, coordonees):
        world.surface.blit(self.surface, [coordonees[0] * GRANDEUR, coordonees[1] * GRANDEUR])


class Personnage:
    def __init__(self, nom, position, pose, vie):
        self.nom = nom
        self.url = './personnageBlock/' + nom + '.png'
        self.position = position
        self.pose = pose
        self.mort = False
        self.surface = pygame.image.load(self.url)
        self.vie = vie

    def deplacer(self, evenement):
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RIGHT:
                self.position[1][0] += 1
                self.dessine()

    def dessine(self):
        world.surface.blit(self.surface, [self.position[1][0], self.position[1][1]])
        pygame.display.flip()

me = Personnage('Andrew', [[0], [1, 1]], 2, 1)
world = World()

imageBlock = []
imageBlock.append(ImageBlock("0", False))
imageBlock.append(ImageBlock("1", False))

temp = [[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

carte = Carte(temp, temp)
carte.afficheCarte()

me.dessine()

while not fini:
    for evenement in pygame.event.get():
        me.deplacer(evenement)

        if evenement.type == pygame.QUIT:
            fini = True

    time.tick(60)

pygame.display.quit()
pygame.quit()
exit()