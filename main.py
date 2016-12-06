import pygame

pygame.init()

time = pygame.time.Clock()
fini = False

SCALE = 32
LIMITES = [40, 20]


class World:
    def __init__(self):
        self.surface = pygame.display.set_mode([LIMITES[0] * SCALE, LIMITES[1] * SCALE])
        self.ending = False
        pygame.display.flip()

    def eventlistener(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.ending = True
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_z:
                    player[0].deplacer('UP')
                if evenement.key == pygame.K_d:
                    player[0].deplacer('RIGHT')
                if evenement.key == pygame.K_s:
                    player[0].deplacer('DOWN')
                if evenement.key == pygame.K_q:
                    player[0].deplacer('LEFT')
                if evenement.key == pygame.K_UP:
                    player[1].deplacer('UP')
                if evenement.key == pygame.K_RIGHT:
                    player[1].deplacer('RIGHT')
                if evenement.key == pygame.K_DOWN:
                    player[1].deplacer('DOWN')
                if evenement.key == pygame.K_LEFT:
                    player[1].deplacer('LEFT')

    def start(self):
        while not self.ending:
            self.eventlistener()

            time.tick(60)

        pygame.display.quit()
        pygame.quit()
        exit()


class Carte:
    def __init__(self, elements):
        self.elements = elements

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
    def __init__(self, nom, position, pose):
        self.nom = nom
        self.url = './personnageBlock/' + nom + '/'
        self.position = position
        self.pose = pose
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
        if evenement == 'UP':
            if not self.limite('UP') and not self.obstacle('UP'):
                self.position[1][1] -= 1
                self.pose = 0
        if evenement == 'RIGHT':
            if not self.limite('RIGHT') and not self.obstacle('RIGHT'):
                self.position[1][0] += 1
                self.pose = 1
        if evenement == 'DOWN':
            if not self.limite('DOWN') and not self.obstacle('DOWN'):
                self.position[1][1] += 1
                self.pose = 2
        if evenement == 'LEFT':
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


player = list()
player.append(Personnage('Andrew', [[0], [1, 1]], 2))
player.append(Personnage('Dominik', [[0], [38, 18]], 2))

world = World()

imageBlock = list()
imageBlock.append(ImageBlock("0", False))
imageBlock.append(ImageBlock("1", False))
imageBlock.append(ImageBlock("2", False))
imageBlock.append(ImageBlock("3", True))


temp = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

carte = Carte(temp)
carte.affichecarte()


player[0].dessine()
player[1].dessine()


while not fini:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:
            player[1].deplacer(evenement)
        if evenement.type == pygame.QUIT:
            fini = True

    time.tick(60)

pygame.display.quit()
pygame.quit()
exit()
