import numpy as np
from scipy.integrate import ode
import pygame
import random

class ball(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.Surface((11, 11), pygame.SRCALPHA)
        self.image.fill("red")

        self.rect = self.image.get_rect(center=pos)

        self.state = np.append(np.array(pos), np.zeros(2))
        self.g = 9.8
        self.gamma = 0.01
        self.m = 45

        self.t = 0

        self.line = np.array(pos)

        self.solv = ode(self.f)
        self.solv.set_integrator("dop853")
        self.solv.set_f_params(self.gamma, self.g, self.m)
        self.solv.set_initial_value(self.state, self.t)

    def f(self, t, y, gamma, g, m):
        px, py, vx, vy = y
        return [vx, vy, -gamma * vx, (-gamma * vy) + g * m]

    def update(self, dt):
        self.t += dt

        self.state = self.solv.integrate(self.t)
        
        self.line = np.append(self.line, self.state[0:2])

        self.rect.center = self.state[0:2]

    def ballcol(self, ob):
        v1 = np.linalg.norm(self.state[2:])
        v2 = np.linalg.norm(ob.state[2:])
        vd = v1 - v2

        point = np.array(ob.state[0:2])
        pos = np.array(self.rect.center)
        pdiff = pos - point

        dist = np.linalg.norm(pos - point)
        u = (pos - point) / dist

        self.state[2:] = (v1 - ((np.dot(vd, pdiff) / np.square(dist)) * (pdiff))) * u * 0.95
        self.solv.set_initial_value(self.state, self.t)

    def col(self, pos):
        pos = np.array(pos)
        point = np.array(self.rect.center)

        dist = np.linalg.norm(pos - point)

        v = np.linalg.norm(self.state[2:])

        u = -(pos - point) / dist

        

        self.state[2:] = u * np.linalg.norm(self.state[2:]) * 0.95
        self.solv.set_initial_value(self.state, self.t)
        
