from colorsys import hsv_to_rgb
from random import randint
from Cursor import Cursor

def handle_off_screen(cursor : Cursor):
    cursor.ink(False)
    cursor.goto(0,0)
    cursor.ink(True)

def draw(cursor : Cursor):
    hue = 0
    while True:
        hue += 1 / 150
        cursor.color(hsv_to_rgb(hue, 1, 0.8))
        cursor.move(randint(1, 50))
        cursor.turn(randint(-180, 180))
        if not cursor.on_screen():
            handle_off_screen(cursor)

def main():
    cursor = Cursor('white', 'black', 'classic', 5, 0, 0, 0, 90)
    draw(cursor)

if __name__ == '__main__':
    main()