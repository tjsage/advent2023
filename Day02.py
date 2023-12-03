import re


def day02(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    games = list()
    for line in lines:
        games.append(Game(line))

    answer = 0

    if not is_part_2:
        for game in games:
            valid = True

            for draw in game.draws:
                if draw.red > 12:
                    valid = False
                    break
                if draw.green > 13:
                    valid = False
                    break
                if draw.blue > 14:
                    valid = False
                    break

            if valid:
                answer += game.game_number
    else:
        for game in games:
            min_red = 0
            min_blue = 0
            min_green = 0

            for draw in game.draws:
                min_red = max(min_red, draw.red)
                min_green = max(min_green, draw.green)
                min_blue = max(min_blue, draw.blue)

            answer += min_red * min_green * min_blue

    return answer


class Game:
    def __init__(self, line):
        self.draws = list()
        self.game_number = int(re.match(r"Game (\d+):", line).group(1))

        right_part = line.split(":")[1]
        draw_parts = right_part.split(";")

        for part in draw_parts:
            self.draws.append(Draw(part))


class Draw:
    def __init__(self, data):
        self.red = 0
        self.green = 0
        self.blue = 0

        red_match = re.search(r"([0-9]+) red", data)
        if red_match:
            red_stuff = red_match.group(1)
            self.red = int(red_match.group(1))

        green_match = re.search(r"([0-9]+) green", data)
        if green_match:
            self.green = int(green_match.group(1))

        blue_match = re.search(r"([0-9]+) blue", data)
        if blue_match:
            self.blue = int(blue_match.group(1))
