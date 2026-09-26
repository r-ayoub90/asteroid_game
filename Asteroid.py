import random

from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame

class Asteroid(CircleShape):
    containers: pygame.sprite.Group

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> list["Asteroid"]:
        self.kill()  # remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []  # cannot split further
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid_movement_1 = self.velocity.rotate(random_angle)
            asteroid_movement_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid_movement_1
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = asteroid_movement_2
            