import turtle

class Cursor:

    def __init__(self, color : str, bgcolor : str, x : float, y : float, speed : int, angle : int):
        self.cursor = turtle.Turtle()
        self.color(color)
        self.screenColor(bgcolor)
        self.ink(False)
        self.goto(x, y)
        self.ink(True)
        self.speed(speed)
        self.turn(angle)
    
    def color(self, color : str):
        self.cursor.color(color)

    def screenColor(self, color : str):
        self.cursor.getscreen().bgcolor(color)

    def ink(self, on : bool):
        if on:
            self.cursor.pendown()
        else:
            self.cursor.penup()

    def goto(self, x : float, y : float):
        self.cursor.goto(x, y)

    def speed(self, speed : int):
        self.cursor.speed(speed)

    def turn(self, angle : int):
        if angle > 0:
            self.cursor.left(angle)
        elif angle < 0:
            self.cursor.right(-angle)

    def move(self, distance : float):
        self.cursor.forward(distance)

    def __del__(self):
        turtle.done()