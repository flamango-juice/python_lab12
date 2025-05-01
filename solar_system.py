from sun import Sun
from planet import Planet
from math import sqrt
from uni_gravity import UniversalGravity

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
        dt = 1 # Constant time interval for each solar system iteration.

        for planet in self.planets:
            # Move the distance covered in the interval dt
            planet.move_to(
                planet.get_x() + dt * planet.get_x_vel(),
                planet.get_y() + dt * planet.get_y_vel())

            # After move we need to calculate the new distance from the sun using the distance formula.
            dist_x = self.sun.get_x() - planet.get_x()
            dist_y = self.sun.get_y() - planet.get_y()
            new_distance = sqrt(dist_x**2 + dist_y**2)

            # Let's calculate our new acceleration so we can set our new velocity
            acc_x = UniversalGravity.G * self.sun.get_mass()*dist_x/new_distance ** 3
            acc_y = UniversalGravity.G * self.sun.get_mass()*dist_y/new_distance ** 3

            # Now let's calculate the new x and y velocities and update them for the planet
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)