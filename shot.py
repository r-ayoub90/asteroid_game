from CircleShape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

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