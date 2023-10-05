def difficulty():
    is_chosing = True
    print("""Choisissez une difficulté :
    ---> Tape 1 pour le mode Facile
    ---> Tape 2 pour le mode Moyen
    ---> Tape 3 pour le mode Difficile
    ---> Tape 4 pour le mode Facile
    """)
    while is_chosing:
        scan = input(">>> ")
        if scan == "1":
            is_chosing = False
            return 9, 9, 10
        elif scan == "2":
            is_chosing = False
            return 16, 16, 40
        elif scan == "3":
            is_chosing = False
            return 30, 16, 99
        elif scan == "4":
            is_chosing = False
            return 9, 9, 10
        else:
            print("Relis la consigne . . . \n")


def set_map(width, height, bombs):
    import random

    map = list(width*height*"0")

    cnt = 0
    while cnt < bombs:
        x = random.randrange(0, width, 1)
        y = random.randrange(0, height, 1)
        index = x + (y * width)
        if map[index] != "X":
            map.insert(index, "X")
            cnt += 1

    return map