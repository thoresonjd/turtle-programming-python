# from colorsys import hsv_to_rgb
from Cursor import Cursor

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta']

def draw(cursor : Cursor):
    distance = 1
    color = 0
    while cursor.on_screen():
        cursor.color(colors[color%len(colors)])
        cursor.move(distance)
        cursor.turn(60.5)
        distance += 1
        color += 1

# def draw(cursor : Cursor):
#     hue = 0
#     distance = 1
#     while cursor.on_screen():
#         hue += 1 / 150
#         cursor.color(hsv_to_rgb(hue, 1, 0.8))
#         cursor.move(distance)
#         cursor.turn(70)
#         distance += 1

def main():
    cursor = Cursor('white', 'black', 'turtle', 3, 0, 0, 0, 144)
    draw(cursor)

if __name__ == '__main__':
    main()