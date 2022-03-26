from p2.deep_blue_fish.util.config import *
import pygame
import sys


class UIMenu:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((WIN_WIDTH * WIN_SCALE, WIN_HEIGHT * WIN_SCALE))
        # Running
        self.running = True
        # Click
        self.left_click = False

    # Call other functions
    def __call__(self):
        while self.running:
            self.while_loop()
            self.event_loop()
            self.update()

    def while_loop(self):
        pass

    def event_loop(self):
        # Event For Loop
        for event in pygame.event.get():
            # X PROGRAM
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # KEYBOARD PRESSES
            if event.type == pygame.KEYDOWN:
                # Escape Key
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            # MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.left_click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.left_click = False

    def update(self):
        pygame.display.update()
        self.CLOCK.tick(FPS)