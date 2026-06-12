import pygame

EARTH_IMG = pygame.transform.scale(
    pygame.image.load("assets/earth-planet.png").convert_alpha(),
    (40, 40)
)

JUPITER_IMG = pygame.transform.scale(
    pygame.image.load("assets/jupiter-planet.png").convert_alpha(),
    (80, 80)
)

MARS_IMG = pygame.transform.scale(
    pygame.image.load("assets/mars-planet.png").convert_alpha(),
    (30, 30)
)

MERCURY_IMG = pygame.transform.scale(
    pygame.image.load("assets/mercury-planet.png").convert_alpha(),
    (20, 20)
)

NEPTUNE_IMG = pygame.transform.scale(
    pygame.image.load("assets/neptune-planet.png").convert_alpha(),
    (55, 55)
)

URANUS_IMG = pygame.transform.scale(
    pygame.image.load("assets/uranus-planet.png").convert_alpha(),
    (55, 55)
)

VENUS_IMG = pygame.transform.scale(
    pygame.image.load("assets/venus-planet.png").convert_alpha(),
    (35, 35)
)

SUN_IMG = pygame.transform.scale(
    pygame.image.load("assets/sun.png").convert_alpha(),
    (120, 120)
)

SATURN_IMG = pygame.transform.scale(
    pygame.image.load("assets/saturn-planet.png").convert_alpha(),
    (70, 70)
)

BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load("assets/stars-at-night-sky.png").convert_alpha(),
    (1920, 1080)
)