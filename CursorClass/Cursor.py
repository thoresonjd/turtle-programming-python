import turtle

class Cursor:

    def __init__(self, color, bgcolor, shape : str, w : int, x : float, y : float, speed : int, angle : int):
        self.shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        self.cursor = turtle.Turtle()
        self.color(color)
        self.screenColor(bgcolor)
        self.shape(shape)
        self.ink(False)
        self.width(w)
        self.goto(x, y)
        self.ink(True)
        self.speed(speed)
        self.turn(angle)
    
    def color(self, color):
        self.cursor.color(color)

    def screenColor(self, color):
        self.cursor.getscreen().bgcolor(color)

    def shape(self, shape : str):
        if shape in self.shapes:
            self.cursor.shape(shape)

    def ink(self, on : bool):
        if on:
            self.cursor.pendown()
        else:
            self.cursor.penup()

    def width(self, width):
        self.cursor.width(width)    

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

    def on_screen(self) -> bool:
        leftBound = -self.cursor.getscreen().window_width() / 2 
        rightBound = self.cursor.getscreen().window_width() / 2 
        topBound = self.cursor.getscreen().window_height() / 2 
        bottomBound = -self.cursor.getscreen().window_height() / 2

        turtleX = self.cursor.xcor()
        turtleY = self.cursor.ycor()

        still_in = True
        if turtleX > rightBound or turtleX < leftBound:
            still_in = False
        if turtleY > topBound or turtleY < bottomBound:
            still_in = False

        return still_in

    def __del__(self):
        turtle.done()