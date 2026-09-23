from Asteroid import Asteroid
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from Player import Player
from AsteroidField import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    (numpass, numfail) = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player.update(dt)
        # player.draw(screen)
        updatable.update(dt)
        for _drawable in drawable:
            _drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        # print(f"Updated dt value: {dt} seconds")

if __name__ == "__main__":
    main()
