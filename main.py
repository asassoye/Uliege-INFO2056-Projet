import pygame

"""
"
" Classe World, initialisation de pygame et affichage de la carte, joueurs
"
"""


class World:
    def __init__(self):
        pygame.init()
        self.time = pygame.time.Clock()
        self.SCALE = 40
        self.LIMITES = [30, 18]
        self.surface = pygame.display.set_mode([self.LIMITES[0] * self.SCALE, self.LIMITES[1] * self.SCALE])
        self.ending = False
        self.imageBlock = list()
        self.level = list()
        self.player = list()
        self.carte = object()
        pygame.display.flip()

    """
    "
    " Demarrage du jeu: initialisations des blocks joueurs et levels
    "
    """

    def start(self):
        self.initblocks()
        self.initlevels()
        self.initplayers()
        while not self.ending:
            self.eventlistener()
            self.time.tick(60)

        pygame.display.quit()
        pygame.quit()
        exit()

    """
    "
    " Verifie les entrées au clavier
    "
    """

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

    """
    "
    " initialisation des differents blocks
    "
    """

    def initblocks(self):
        self.imageBlock.append(ImageBlock("0", False))
        self.imageBlock.append(ImageBlock("1", False))
        self.imageBlock.append(ImageBlock("2", False))
        self.imageBlock.append(ImageBlock("3", True))
        self.imageBlock.append(ImageBlock("4", True))
        self.imageBlock.append(ImageBlock("5", True))
        self.imageBlock.append(ImageBlock("6", True))
        self.imageBlock.append(ImageBlock("7", True))
        self.imageBlock.append(ImageBlock("8", True))
        self.imageBlock.append(ImageBlock("9", True))
        self.imageBlock.append(ImageBlock("10", True))
        self.imageBlock.append(ImageBlock("11", True))
        self.imageBlock.append(ImageBlock("12", True))
        self.imageBlock.append(ImageBlock("13", True))
        self.imageBlock.append(ImageBlock("14", True))
        self.imageBlock.append(ImageBlock("15", True))
        self.imageBlock.append(ImageBlock("16", True))
        self.imageBlock.append(ImageBlock("17", True))

    """
    "
    " initialisation des joureurs
    "
    """

    def initplayers(self):
        self.player.append(Personnage('Andrew', [[0], [1, 1]], 2))
        self.player.append(Personnage('Dominik', [[0], [1, 2]], 2))

    """
    "
    " initalisations des diferents levels
    "
    """

    def initlevels(self):
        self.level.append(
            [#1  2  3  4  5  6  7  8  9 10 11 12 13 14 15"16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
            [ 3, 7, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7, 7, 3], #1
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #2
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #3
            [12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,13], #4
            [ 2, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2, 2], #5
            [ 2, 2, 2, 2, 4, 3, 6, 2, 2, 2, 4, 3, 6, 2, 2, 2, 2, 4, 3, 6, 2, 2, 2, 4, 3, 6, 2, 2, 2, 2], #6
            [ 2, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2, 2], #7
            [11, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,10], #8
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,10,11, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #9
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,13,12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #10
            [12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,13], #11
            [ 2, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2, 2], #12
            [ 2, 2, 2, 2, 4, 3, 6, 2, 2, 2, 4, 3, 6, 2, 2, 2, 2, 4, 3, 6, 2, 2, 2, 4, 3, 6, 2, 2, 2, 2], #13
            [ 2, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2, 2,13, 7,12, 2, 2, 2,13, 7,12, 2, 2, 2, 2], #14
            [11, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,10], #15
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #16
            [ 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], #17
            [ 3, 5, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5, 5,11, 2, 2, 2,10, 5,11, 2, 2, 2,10, 5, 5, 3]  #18
            ]
        )

        self.carte = Carte(self.level[0])
        self.carte.affichecarte()


"""
"
" Classe Carte, structure de la carte a l'affichage
"
"""


