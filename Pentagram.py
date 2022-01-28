from Cursor import Cursor

def pentagram(cursor : Cursor, distance : float):
    if distance < 25: return
    for i in range(5):
        cursor.move(distance)
        pentagram(cursor, distance / 2)
        cursor.turn(144)

def main():
    cursor = Cursor('red', 'black', 1, 100, 0, 0, 144)
    pentagram(cursor, 200)

if __name__ == '__main__':
    main()