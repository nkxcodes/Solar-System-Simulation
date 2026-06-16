# Solar System Simulation
# Main.py

import pygame
import json

with open("data/planets.json") as file:
    planets = json.load(file)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Solar System Simulation")

from assets import EARTH_IMG, JUPITER_IMG, MARS_IMG, MERCURY_IMG, NEPTUNE_IMG, SATURN_IMG, SUN_IMG, URANUS_IMG, VENUS_IMG, BACKGROUND_IMG
from planets import Planet

def main():
    print("Welcome to the Solar System Simulation!")
    print("This is a simulation of the solar system.")
    print("- Nitesh Kumar - 2026")

    running = True

    while running:
        for event in pygame.event.get():
            screen.blit(BACKGROUND_IMG, (0, 0))
            screen.blit(MERCURY_IMG, (960, 500))
            screen.blit(VENUS_IMG, (1060, 500))
            screen.blit(EARTH_IMG, (1160, 500))
            screen.blit(MARS_IMG, (1260, 500))
            screen.blit(JUPITER_IMG, (1380, 500))
            screen.blit(SATURN_IMG, (1520, 500))
            screen.blit(URANUS_IMG, (1660, 500))
            screen.blit(NEPTUNE_IMG, (1800, 500))


        for planet in planets:
            Planet(planet["Diameter(km)"], planet["Distance_from_Sun_(million km)"], planet["Main_Color"], planet["Moons"], planet["Orbital_Speed_(km/s)"], planet["Current_X_Position"], planet["Current_Y_Position"])

            earth_rect = EARTH_IMG.get_rect(center=(860, 460))
            screen.blit(SUN_IMG, earth_rect)
            if event.type == pygame.QUIT:
                running = False;
        pygame.display.update();


if __name__ == "__main__":
    main()