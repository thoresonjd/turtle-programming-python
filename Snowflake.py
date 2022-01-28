from colorsys import hsv_to_rgb
from Cursor import Cursor

def snowflake(cursor : Cursor, size : int, order : int):   
    if order > 0:
        for t in [60, -120, 60, 0]:
            snowflake(cursor, size/3, order-1)
            cursor.turn(t)
    else:
        cursor.move(size)

def draw(cursor : Cursor, size : int, order : int):
    for i in range(6):
        snowflake(cursor, size, order)
        cursor.turn(-60)

def main():
    cursor = Cursor('red', 'black', 'classic', 2, -150, 250, 0, 0)
    cursor2 = Cursor('orange', 'black', 'classic', 2, -125, 225, 0, 0)
    cursor3 = Cursor('yellow', 'black', 'classic', 2, -100, 200, 0, 0)
    cursor4 = Cursor('green', 'black', 'classic', 2, -75, 175, 0, 0)
    cursor5 = Cursor('cyan', 'black', 'classic', 2, -50, 150, 0, 0)
    cursor6 = Cursor('blue', 'black', 'classic', 2, -25, 125, 0, 0)
    draw(cursor, 300, 3)
    draw(cursor2, 250, 3)
    draw(cursor3, 200, 3)
    draw(cursor4, 150, 3)
    draw(cursor5, 100, 3)
    draw(cursor6, 50, 3)

if __name__ == '__main__':
    main()