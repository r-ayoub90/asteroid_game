from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SPEED
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from CircleShape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shot_cooldown_timer):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = shot_cooldown_timer

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return  # still in cooldown, cannot shoot yet
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * 500
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = shot_velocity
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS  # reset cooldown timer