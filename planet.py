import turtle

class Planet:
    def __init__(self,name:str, radius:float, mass:float, distance:float, x:int, y:int, vel_x:float, vel_y:float, color:str, icon:str=None):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.speed(0)

        if icon:
            self.t.shape(icon)
        else:
            self.t.shape("circle")

    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_x_vel(self):
        return self.vel_x

    def get_y_vel(self):
        return self.vel_y

    def set_x_vel(self, new_x_vel: float):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self.vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
        self.t.goto(self.x,self.y)

    def __str__(self):
        return f"Planet {self.name}, ({self.distance}, {self.vel_y})"

    def __eq__(self, other):
        return self.name == other.name
