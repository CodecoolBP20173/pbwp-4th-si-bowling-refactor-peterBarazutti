def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
            if frame < 10 and get_value(game[i]) == 10:
                result += get_value(game[i + 1])
        else:
            result += get_value(game[i])
<<<<<<< HEAD
            if frame < 10 and get_value(game[i]) == 10 and game[i].lower() == 'x':
                    result += get_value(game[i + 1])
                    if game[i + 2] == '/':
                        result += 10 - get_value(game[i + 1])
                    else:
                        result += get_value(game[i + 2])
            
        last = get_value(game[i])
=======
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i].lower() == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
>>>>>>> old-project-state
        if in_first_half:
            in_first_half = False
        elif not in_first_half:
            frame += 1
            in_first_half = True
        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
<<<<<<< HEAD
    if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
=======
    if char in [str(i) for i in range(1, 10)]:
>>>>>>> old-project-state
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
