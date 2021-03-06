import pygame
import pytmx
import pyscroll

from map import MapManager
from player import Player


class Game:

    def __init__(self):

        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("The adventure of the hero")

        # generer un joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_w]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')
        elif pressed[pygame.KMOD_CTRL] + pressed[pygame.K_PLUS]:
            self.player.speed = self.player.speed + 1

    def update(self):
        self.map_manager.update()

    def run(self):
        
        clock = pygame.time.Clock()

        # Boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
