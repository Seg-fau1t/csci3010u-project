import numpy as np
from scipy.integrate import ode
import pygame

class peg(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.image.fill("pink")

        self.rect = self.image.get_rect(center=pos)

