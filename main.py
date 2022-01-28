from colorsys import hsv_to_rgb
from Cursor import Cursor
import math

def draw(cursor : Cursor):
    hue = 0
    distance = 1
    while cursor.on_screen():
        hue += 1 / 150
        cursor.color(hsv_to_rgb(hue, 1, 0.8))
        cursor.move(20)
        cursor.turn(math.sqrt(distance*20))
        distance += 1
        distance %= 150

def main():
    cursor = Cursor('white', 'black', 'classic', 2, 0, 0, 0, 144)
    draw(cursor)

if __name__ == '__main__':
    main()