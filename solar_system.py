from sun import Sun
from planet import Planet

class SolarSystem:
    def __init__(self):
        self.sun: Sun = None
        self.planets: list[Planet] = []
    def add_sun(self, sun: Sun):
        self.sun = sun
    def add_planet(self, new_planet: Planet):
        self.planets.append(new_planet)
    def show_planets(self):
        for planet in self.planets:
            print(planet)
    def move_planets(self):
        pass