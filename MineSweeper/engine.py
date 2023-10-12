import display


def undercover(x, y, width, height, displayed_map, mine_map):
    if x < 0 or x >= height or y < 0 or y >= width:
        return displayed_map
    index = x * width + y

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
                    undercover(x + i, y + j, width, height, displayed_map, mine_map)

    return displayed_map


def selection(width, height, displayed_map, mine_map):
    x_selection = False
    print("\nVeuiller entrer la position de x (⮟) :")
    while not x_selection:
        x = int(input(">>> ")) - 1
        if -1 < x < width and x != '':
            x_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    y_selection = False
    print("\nVeuiller entrer la position de y (⮞) :")
    while not y_selection:
        y = int(input(">>> ")) - 1
        if -1 < y < height and y != '':
            y_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    return undercover(x, y, width, height, displayed_map, mine_map)


def play(width, height, bombs, displayed_map, mine_map):
    win = False
    lose = False
    while not win and not lose:
        if displayed_map.count("█") == bombs:
            display.win()
            win = True
        elif len(displayed_map) == 1:
            display.lose()
            lose = True
        else:
            display.display_map(displayed_map, width)
            displayed_map = selection(width, height, displayed_map, mine_map)
