import re


def day08(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    first_line = lines[0].rstrip()
    instruction_list = list()
    for char in first_line:
        instruction_list.append(char)

    left_map = dict()
    right_map = dict()
    map_lines = lines[2:]
    for line in map_lines:
        match = re.match(r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", line)
        source = match.group(1)
        left = match.group(2)
        right = match.group(3)

        left_map[source] = left
        right_map[source] = right

    if is_part_2:
        steps = 0
        index = 0
        ghosts = list()
        for key in left_map:
            if key.endswith("A"):
                ghost = Ghost()
                ghost.current = key
                ghosts.append(ghost)

        while True:
            steps_moved = 0
            instruction = instruction_list[index]
            z_count = 0
            for ghost in ghosts:
                if ghost.done:
                    z_count += 1
                    continue
                current_location = ""
                if instruction == "L":
                    current_location = left_map[ghost.current]
                elif instruction == "R":
                    current_location = right_map[ghost.current]
                else:
                    raise f"Oh no, invalid instruction {instruction}"

                ghost.total_steps += 1
                ghost.steps_to_current_z += 1
                ghost.current = current_location

                if ghost.current.endswith("Z"):
                    if ghost.steps_to_current_z == ghost.steps_to_last_z:
                        ghost.done = True
                        z_count += 1
                    else:
                        ghost.steps_to_last_z = ghost.steps_to_current_z
                        ghost.steps_to_current_z = 0
                        z_count += 1

            steps += 1
            if z_count == len(ghosts):
                break

            index = (index + 1) % len(instruction_list)

        number = 1
        for ghost in ghosts:
            number = lcm(number, ghost.steps_to_current_z)

        return number

    else:
        steps = 0
        index = 0
        current_location = "AAA"
        while True:
            steps += 1
            instruction = instruction_list[index]
            if instruction == "L":
                current_location = left_map[current_location]
            elif instruction == "R":
                current_location = right_map[current_location]
            else:
                raise f"Oh no, invalid instruction {instruction}"

            if current_location == "ZZZ":
                break

            index = (index + 1) % len(instruction_list)

        return steps


class Ghost:
    def __init__(self):
        self.current = ""
        self.last_z = ""
        self.steps_to_last_z = 0
        self.steps_to_current_z = 0
        self.total_steps = 0
        self.done = False


def lcm(x, y):
    return (x * y) // gcd(x, y)


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x
