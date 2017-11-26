def score(game):
    result = 0
    num_of_pins = 10
    frame = 1
    max_frame = 10
    previous_round_score = 0
    in_first_half = True
    for i in range(len(game)):
        result = calc_result(game, i, frame, result, previous_round_score, max_frame, num_of_pins)
        previous_round_score = get_value(game[i])
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
    return result


def calc_result(game, i, frame, result, previous_round_score, max_frame, num_of_pins):
    if game[i] == '/':
        result += num_of_pins - previous_round_score
        if frame < max_frame:
            result += get_value(game[i + 1])
    else:
        result += get_value(game[i])
    if game[i].lower() == 'x':
        if frame < max_frame:
            result += get_value(game[i + 1])
            if game[i + 2] == '/':
                result += num_of_pins - get_value(game[i + 1])
            else:
                result += get_value(game[i + 2])
    return result


def get_value(char):
    if char in [str(i) for i in range(1, 10)]:
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
