import display
import time
from playsound import playsound


# Fonction pour afficher les cases
def undercover(flag, x, y, width, height, displayed_map, mine_map):
    if x < 0 or x >= height or y < 0 or y >= width:
        return displayed_map
    index = x * width + y

    if flag == 2:
        displayed_map[index] = "⚑"
        return displayed_map

    if displayed_map[index] == "⚑":
        return displayed_map

    if mine_map[index] == "X":
        lose = list('0')
        return lose
    elif int(mine_map[index]) > 0:
        displayed_map[index] = mine_map[index]
    elif displayed_map[index] != " ":
        displayed_map[index] = " "

        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < height and 0 <= y + j < width:
                    undercover(flag, x + i, y + j, width, height, displayed_map, mine_map)

    return displayed_map


# Fonction pour selectionner une case
def selection(width, height, displayed_map, mine_map):
    x_selection = False
    print("\nVeuiller entrer la colonne (⮟) :")
    while not x_selection:
        x = int(input(">>> ")) - 1
        if -1 < x < width and x != '':
            x_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    y_selection = False
    print("\nVeuiller entrer la ligne (⮞) :")
    while not y_selection:
        y = int(input(">>> ")) - 1
        if -1 < y < height and y != '':
            y_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    flag_or_not = False
    print("""Quelle action souhaitez vous réaliser ?
    ---> Tape 1 pour déminer
    ---> Tape 2 pour poser un drapeau""")
    while not flag_or_not:
        flag = int(input(">>> "))
        if 0 < flag < 3:
            flag_or_not = True

    return undercover(flag, x, y, width, height, displayed_map, mine_map)


# Fonction principale qui permet de jouer (la seule qu'on doit appeler de l'extérieur)
def play(width, height, bombs, displayed_map, mine_map):
    start_time = time.time()
    win = False
    lose = False
    while not win and not lose:
        if displayed_map.count("█") == bombs:
            display.win(time.time() - start_time)
            win = True
            playsound("minesweeper-Septsept/MineSweeper/win.mp3")
            time.sleep(5)
        elif len(displayed_map) == 1:
            display.lose()
            lose = True
            playsound("minesweeper-Septsept/MineSweeper/sound.mp3")
            time.sleep(5)
        else:
            display.display_map(displayed_map, width)
            print(f"Bombes restantes : {bombs - displayed_map.count('⚑')}")
            print(f"Temps : {(time.time() - start_time):.2f} secondes")
            displayed_map = selection(width, height, displayed_map, mine_map)
