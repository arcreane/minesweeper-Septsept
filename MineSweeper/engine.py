import display

def undercover(x, y, width, displayed_map, mine_map):
    index = x * width + y
    if mine_map[index] == "X" :
        display.lose()
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