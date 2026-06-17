# Planets

solar_system_planets = ['Earth', 'Moon', 'Venus', 'Jupiter', 'Saturn', 'Mars', 'Neptune', 'Uranus', 'Pluto', 'Sun']
exo_planets = ['Kepler-452b', 'Proxima Centauri b', 'HD 209458 b', 'WASP-12b', 'TRAPPIST-1e']

class Planet:
    def __init__(self, diameter, distance_from_sun, orbital_speed, current_x_position, current_y_position):
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.orbital_speed = orbital_speed