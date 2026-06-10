# Planets

solar_system_planets = ['Earth', 'Moon', 'Venus', 'Jupiter', 'Saturn', 'Mars', 'Neptune', 'Uranus', 'Pluto', 'Sun']
exo_planets = ['Kepler-452b', 'Proxima Centauri b', 'HD 209458 b', 'WASP-12b', 'TRAPPIST-1e']

class Planet:
    def __init__(self, diameter, distance_from_sun, main_color, moons, orbital_speed):
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.main_color = main_color
        self.moons = moons
        self.orbital_speed = orbital_speed