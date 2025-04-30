class Sun:
    def __init__(self,name: str, radius: float, mass: float, temp: float, x: float, y:float):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
    def get_mass(self) -> float:
        return self.mass

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def __str__(self):
        return f"Sun: {self.name}"