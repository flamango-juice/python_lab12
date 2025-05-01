import turtle


class Sun:
    def __init__(self,name: str, radius: float, mass: float, temp: float, x: int, y:int):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y

        self.t = turtle.Turtle()
        self.t.color("#ffbf00")
        self.t.shape("circle")
        self.t.goto(self.x, self.y)
        self.t.speed(0)


    def get_mass(self) -> float:
        return self.mass

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def __str__(self):
        return f"Name: {self.name}, Mass: {self.mass}, ({self.x}, {self.y}), Temp :{self.temp}"

if __name__ == "__main__":
    sun = Sun("Helios", 1000, 1000, 1000, 1000, 1000)
    print(sun)