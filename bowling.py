def score(game):
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        result = newmethod749(game, i, frame, result, last)
        last = get_value(game[i])
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
    return result

def newmethod749(game, i, frame, result, last):
    if game[i] == '/':
        result += 10 - last
    else:
        result += get_value(game[i])
    if frame < 10 and get_value(game[i]) == 10:
        if game[i] == '/':
            result += get_value(game[i + 1])
        elif game[i].lower() == 'x':
            result += get_value(game[i + 1])
            if game[i + 2] == '/':
                result += 10 - get_value(game[i + 1])
            else:
                result += get_value(game[i + 2])
    return result


def get_value(char):
    if char in [str(i) for i in range(1, 10)]:
        return int(char)
    elif char.lower() == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
