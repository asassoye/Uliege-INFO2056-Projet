import copy
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
        self.FPS = 60
        self.SCALE = 40
        self.LIMITES = [30, 18]
        self.surface = pygame.display.set_mode(
            [self.get_limites('x') * self.get_scale(), self.get_limites('y') * self.get_scale()])
        pygame.display.set_caption('SplatULg')
        self.environnement = str()
        self.ending = False
        self.imageBlock = list()
        self.level = list()
        self.player = list()
        self.carte = Carte([])
        pygame.display.flip()

    """
    "
    " Getter/Setter Attr "time"
    "
    """

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    """
    "
    " Getter Attr "FPS"
    "
    """

    def get_fps(self):
        return self.FPS

    """
    "
    " GetterAttr "SCALE"
    "
    """

    def get_scale(self):
        return self.SCALE

    """
    "
    " Getter Attr "LIMITES"
    "
    """

    def get_limites(self, axe=None):
        if axe == 'x':
            return self.LIMITES[0]
        elif axe == 'y':
            return self.LIMITES[1]
        else:
            return self.LIMITES

    """
    "
    " Getter/Setter Attr "surface"
    "
    """

    def get_surface(self):
        return self.surface

    def set_surface(self, surface):
        self.surface = surface

    """
    "
    " Getter/Setter Attr "environnement"
    "
    """

    def get_environnement(self):
        return self.environnement

    def set_environnement(self, environnement):
        self.environnement = environnement

    """
    "
    " Getter/Setter Attr "ending"
    "
    """

    def get_ending(self):
        return self.ending

    def set_ending(self, ending):
        self.ending = ending

    """
    "
    " Getter/Setter Attr "imageBlock"
    "
    """

    def get_imageblock(self, id=None):
        if id != None:
            return self.imageBlock[id]
        else:
            return self.imageBlock

    def set_imageblock(self, imageblock):
        self.imageBlock = imageblock

    def add_imageblock(self, imageblock):
        self.imageBlock.append(imageblock)

    """
    "
    " Getter/Setter Attr "level"
    "
    """

    def get_level(self, id=None):
        if id != None:
            return self.level[id]
        else:
            return self.level

    def set_level(self, level):
        self.level = level

    def add_level(self, level):
        self.level.append(level)

    """
    "
    " Getter/Setter Attr "player"
    "
    """

    def get_player(self, id=None):
        if id != None:
            return self.player[id]
        else:
            return self.player

    def set_player(self, player):
        self.player = player

    def add_player(self, player):
        self.player.append(player)

    """
    "
    " Getter/Setter Attr "carte"
    "
    """

    def get_carte(self):
        return self.carte

    def set_carte(self, carte):
        self.carte = carte

    """
    "
    " Demarrage du jeu: initialisations des blocks joueurs et levels
    "
    """

    def init(self):
        self.set_environnement('menu')
        self.initblocks()
        self.initlevels()
        self.initplayers()
        while not self.get_ending():
            if self.get_environnement() == 'menu':
                self.showmenu()

            if self.get_environnement() == 'playing':
                self.play()

            if self.get_environnement() == 'level':
                self.showlevel()

            if self.get_environnement() == 'score':
                self.showscore()


            self.get_time().tick(self.get_fps())

        pygame.display.quit()
        pygame.quit()
        exit()

    def showmenu(self):
        menu = list()

        menu.append(pygame.image.load('./img/menu/main.png').convert())
        menu[0] = pygame.transform.scale(menu[0],
                                         (self.get_limites('x') * self.get_scale(),
                                          self.get_limites('y') * self.get_scale()))

        menu.append(pygame.image.load('./img/menu/mainanim.png').convert())
        menu[1] = pygame.transform.scale(menu[1],
                                         (self.get_limites('x') * self.get_scale(),
                                          self.get_limites('y') * self.get_scale()))

        actual = 1
        tmp = 0
        while self.get_environnement() == 'menu' and not self.get_ending():
            tmp += 1
            if tmp == 6:
                actual = not actual
                self.get_surface().blit(menu[actual], [0, 0])
                pygame.display.flip()
                tmp = 0
            self.eventlistener()
            self.get_time().tick(60)

    def showlevel(self):
        level = pygame.image.load('./img/menu/level.png').convert()
        level = pygame.transform.scale(level,
                                       (self.get_limites('x') * self.get_scale(),
                                        self.get_limites('y') * self.get_scale()))
        self.get_surface().blit(level, [0, 0])
        pygame.display.flip()
        while self.get_environnement() == 'level' and not self.get_ending():
            self.eventlistener()
            self.get_time().tick(self.get_fps())

    def play(self):
        time = 2 * 60 * self.get_fps()
        while self.get_environnement() == 'playing' and not self.get_ending():
            if time != 0:
                self.get_player(0).diminuepenalite()
                self.get_player(1).diminuepenalite()
                self.eventlistener()
                self.get_time().tick(60)
                time -= 1
            else:
                self.set_environnement('score')

    def showscore(self):
        for player in self.get_player():
            player.reset_score()

        for lines in self.get_carte().get_elements():
            for element in lines:
                if element == 1:
                    self.get_player(0).augmente_score()

                if element == 2:
                    self.get_player(1).augmente_score()

        if self.get_player(0).get_score() < self.get_player(1).get_score():
            board = pygame.image.load('./img/score/1.png').convert_alpha()
        elif self.get_player(1).get_score() < self.get_player(0).get_score():
            board = pygame.image.load('./img/score/0.png').convert_alpha()
        else:
            board = pygame.image.load('./img/score/egal.png').convert_alpha()

        board = pygame.transform.scale(board, (self.get_limites('x') * self.get_scale(), self.get_limites('y') * self.get_scale()))

        self.get_surface().blit(board, [0, 0])
        pygame.display.flip()

        while self.get_environnement() == 'score' and not self.get_ending():
            self.eventlistener()
            self.get_time().tick(self.get_fps())

    """
    "
    " Verifie les entrées au clavier
    "
    """

    def eventlistener(self):
        for evenement in pygame.event.get():
            if self.get_environnement() == "menu":
                if evenement.type == pygame.QUIT:
                    if evenement.type == pygame.QUIT:
                        self.set_ending(True)
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    self.set_environnement('level')
                return

            if self.get_environnement() == "level":
                if evenement.type == pygame.QUIT:
                    if evenement.type == pygame.QUIT:
                        self.set_environnement('menu')
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_ESCAPE:
                        self.set_environnement('menu')
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    for ligne in range(2):
                        for colonne in range(3):
                            if (162 + 303 * colonne) < pygame.mouse.get_pos()[0] < (433 + 303 * colonne) \
                                    and (115 + 190 * ligne) < pygame.mouse.get_pos()[1] < (276 + 190 * ligne):
                                self.initcarte(colonne + 3 * ligne)

            if self.get_environnement() == "playing":
                if evenement.type == pygame.QUIT:
                    self.set_environnement('menu')
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_ESCAPE:
                        self.set_environnement('score')
                    if evenement.key == pygame.K_z:
                        self.get_player(0).deplacer('UP')
                    if evenement.key == pygame.K_d:
                        self.get_player(0).deplacer('RIGHT')
                    if evenement.key == pygame.K_s:
                        self.get_player(0).deplacer('DOWN')
                    if evenement.key == pygame.K_q:
                        self.get_player(0).deplacer('LEFT')
                    if evenement.key == pygame.K_UP:
                        self.get_player(1).deplacer('UP')
                    if evenement.key == pygame.K_RIGHT:
                        self.get_player(1).deplacer('RIGHT')
                    if evenement.key == pygame.K_DOWN:
                        self.get_player(1).deplacer('DOWN')
                    if evenement.key == pygame.K_LEFT:
                        self.get_player(1).deplacer('LEFT')

            if self.get_environnement() == "score":
                if evenement.type == pygame.QUIT:
                    if evenement.type == pygame.QUIT:
                        self.set_environnement('menu')
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    self.set_environnement('menu')
                return

    """
    "
    " initialisation des differents blocks
    "
    """

    def initblocks(self):
        self.add_imageblock(ImageBlock("0", False))
        self.add_imageblock(ImageBlock("1", False))
        self.add_imageblock(ImageBlock("2", False))
        self.add_imageblock(ImageBlock("3", True))
        self.add_imageblock(ImageBlock("4", True))
        self.add_imageblock(ImageBlock("5", True))
        self.add_imageblock(ImageBlock("6", True))
        self.add_imageblock(ImageBlock("7", True))
        self.add_imageblock(ImageBlock("8", True))
        self.add_imageblock(ImageBlock("9", True))
        self.add_imageblock(ImageBlock("10", True))
        self.add_imageblock(ImageBlock("11", True))
        self.add_imageblock(ImageBlock("12", True))
        self.add_imageblock(ImageBlock("13", True))
        self.add_imageblock(ImageBlock("14", True))
        self.add_imageblock(ImageBlock("15", True))
        self.add_imageblock(ImageBlock("16", True))
        self.add_imageblock(ImageBlock("17", True))

    """
    "
    " initialisation des joureurs
    "
    """

    def initplayers(self):
        self.add_player(Personnage(1, [1, 1], 2))
        self.add_player(Personnage(2, [28, 16], 2))

    def dessineplayers(self):
        self.get_player(0).set_position([1, 1])
        self.get_player(1).set_position([28, 16])
        self.get_player(0).dessine()
        self.get_player(1).dessine()

    """
    "
    " initalisations des diferents levels
    "
    """

    def initlevels(self):
        # LEVEL 1
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 7
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 8
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 14
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 3]  # 17
        ]
        )
        # LEVEL 2
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 3
            [0, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 0],  # 6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 7
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 8
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 10
            [0, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 0],  # 11
            [0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0],  # 12
            [0, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 0],  # 13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 14
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 3]  # 17
        ]
        )
        # LEVEL 3
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 12, 0, 17, 0, 13, 7, 12, 0, 9, 0, 13, 7, 7, 12, 0, 9, 0, 13, 7, 12, 0, 17, 0, 13, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 10, 11, 0, 0, 10, 11, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 10, 11, 0, 0, 10, 11, 0, 4],  # 2
            [12, 0, 4, 6, 0, 0, 4, 6, 0, 0, 0, 0, 0, 14, 8, 8, 16, 0, 0, 0, 0, 0, 4, 6, 0, 0, 4, 6, 0, 13],  # 3
            [0, 0, 4, 6, 0, 0, 4, 6, 0, 10, 5, 11, 0, 0, 0, 0, 0, 0, 10, 5, 11, 0, 4, 6, 0, 0, 4, 6, 0, 0],  # 4
            [16, 0, 4, 6, 0, 0, 4, 6, 0, 4, 3, 6, 0, 10, 8, 8, 11, 0, 4, 3, 6, 0, 4, 6, 0, 0, 4, 6, 0, 14],  # 5
            [0, 0, 4, 6, 0, 0, 4, 6, 0, 13, 7, 12, 0, 17, 0, 0, 17, 0, 13, 7, 12, 0, 4, 6, 0, 0, 4, 6, 0, 0],  # 6
            [11, 0, 4, 6, 0, 0, 13, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 0, 0, 4, 6, 0, 10],  # 7
            [6, 0, 4, 6, 0, 0, 0, 0, 0, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 11, 0, 0, 0, 0, 0, 4, 6, 0, 4],  # 8
            [6, 0, 4, 6, 0, 0, 0, 0, 0, 13, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 0, 0, 0, 0, 0, 4, 6, 0, 4],  # 9
            [12, 0, 4, 6, 0, 0, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 11, 0, 0, 4, 6, 0, 13],  # 10
            [0, 0, 4, 6, 0, 0, 4, 6, 0, 10, 5, 11, 0, 15, 0, 0, 15, 0, 10, 5, 11, 0, 4, 6, 0, 0, 4, 6, 0, 0],  # 11
            [16, 0, 4, 6, 0, 0, 4, 6, 0, 4, 3, 6, 0, 13, 8, 8, 12, 0, 4, 3, 6, 0, 4, 6, 0, 0, 4, 6, 0, 14],  # 12
            [0, 0, 4, 6, 0, 0, 4, 6, 0, 13, 7, 12, 0, 0, 0, 0, 0, 0, 13, 7, 12, 0, 4, 6, 0, 0, 4, 6, 0, 0],  # 13
            [11, 0, 4, 6, 0, 0, 4, 6, 0, 0, 0, 0, 0, 14, 8, 8, 16, 0, 0, 0, 0, 0, 4, 6, 0, 0, 4, 6, 0, 10],  # 14
            [6, 0, 13, 12, 0, 0, 13, 12, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 13, 12, 0, 0, 13, 12, 0, 4],  # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 11, 0, 15, 0, 10, 5, 11, 0, 9, 0, 10, 5, 5, 11, 0, 9, 0, 10, 5, 11, 0, 15, 0, 10, 5, 5, 3]  # 17
        ]
        )
        # LEVEL 4
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 7
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 8
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 14
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 3]  # 17
        ]
        )
        # LEVEL 5
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 12, 0, 0, 0, 13, 7, 12, 0, 0, 0, 13, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 7
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 8
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],  # 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],  # 14
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 11, 0, 0, 0, 10, 5, 11, 0, 0, 0, 10, 5, 5, 3]  # 17
        ]
        )
        # LEVEL 6
        self.add_level([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [3, 7, 7, 7, 12, 0, 13, 7, 3, 7, 12, 0, 13, 7, 3, 3, 7, 12, 0, 13, 7, 3, 7, 12, 0, 13, 7, 7, 7, 3],  # 0
            [6, 1, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 4],  # 1
            [6, 0, 10, 11, 0, 14, 16, 0, 9, 0, 14, 5, 16, 0, 4, 6, 0, 14, 5, 16, 0, 9, 0, 14, 16, 0, 10, 11, 0, 4],  # 2
            [6, 0, 13, 12, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 4, 6, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0, 13, 12, 0, 4],  # 3
            [12, 0, 0, 0, 14, 8, 11, 0, 9, 0, 10, 7, 16, 0, 13, 12, 0, 14, 7, 16, 0, 9, 0, 10, 8, 16, 0, 0, 0, 13],  # 4
            [0, 0, 15, 0, 0, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 15, 0, 0],  # 5
            [11, 0, 13, 8, 11, 0, 9, 0, 17, 0, 13, 8, 8, 11, 0, 10, 8, 11, 0, 15, 0, 17, 0, 9, 0, 10, 8, 12, 0, 10],
            # 6
            [6, 0, 0, 0, 9, 0, 17, 0, 0, 0, 0, 0, 0, 17, 0, 9, 0, 9, 0, 13, 16, 0, 0, 9, 0, 9, 0, 0, 0, 4],  # 7
            [3, 5, 11, 0, 9, 0, 0, 0, 14, 8, 8, 8, 11, 0, 0, 17, 0, 9, 0, 0, 0, 0, 14, 12, 0, 9, 0, 10, 5, 3],  # 8
            [3, 7, 12, 0, 9, 0, 10, 16, 0, 0, 0, 0, 9, 0, 15, 0, 0, 13, 8, 8, 8, 16, 0, 0, 0, 9, 0, 13, 7, 3],  # 9
            [6, 0, 0, 0, 9, 0, 9, 0, 0, 14, 11, 0, 9, 0, 9, 0, 15, 0, 0, 0, 0, 0, 0, 15, 0, 9, 0, 0, 0, 4],  # 10
            [12, 0, 10, 8, 12, 0, 9, 0, 15, 0, 17, 0, 13, 8, 12, 0, 13, 8, 8, 11, 0, 15, 0, 9, 0, 13, 8, 11, 0, 13],
            # 11
            [0, 0, 17, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 0, 0, 17, 0, 0],  # 12
            [11, 0, 0, 0, 14, 8, 12, 0, 9, 0, 14, 5, 16, 0, 10, 11, 0, 14, 5, 12, 0, 9, 0, 13, 8, 16, 0, 0, 0, 10],
            # 13
            [6, 0, 10, 11, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 4, 6, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0, 10, 11, 0, 4],  # 14
            [6, 0, 13, 12, 0, 14, 16, 0, 9, 0, 14, 7, 16, 0, 4, 6, 0, 14, 7, 16, 0, 9, 0, 14, 16, 0, 13, 12, 0, 4],
            # 15
            [6, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 2, 4],  # 16
            [3, 5, 5, 5, 11, 0, 10, 5, 3, 5, 11, 0, 10, 5, 3, 3, 5, 11, 0, 10, 5, 3, 5, 11, 0, 10, 5, 5, 5, 3]  # 17
        ]
        )

    def initcarte(self, level):
        self.get_carte().elements = copy.deepcopy(self.get_level(level))
        self.dessinecarte()
        self.set_environnement('playing')

    def dessinecarte(self):
        self.get_carte().affichecarte()
        self.dessineplayers()


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
    " Getter/Setter Attr "elements"
    "
    """

    def get_elements(self):
        return self.elements

    def set_elements(self, elements):
        self.elements = elements

    """
    "
    " Affichage de la carte
    "
    """

    def affichecarte(self):
        i = 0

        for lines in self.get_elements():
            j = 0

            for element in lines:
                world.get_imageblock(element).dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()

    """
    "
    " Return l'objet block se trouvant aux coordonnées données
    "
    """

    def quelblock(self, coordonnees):
        return world.get_imageblock(self.elements[coordonnees[1]][coordonnees[0]])

    def coloriecase(self, type, coordonnees):
        self.elements[coordonnees[1]][coordonnees[0]] = type
        world.get_imageblock(type).dessine([coordonnees[0], coordonnees[1]])


"""
"
" Class imageBlock: proprietés des blocks differents (obstacles ou pas etc)
"
"""


class ImageBlock:
    def __init__(self, nom, isObstacle):
        self.nom = nom
        self.url = './img/imageBlock/' + nom + '.png'
        self.isObstacle = isObstacle
        self.surface = pygame.image.load(self.url).convert()
        self.surface = pygame.transform.scale(self.get_surface(), (world.get_scale(), world.get_scale()))

    """
    "
    " Getter/Setter Attr "nom"
    "
    """

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    """
    "
    " Getter/Setter Attr "url"
    "
    """

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    """
    "
    " Getter/Setter Attr "obstacle"
    "
    """

    def is_obstacle(self):
        return self.isObstacle

    def set_is_obstacle(self, isobstacle):
        self.isObstacle = isobstacle

    """
    "
    " Getter/Setter Attr "surface"
    "
    """

    def get_surface(self):
        return self.surface

    def set_surface(self, surface):
        self.surface = surface

    """
    "
    " Dessine le block sur la carte par rapport aux coordonnées données
    "
    """

    def dessine(self, coordonees):
        world.get_surface().blit(self.get_surface(),
                                 [coordonees[0] * world.get_scale(), coordonees[1] * world.get_scale()])


"""
"
" Class Personnage: Personnage et leur proprietés
"
"""


class Personnage:
    def __init__(self, nom, position, pose):
        self.nom = nom
        self.url = './img/personnageBlock/' + str(nom) + '/'
        self.position = position
        self.pose = pose
        self.surface = list()
        self.penalite = 0
        self.score = 0

        for pose in ['TOP', 'RIGHT', 'DOWN', 'LEFT', 'DEAD']:
            self.add_surface(
                pygame.transform.scale(
                    pygame.image.load(self.url + pose + '.png'),
                    (world.get_scale(), world.get_scale())
                )
            )
        self.dessine()

    """
    "
    " Getter/Setter Attr "nom"
    "
    """

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    """
    "
    " Getter/Setter Attr "url"
    "
    """

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    """
    "
    " Getter/Setter Attr "position"
    "
    """

    def get_position(self, axe=None):
        if axe == 'x':
            return self.position[0]
        elif axe == 'y':
            return self.position[1]
        else:
            return self.position

    def set_position(self, position, axe=None):
        if axe == 'x':
            self.position[0] = position
        elif axe == 'y':
            self.position[1] = position
        else:
            self.position = position

    def augmente_position(self, axe, nombre=None):
        if axe == 'x':
            if nombre != None:
                self.position[0] += nombre
            else:
                self.position[0] += 1
        elif axe == 'y':
            if nombre != None:
                self.position[1] += nombre
            else:
                self.position[1] += 1

    def diminue_position(self, axe, nombre=None):
        if axe == 'x':
            if nombre != None:
                self.position[0] -= nombre
            else:
                self.position[0] -= 1
        elif axe == 'y':
            if nombre != None:
                self.position[1] -= nombre
            else:
                self.position[1] -= 1

    """
    "
    " Getter/Setter Attr "pose"
    "
    """

    def get_pose(self):
        return self.pose

    def set_pose(self, pose):
        self.pose = pose

    """
    "
    " Getter/Setter Attr "surface"
    "
    """

    def get_surface(self, id=None):
        if id != None:
            return self.surface[id]
        else:
            return self.surface

    def set_surface(self, surface):
        self.surface = surface

    def add_surface(self, surface):
        self.surface.append(surface)

    """
    "
    " Getter/Setter Attr "penalite"
    "
    """

    def get_penalite(self):
        return self.penalite

    def set_penalite(self, penalite):
        self.penalite = penalite

    """
    "
    " Getter/Setter Attr "score"
    "
    """

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def augmente_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    """
    "
    " Renvoi le type d'element (block) se trouvant a sa position
    "
    """

    def caseactuel(self):
        return world.get_carte().elements[self.get_position('y')][self.get_position('x')]

    """
    "
    " Recois la direction du eventlistener et se deplace si il peut se deplacer (verifie les obstacles, les limites de
    " la fenetre et les autres personnages)
    "
    """

    def deplacer(self, evenement):
        if self.penalite == 0:
            world.get_imageblock(self.caseactuel()).dessine([self.get_position('x'), self.get_position('y')])
            if not self.autrepersonne(evenement):
                if self.obstacle(evenement):
                    if self.nom == 1:
                        self.set_position([1, 1])
                        self.mort()
                    if self.nom == 2:
                        self.set_position([28, 16])
                        self.mort()
                else:
                    if evenement == 'UP':
                        if self.limite(evenement):
                            self.set_position(world.get_limites('y') - 1, 'y')
                        else:
                            self.diminue_position('y')
                        self.set_pose(0)
                    if evenement == 'RIGHT':
                        if self.limite(evenement):
                            self.set_position(0, 'x')
                        else:
                            self.augmente_position('x')
                        self.set_pose(1)
                    if evenement == 'DOWN':
                        if self.limite(evenement):
                            self.set_position(0, 'y')
                        else:
                            self.augmente_position('y')
                        self.set_pose(2)
                    if evenement == 'LEFT':
                        if self.limite(evenement):
                            self.set_position(world.get_limites('x') - 1, 'x')
                        else:
                            self.diminue_position('x')
                        self.set_pose(3)
                world.get_carte().coloriecase(self.nom, [self.get_position('x'), self.get_position('y')])
            self.dessine()

    """
    "
    " Verifie si il depace une limite en se deplacant dans $direction
    "
    """

    def limite(self, direction):
        if direction == 'UP':
            return self.get_position('y') == 0
        if direction == 'RIGHT':
            return self.get_position('x') == world.get_limites('x') - 1
        if direction == 'DOWN':
            return self.get_position('y') == world.get_limites('y') - 1
        if direction == 'LEFT':
            return self.get_position('x') == 0

    """
    "
    " Verifie si en se deplacant on se deplace sur un obstacle par rapport a $direction
    "
    """

    def obstacle(self, direction):
        if direction == 'UP':
            return world.get_carte().quelblock(
                [self.get_position('x'), (self.get_position('y') - 1) % world.get_limites('y')]).is_obstacle()
        if direction == 'RIGHT':
            return world.get_carte().quelblock(
                [(self.get_position('x') + 1) % world.get_limites('x'), self.get_position('y')]).is_obstacle()
        if direction == 'DOWN':
            return world.get_carte().quelblock(
                [self.get_position('x'), (self.get_position('y') + 1) % world.get_limites('y')]).is_obstacle()
        if direction == 'LEFT':
            return world.get_carte().quelblock(
                [(self.get_position('x') - 1) % world.get_limites('x'), self.get_position('y')]).is_obstacle()

    """
    "
    " Verifie si en se deplacant on se deplace sur un autre personnage par rapport a $direction
    "
    """

    def autrepersonne(self, direction):
        if direction == 'UP':
            if self.get_nom() == 1:
                return self.get_position('y') == world.get_player(1).get_position('y') + 1 \
                       and self.get_position('x') == world.get_player(1).get_position('x')
            else:
                return self.get_position('y') == world.get_player(0).get_position('y') + 1 \
                       and self.get_position('x') == world.get_player(0).get_position('x')
        if direction == 'RIGHT':
            if self.get_nom() == 1:
                return self.get_position('x') == world.get_player(1).get_position('x') - 1 \
                       and self.get_position('y') == world.get_player(1).get_position('y')
            else:
                return self.get_position('x') == world.get_player(0).get_position('x') - 1 \
                       and self.get_position('y') == world.get_player(0).get_position('y')
        if direction == 'DOWN':
            if self.get_nom() == 1:
                return self.get_position('y') == world.get_player(1).get_position('y') - 1 \
                       and self.get_position('x') == world.get_player(1).get_position('x')
            else:
                return self.get_position('y') == world.get_player(0).get_position('y') - 1 \
                       and self.get_position('x') == world.get_player(0).get_position('x')
        if direction == 'LEFT':
            if self.get_nom() == 1:
                return self.get_position('x') == world.get_player(1).get_position('x') + 1 \
                       and self.get_position('y') == world.get_player(1).get_position('y')
            else:
                return self.get_position('x') == world.get_player(0).get_position('x') + 1 \
                       and self.get_position('y') == world.get_player(0).get_position('y')

    def mort(self):
        self.penalite = 2 * world.get_fps()
        self.pose = 4

    def diminuepenalite(self):
        if self.penalite != 0:
            self.penalite -= 1
            if self.penalite == 0:
                self.pose = 2
                self.dessine()

    """
    "
    " Affiche le personnage par rapport a sa postion
    "
    """

    def dessine(self):
        world.get_surface().blit(self.get_surface()[self.pose],
                                 [self.get_position('x') * world.get_scale(),
                                  self.get_position('y') * world.get_scale()])
        pygame.display.flip()


"""
"
" Initialisation du monde
"
"""
world = World()
world.init()
