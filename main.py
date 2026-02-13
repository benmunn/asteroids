import pygame
from logger import log_state
from constants import *
import player




def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player_1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        dt = clock.tick(60)/1000
        player_1.update(dt)
        player_1.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()
