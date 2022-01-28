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
    draw(cursor, 300, 3)

    # cursors = [
    #     Cursor('red', 'black', 'classic', 2, -150, 250, 0, 0),
    #     Cursor('orange', 'black', 'classic', 2, -125, 225, 0, 0),
    #     Cursor('yellow', 'black', 'classic', 2, -100, 200, 0, 0),
    #     Cursor('green', 'black', 'classic', 2, -75, 175, 0, 0),
    #     Cursor('cyan', 'black', 'classic', 2, -50, 150, 0, 0),
    #     Cursor('blue', 'black', 'classic', 2, -25, 125, 0, 0)
    # ]
    # size = 300
    # order = 3
    # for i in range(len(cursors)):
    #     draw(cursors[i], size, order)
    #     size -= 50

if __name__ == '__main__':
    main()