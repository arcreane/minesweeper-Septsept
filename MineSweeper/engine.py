import display


def undercover(x, y, width, displayed_map, mine_map):
    x -= 1
    y -= 1
    index = x * width + y
    if mine_map[index] == "X":
        display.lose()
        return 0
    elif int(mine_map[index]) > 0:
        displayed_map[index] = mine_map[index]
    else:
        cnt = -1
        while cnt < 2:
            undercover(x - 1, y + cnt, width, displayed_map, mine_map)
            undercover(x + 1, y + cnt, width, displayed_map, mine_map)
            cnt += 1
        undercover(x, y - 1, width, displayed_map, mine_map)
        undercover(x, y + 1, width, displayed_map, mine_map)
    return displayed_map


def selection(width, height, displayed_map, mine_map):
    x_selection = False
    print("\nVeuiller entrer la position de x (⮟) :")
    while not x_selection:
        x = int(input(">>> "))
        if 0 < x < width:
            x_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    y_selection = False
    print("\nVeuiller entrer la position de y (⮞) :")
    while not y_selection:
        y = int(input(">>> "))
        if 0 < y < height:
            y_selection = True
        else:
            print("Erreur, veuillez réessayer.")

    return undercover(x, y, width, displayed_map, mine_map)

def counter(str):
    cnt = 0
    res = 0
    while cnt < len(str):
        if(str[cnt] == "█"):
            res += 1
        cnt += 1
    return res

def play(width, height, bombs, displayed_map, mine_map):
    win = False
    while not win:
        if counter(displayed_map) == bombs:
            win = True
        else:
            display.display_map(displayed_map, width)
            displayed_map = selection(width, height, displayed_map, mine_map)