import pygame


class World:
    def __init__(self):
        pygame.init()
        self.time = pygame.time.Clock()
        self.SCALE = 32
        self.LIMITES = [40, 20]
        self.surface = pygame.display.set_mode([self.LIMITES[0] * self.SCALE, self.LIMITES[1] * self.SCALE])
        self.ending = False
        self.imageBlock = list()
        self.maps = list()
        self.player = list()
        self.carte = object()
        pygame.display.flip()

    def start(self):
        self.initblocks()
        self.initmaps()
        self.initplayers()
        while not self.ending:
            self.eventlistener()
            self.time.tick(60)

        pygame.display.quit()
        pygame.quit()
        exit()

    def eventlistener(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.ending = True
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_z:
                    self.player[0].deplacer('UP')
                if evenement.key == pygame.K_d:
                    self.player[0].deplacer('RIGHT')
                if evenement.key == pygame.K_s:
                    self.player[0].deplacer('DOWN')
                if evenement.key == pygame.K_q:
                    self.player[0].deplacer('LEFT')
                if evenement.key == pygame.K_UP:
                    self.player[1].deplacer('UP')
                if evenement.key == pygame.K_RIGHT:
                    self.player[1].deplacer('RIGHT')
                if evenement.key == pygame.K_DOWN:
                    self.player[1].deplacer('DOWN')
                if evenement.key == pygame.K_LEFT:
                    self.player[1].deplacer('LEFT')

    def initblocks(self):
        self.imageBlock.append(ImageBlock("0", False))
        self.imageBlock.append(ImageBlock("1", False))
        self.imageBlock.append(ImageBlock("2", False))
        self.imageBlock.append(ImageBlock("3", True))

    def initplayers(self):
        self.player.append(Personnage('Andrew', [[0], [1, 1]], 2))
        self.player.append(Personnage('Dominik', [[0], [38, 18]], 2))

    def initmaps(self):
        self.maps.append(
            [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
              3, 3, 3, 3, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 3],
             [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
              3, 3, 3, 3, 3]
             ]
        )

        self.carte = Carte(self.maps[0])
        self.carte.affichecarte()


class Carte:
    def __init__(self, elements):
        self.elements = elements

    def affichecarte(self):
        i = 0

        for lines in self.elements:
            j = 0

            for element in lines:
                world.imageBlock[element].dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()

    def quelblock(self, coordonnees):
        return world.imageBlock[self.elements[coordonnees[1]][coordonnees[0]]]


class ImageBlock:
    def __init__(self, nom, obstacle):
        self.nom = nom
        self.url = './imageBlock/' + nom + '.png'
        self.obstacle = obstacle
        self.surface = pygame.image.load(self.url).convert()
        self.surface = pygame.transform.scale(self.surface, (world.SCALE, world.SCALE))

    def dessine(self, coordonees):
        world.surface.blit(self.surface, [coordonees[0] * world.SCALE, coordonees[1] * world.SCALE])


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
                    (world.SCALE, world.SCALE)
                )
            )
        self.dessine()

    def caseactuel(self):
        return world.carte.elements[self.position[1][1]][self.position[1][0]]

    def deplacer(self, evenement):
        world.imageBlock[self.caseactuel()].dessine([self.position[1][0], self.position[1][1]])
        if evenement == 'UP':
            if not self.limite(evenement) and not self.obstacle(evenement) and not self.autrepersonne(evenement):
                self.position[1][1] -= 1
                self.pose = 0
        if evenement == 'RIGHT':
            if not self.limite(evenement) and not self.obstacle(evenement) and not self.autrepersonne(evenement):
                self.position[1][0] += 1
                self.pose = 1
        if evenement == 'DOWN':
            if not self.limite(evenement) and not self.obstacle(evenement) and not self.autrepersonne(evenement):
                self.position[1][1] += 1
                self.pose = 2
        if evenement == 'LEFT':
            if not self.limite(evenement) and not self.obstacle(evenement) and not self.autrepersonne(evenement):
                self.position[1][0] -= 1
                self.pose = 3
        self.dessine()

    def limite(self, direction):
        if direction == 'UP':
            return self.position[1][1] == 0
        if direction == 'RIGHT':
            return self.position[1][0] == world.LIMITES[0] - 1
        if direction == 'DOWN':
            return self.position[1][1] == world.LIMITES[1] - 1
        if direction == 'LEFT':
            return self.position[1][0] == 0

    def obstacle(self, direction):
        if direction == 'UP':
            return world.carte.quelblock([self.position[1][0], self.position[1][1] - 1]).obstacle
        if direction == 'RIGHT':
            return world.carte.quelblock([self.position[1][0] + 1, self.position[1][1]]).obstacle
        if direction == 'DOWN':
            return world.carte.quelblock([self.position[1][0], self.position[1][1] + 1]).obstacle
        if direction == 'LEFT':
            return world.carte.quelblock([self.position[1][0] - 1, self.position[1][1]]).obstacle

    def autrepersonne(self, direction):
        if direction == 'UP':
            if self.nom == 'Andrew':
                return self.position[1][1] == world.player[1].position[1][1] + 1 and self.position[1][0] == world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] + 1 and self.position[1][0] == world.player[0].position[1][0]
        if direction == 'RIGHT':
            if self.nom == 'Andrew':
                return self.position[1][0] == world.player[1].position[1][0] - 1 and self.position[1][1] == world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] - 1 and self.position[1][1] == world.player[0].position[1][1]
        if direction == 'DOWN':
            if self.nom == 'Andrew':
                return self.position[1][1] == world.player[1].position[1][1] - 1 and self.position[1][0] == world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] - 1 and self.position[1][0] == world.player[0].position[1][0]
        if direction == 'LEFT':
            if self.nom == 'Andrew':
                return self.position[1][0] == world.player[1].position[1][0] + 1 and self.position[1][1] == world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] + 1 and self.position[1][1] == world.player[0].position[1][1]

    def dessine(self):
        world.surface.blit(self.surface[self.pose],
                           [self.position[1][0] * world.SCALE, self.position[1][1] * world.SCALE])
        pygame.display.flip()


world = World()
world.start()
