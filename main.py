import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updateables.update(dt)
        for sprite in drawables:
            sprite.draw(screen)

        print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
        dt = clock.tick(60)/1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
