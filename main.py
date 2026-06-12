# Solar System Simulation
# Main.py

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar System Simulation")

from assets import EARTH_IMG, JUPITER_IMG, MARS_IMG, MERCURY_IMG, NEPTUNE_IMG, SATURN_IMG, SUN_IMG, URANUS_IMG, VENUS_IMG, BACKGROUND_IMG

def main():
    print("Welcome to the Solar System Simulation!")
    print("This is a simulation of the solar system.")
    print("- Nitesh Kumar - 2026")

    running = True

    while running:
        for event in pygame.event.get():
            screen.blit(BACKGROUND_IMG, (0, 0))
            screen.blit(EARTH_IMG, (50, 150))
            screen.blit(JUPITER_IMG, (200, 150))
            screen.blit(MARS_IMG, (350, 150))
            screen.blit(MERCURY_IMG, (500, 150))
            screen.blit(NEPTUNE_IMG, (650, 150))
            screen.blit(SATURN_IMG, (800, 150))
            screen.blit(URANUS_IMG, (950, 150))
            screen.blit(VENUS_IMG, (50, 350))

            earth_rect = EARTH_IMG.get_rect(center=(640, 320))
            screen.blit(SUN_IMG, earth_rect)
            if event.type == pygame.QUIT:
                running = False;
        pygame.display.update();


if __name__ == "__main__":
    main()