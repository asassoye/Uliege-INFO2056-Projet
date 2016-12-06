import pygame

pygame.init()

time = pygame.time.Clock()
fini = False

SCALE = 32
LIMITES = [40, 20]

class World:
    def __init__(self):
        self.surface = pygame.display.set_mode([20 * SCALE, 12 * SCALE])
        pygame.display.flip()


class Carte:
    def __init__(self, elements, portes):
        self.elements = elements
        self.portes = portes

    def affichecarte(self):
        i = 0

        for lines in self.elements:
            j = 0

            for element in lines:
                imageBlock[element].dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()

    def quelblock(self, coordonnees):
        return imageBlock[self.elements[coordonnees[1]][coordonnees[0]]]

class ImageBlock:
    def __init__(self, nom, obstacle):
        self.nom = nom
        self.url = './imageBlock/' + nom + '.png'
        self.obstacle = obstacle
        self.surface = pygame.image.load(self.url).convert()
        self.surface = pygame.transform.scale(self.surface, (SCALE, SCALE))

    def dessine(self, coordonees):
        world.surface.blit(self.surface, [coordonees[0] * SCALE, coordonees[1] * SCALE])


class Personnage:
    def __init__(self, nom, position, pose, vie):
        self.nom = nom
        self.url = './personnageBlock/' + nom + '/'
        self.position = position
        self.pose = pose
        self.mort = False
        self.vie = vie
        self.surface = list()

        for pose in ['TOP', 'RIGHT', 'DOWN', 'LEFT']:
            self.surface.append(
                pygame.transform.scale(
                    pygame.image.load(self.url + pose + '.png'),
                    (SCALE, SCALE)
                )
            )

    def caseactuel(self):
        return carte.elements[self.position[1][1]][self.position[1][0]]

    def deplacer(self, evenement):
            imageBlock[self.caseactuel()].dessine([self.position[1][0], self.position[1][1]])
            if evenement.key == pygame.K_UP:
                if not self.limite('UP') and not self.obstacle('UP'):
                    self.position[1][1] -= 1
                    self.pose = 0
            if evenement.key == pygame.K_RIGHT:
                if not self.limite('RIGHT') and not self.obstacle('RIGHT'):
                    self.position[1][0] += 1
                    self.pose = 1
            if evenement.key == pygame.K_DOWN:
                if not self.limite('DOWN') and not self.obstacle('DOWN'):
                    self.position[1][1] += 1
                    self.pose = 2
            if evenement.key == pygame.K_LEFT:
                if not self.limite('LEFT') and not self.obstacle('LEFT'):
                    self.position[1][0] -= 1
                    self.pose = 3
            self.dessine()

    def limite(self, direction):
        if direction == 'UP':
            return self.position[1][1] == 0
        if direction == 'RIGHT':
            return self.position[1][0] == LIMITES[0] - 1
        if direction == 'DOWN':
            return self.position[1][1] == LIMITES[1] - 1
        if direction == 'LEFT':
            return self.position[1][0] == 0

    def obstacle(self, direction):
        if direction == 'UP':
            return carte.quelblock([self.position[1][0], self.position[1][1] - 1]).obstacle
        if direction == 'RIGHT':
            return carte.quelblock([self.position[1][0] + 1, self.position[1][1]]).obstacle
        if direction == 'DOWN':
            return carte.quelblock([self.position[1][0], self.position[1][1] + 1]).obstacle
        if direction == 'LEFT':
            return carte.quelblock([self.position[1][0] - 1, self.position[1][1]]).obstacle

    def dessine(self):
        world.surface.blit(self.surface[self.pose], [self.position[1][0] * SCALE, self.position[1][1] * SCALE])
        pygame.display.flip()


me = Personnage('Benoit', [[0], [1, 1]], 2, 1)
world = World()

imageBlock = list()
imageBlock.append(ImageBlock("0", False))
imageBlock.append(ImageBlock("1", False))
imageBlock.append(ImageBlock("2", False))
imageBlock.append(ImageBlock("3", False))
imageBlock.append(ImageBlock("4", True))
imageBlock.append(ImageBlock("5", True))
imageBlock.append(ImageBlock("6", True))
imageBlock.append(ImageBlock("7", True))
imageBlock.append(ImageBlock("8", False))
imageBlock.append(ImageBlock("9", True))
imageBlock.append(ImageBlock("10", True))

temp = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 6, 6, 6, 6, 6, 6, 6, 4],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 7, 6, 8, 6, 7, 6, 4],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 1, 4, 4, 4, 4],
        [9, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        ]

carte = Carte(temp, [0])
carte.affichecarte()

me.dessine()

while not fini:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:
            me.deplacer(evenement)
        if evenement.type == pygame.QUIT:
            fini = True

    time.tick(60)

pygame.display.quit()
pygame.quit()
exit()
