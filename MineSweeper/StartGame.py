import display
import random


# Fonction pour choisir sa difficulté
def difficulty():
    is_chosing = True
    display.difficulty()
    while is_chosing:
        scan = input(">>> ")
        if scan == "1":  # Facile
            is_chosing = False
            return 9, 9, 10
        elif scan == "2":  # Moyen
            is_chosing = False
            return 16, 16, 40
        elif scan == "3":  # Difficile
            is_chosing = False
            return 30, 16, 99
        elif scan == "4":  # Personnalisé
            is_chosing = False
            return custom()
        else:
            print("Relis la consigne . . . \n")


# Fonction pour le choix personalisé
def custom():
    # Choix du nombre de colonne
    is_chosing = True
    print("Entrez le nombre de colonne (max : 50) : ")
    while is_chosing:
        width = int(input(">>> "))
        if 0 < width <= 50:
            is_chosing = False

    # Choix du nombre de ligne
    is_chosing = True
    print("Entrez le nombre de ligne (max : 25) : ")
    while is_chosing:
        height = int(input(">>> "))
        if 0 < height <= 25:
            is_chosing = False

    # Choix du nombre de bombes
    is_chosing = True
    print(f"Entrez le nombre de bombes (max : {int(width * height / 5)}) : ")
    while is_chosing:
        bombs = int(input(">>> "))
        if 0 < bombs <= width * height / 5:
            is_chosing = False

    return width, height, bombs


# Fonction pour placer mes mines et mes chiffres
def set_mines(width, height, bombs):
    # Crée une grille vide remplie de zéros
    grid = [0] * (width * height)

    # Place les bombes aléatoirement
    for _ in range(bombs):
        while True:
            x, y = random.randrange(0, width), random.randrange(0, height)
            index = x + y * width

            if grid[index] == 0:
                grid[index] = -1  # Utilise -1 pour représenter les bombes
                break

    # Définit les chiffres en comptant les bombes adjacentes
    for x in range(height):
        for y in range(width):
            index = x * width + y

            if grid[index] == -1:
                continue

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < height and 0 <= y + j < width:
                        if grid[(x + i) * width + (y + j)] == -1:
                            grid[index] += 1

    # Convertit la grille en une liste de chaînes de caractères
    return [str(cell) if cell >= 0 else "X" for cell in grid]
