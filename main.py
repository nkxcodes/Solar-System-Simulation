# Solar System Simulation
# Main.py

import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
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
            screen.blit(EARTH_IMG, (1180, 540))
            screen.blit(JUPITER_IMG, (1380, 540))
            screen.blit(MARS_IMG, (1260, 540))
            screen.blit(MERCURY_IMG, (1060, 540))
            screen.blit(NEPTUNE_IMG, (1810, 540))
            screen.blit(SATURN_IMG, (1510, 540))
            screen.blit(URANUS_IMG, (1660, 540))
            screen.blit(VENUS_IMG, (1110, 540))

            earth_rect = EARTH_IMG.get_rect(center=(960, 540))
            screen.blit(SUN_IMG, earth_rect)
            if event.type == pygame.QUIT:
                running = False;
        pygame.display.update();


if __name__ == "__main__":
    main()