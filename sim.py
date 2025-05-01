import turtle
from solar_system import SolarSystem
from sun import Sun
from planet import Planet

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width,height=self.height)
        self.screen.bgcolor("black")
        self.t.speed(0)


    def run(self):
        #self.solar_system.show_planets()
        for a_move in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()
        self.freeze()

    def freeze(self):
        self.exit = turtle.exitonclick()
    def get_shapes(self):
        return self.screen.getshapes()

    def add_shapes(self, icon:str):
        self.screen.addshape(icon)

def main(): # values in Earth masses

    system = SolarSystem()
    sim = Simulation(system, 1280, 720, 200000)

    files = ["sun.gif","mercury.gif", "venus.gif", "earth.gif", "mars.gif"]

    for gif in files:
        sim.add_shapes(f"resources/{gif}")

    sun = Sun("Sun", 109, 332950 * 10, 5800, 0,0, "resources/sun.gif")
    system.add_sun(sun)

    mercury = Planet("Mercury", 0.3829, 0.055, 0, 50, 0, 0, 12, "gray","resources/mercury.gif")
    venus = Planet("Venus", 0.9499, 0.815, 0, 100, 0, 0, 9, "#ddc883","resources/venus.gif")
    earth = Planet("Earth", 1, 1, 0, 200,0, 0, 6.2, "#4f91cf","resources/earth.gif")
    mars = Planet("Mars", 0.533, 0.107, 0, 400, 0, 0, 4.2, "#cf754f","resources/mars.gif")

    system.add_planet(mercury)
    system.add_planet(venus)
    system.add_planet(earth)
    system.add_planet(mars)


    sim.run()

if __name__ == "__main__":
    main()