from collections import  deque


def day17(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    rows = list()

    for line in lines:
        clean_line = line.rstrip()
        row = list()
        for char in clean_line:
            row.append(char)

        rows.append(row)

    min_heat_lost = 99999999999999999
    start_command = Command()
    start_command.row = 0
    start_command.col = 0
    start_command.heat_loss = 0
    start_command.direction = "south"

    visited = dict()
    queue = deque()
    queue.append(start_command)

    while len(queue) > 0:
        command = queue.popleft()
        key = f"{command.row}-{command.col}-{command.steps_forward}-{command.direction}"
        if key in visited:
            if command.heat_loss < visited[key]:
                visited[key] = command.heat_loss
            else:
                continue

        else:
            visited[key] = command.heat_loss

        if command.heat_loss > min_heat_lost:
            continue

        if command.row == len(rows) - 1 and command.col == len(rows[0]) - 1:
            if is_part_2 and command.steps_forward < 4:
                continue

            min_heat_lost = min(min_heat_lost, command.heat_loss)
            continue

        get_next_command(is_part_2, rows, queue, command, "forward")
        get_next_command(is_part_2, rows, queue, command, "left")
        get_next_command(is_part_2, rows, queue, command, "right")

    return min_heat_lost


def get_next_command(is_part_2, rows, queue, current_command, goal_direction):
    if is_part_2:
        if goal_direction == "forward" and current_command.steps_forward >= 10:
            return

        if goal_direction != "forward" and 0 < current_command.steps_forward < 4:
            return

    else:
        if goal_direction == "forward" and current_command.steps_forward >= 3:
            return

    next_command = Command()

    row_move = 0
    col_move = 0
    new_direction = current_command.direction
    steps_forward = 0

    if goal_direction == "forward":
        if current_command.direction == "south":
            row_move += 1
        elif current_command.direction == "north":
            row_move -= 1
        elif current_command.direction == "east":
            col_move += 1
        elif current_command.direction == "west":
            col_move -= 1
        else:
            raise "Invalid direction"

        steps_forward = current_command.steps_forward + 1

    elif goal_direction == "left":
        if current_command.direction == "south":
            new_direction = "east"
            col_move += 1
        elif current_command.direction == "north":
            new_direction = "west"
            col_move -= 1
        elif current_command.direction == "east":
            new_direction = "north"
            row_move -= 1
        elif current_command.direction == "west":
            new_direction = "south"
            row_move += 1
        else:
            raise "Invalid Direction"

        steps_forward = 1
    elif goal_direction == "right":
        if current_command.direction == "south":
            new_direction = "west"
            col_move -= 1
        elif current_command.direction == "north":
            new_direction = "east"
            col_move += 1
        elif current_command.direction == "east":
            new_direction = "south"
            row_move += 1
        elif current_command.direction == "west":
            new_direction = "north"
            row_move -= 1

        steps_forward = 1
    else:
        raise "Invalid move"

    next_command.row = current_command.row + row_move
    next_command.col = current_command.col + col_move
    next_command.direction = new_direction
    next_command.steps_forward = steps_forward

    # Check for out of bounds
    if next_command.row < 0 or next_command.col < 0 or next_command.row >= len(rows) or next_command.col >= len(rows[0]):
        return

    new_heat_loss = int(rows[next_command.row][next_command.col])
    next_command.heat_loss = new_heat_loss + current_command.heat_loss

    queue.append(next_command)


class Command:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.heat_loss = 0
        self.steps_forward = 0
        self.direction = "south"