class Carte:
    def __init__(self, elements):
        self.elements = elements

    """
    "
    " Affichage de la carte
    "
    """

    def affichecarte(self):
        i = 0

        for lines in self.elements:
            j = 0

            for element in lines:
                world.imageBlock[element].dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()

    """
    "
    " Return l'objet block se trouvant aux coordonnées données
    "
    """

    def quelblock(self, coordonnees):
        return world.imageBlock[self.elements[coordonnees[1]][coordonnees[0]]]


"""
"
" Class imageBlock: proprietés des blocks differents (obstacles ou pas etc)
"
"""


class ImageBlock:
    def __init__(self, nom, obstacle):
        self.nom = nom
        self.url = './imageBlock/' + nom + '.png'
        self.obstacle = obstacle
        self.surface = pygame.image.load(self.url).convert()
        self.surface = pygame.transform.scale(self.surface, (world.SCALE, world.SCALE))

    """
    "
    " Dessine le block sur la carte par rapport aux coordonnées données
    "
    """

    def dessine(self, coordonees):
        world.surface.blit(self.surface, [coordonees[0] * world.SCALE, coordonees[1] * world.SCALE])


"""
"
" Class Personnage: Personnage et leur proprietés
"
"""


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

    """
    "
    " Renvoi le type d'element (block) se trouvant a sa position
    "
    """

    def caseactuel(self):
        return world.carte.elements[self.position[1][1]][self.position[1][0]]

    """
    "
    " Recois la direction du eventlistener et se deplace si il peut se deplacer (verifie les obstacles, les limites de
    " la fenetre et les autres personnages)
    "
    """

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

    """
    "
    " Verifie si il depace une limite en se deplacant dans $direction
    "
    """

    def limite(self, direction):
        if direction == 'UP':
            return self.position[1][1] == 0
        if direction == 'RIGHT':
            return self.position[1][0] == world.LIMITES[0] - 1
        if direction == 'DOWN':
            return self.position[1][1] == world.LIMITES[1] - 1
        if direction == 'LEFT':
            return self.position[1][0] == 0

    """
    "
    " Verifie si en se deplacant on se deplace sur un obstacle par rapport a $direction
    "
    """

    def obstacle(self, direction):
        if direction == 'UP':
            return world.carte.quelblock([self.position[1][0], self.position[1][1] - 1]).obstacle
        if direction == 'RIGHT':
            return world.carte.quelblock([self.position[1][0] + 1, self.position[1][1]]).obstacle
        if direction == 'DOWN':
            return world.carte.quelblock([self.position[1][0], self.position[1][1] + 1]).obstacle
        if direction == 'LEFT':
            return world.carte.quelblock([self.position[1][0] - 1, self.position[1][1]]).obstacle

    """
    "
    " Verifie si en se deplacant on se deplace sur un autre personnage par rapport a $direction
    "
    """

    def autrepersonne(self, direction):
        if direction == 'UP':
            if self.nom == 'Andrew':
                return self.position[1][1] == world.player[1].position[1][1] + 1 and self.position[1][0] == \
                                                                                     world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] + 1 and self.position[1][0] == \
                                                                                     world.player[0].position[1][0]
        if direction == 'RIGHT':
            if self.nom == 'Andrew':
                return self.position[1][0] == world.player[1].position[1][0] - 1 and self.position[1][1] == \
                                                                                     world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] - 1 and self.position[1][1] == \
                                                                                     world.player[0].position[1][1]
        if direction == 'DOWN':
            if self.nom == 'Andrew':
                return self.position[1][1] == world.player[1].position[1][1] - 1 and self.position[1][0] == \
                                                                                     world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] - 1 and self.position[1][0] == \
                                                                                     world.player[0].position[1][0]
        if direction == 'LEFT':
            if self.nom == 'Andrew':
                return self.position[1][0] == world.player[1].position[1][0] + 1 and self.position[1][1] == \
                                                                                     world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] + 1 and self.position[1][1] == \
                                                                                     world.player[0].position[1][1]

    """
    "
    " Affiche le personnage par rapport a sa postion
    "
    """

    def dessine(self):
        world.surface.blit(self.surface[self.pose],
                           [self.position[1][0] * world.SCALE, self.position[1][1] * world.SCALE])
        pygame.display.flip()


"""
"
" Initialise le monde et demarre
"
"""
world = World()
world.start()
