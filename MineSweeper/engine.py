import display

def undercover(x, y, width, displayed_map, mine_map):
    index = x * width + y
    if mine_map[index] == "X" :
        display.lose()
    elif int(mine_map[index]) > 0:
        displayed_map[index] = mine_map[index]
    else

    return displayed_map