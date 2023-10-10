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


def set_mines(width, height, bombs):
    import random

    res = list(width*height*"0")

    cnt = 0
    while cnt < bombs:
        x = random.randrange(0, width, 1)
        y = random.randrange(0, height, 1)
        index = x + (y * width)
        if res[index] != "X":
            # Placement de la bombe
            res[index] = "X"

            # Placement des chiffres au dessus et en dessous
            if index > width and res[index - width] != "X":
                res[index - width] = str(int(res[index - width]) + 1)
            if index < width * height - width and res[index + width] != "X":
                res[index + width] = str(int(res[index + width]) + 1)

            # Placement des chiffres à gauche
            if index % width != 0:
                if res[index - 1] != "X":
                    res[index - 1] = str(int(res[index - 1]) + 1)
                if index > width and res[index - width - 1] != "X":
                    res[index - width - 1] = str(int(res[index - width - 1]) + 1)
                if index < width * height - width and res[index + width - 1] != "X":
                    res[index + width - 1] = str(int(res[index + width - 1]) + 1)

            # Placement des chiffres à droite
            if (index + 1) % width != 0:
                if res[index + 1] != "X":
                    res[index + 1] = str(int(res[index + 1]) + 1)
                if index > width and res[index - width + 1] != "X":
                    res[index - width + 1] = str(int(res[index - width + 1]) + 1)
                if index < width * height - width and res[index + width + 1] != "X":
                    res[index + width + 1] = str(int(res[index + width + 1]) + 1)

            cnt += 1
    return res

