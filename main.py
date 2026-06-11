# Solar System Simulation
# Main.py

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar System Simulation")

def main():
    print("Welcome to the Solar System Simulation!")
    print("This is a simulation of the solar system.")
    print("- Nitesh Kumar - 2026")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
        pygame.display.update();


if __name__ == "__main__":
    main()