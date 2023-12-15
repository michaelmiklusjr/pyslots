
from machine import Machine
from settings import *
import pygame, sys


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('PySlots')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(bg_image_path)
        self.grid_image = pygame.image.load(grid_image_path).convert_alpha()
        self.machine = Machine()
        self.delta_time = 0

        # sound
        main_sound = pygame.mixer.Sound('PySlots Michael Miklus II CIS 189 16025/audio/pyslots_main_theme.mp3')
        main_sound.play(loops=-1)

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image, (0, 0))
            self.clock.tick(fps)


if __name__ == '__main__':
    game = Game()
    game.run()
