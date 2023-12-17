from collections import deque


def day10(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    x = 0
    y = 0

    rows = list()
    for line in lines:
        clean_line = line.rstrip()
        cols = list()
        for char in clean_line:
            node = Node()
            node.original = True
            node.character = char

            if char == "|":
                node.north_open = True
                node.south_open = True
            elif char == "-":
                node.east_open = True
                node.west_open = True
            elif char == "L":
                node.north_open = True
                node.east_open = True
            elif char == "J":
                node.north_open = True
                node.west_open = True
            elif char == "7":
                node.south_open = True
                node.west_open = True
            elif char == "F":
                node.south_open = True
                node.east_open = True
            elif char == "S":
                x = len(cols)
                y = len(rows)
            elif char == ".":
                node.is_empty = True

            cols.append(node)

        rows.append(cols)

    # Figure out s directions
    s_node = rows[y][x]
    s_node.north_open = can_access(rows, x, y, "North")
    s_node.south_open = can_access(rows, x, y, "South")
    s_node.east_open = can_access(rows, x, y, "East")
    s_node.west_open = can_access(rows, x, y, "West")

    max_steps = 0
    queue = deque()
    visited = dict()
    first_command = Command()
    first_command.x = x
    first_command.y = y
    first_command.steps = 0
    queue.append(first_command)

    while len(queue) > 0:
        command = queue.popleft()

        key = f"{command.y}-{command.x}"
        if key in visited:
            if visited[key] > command.steps:
                visited[key] = command.steps

                max_steps = max(max_steps, visited[key])

            continue
        else:
            visited[key] = command.steps
            node = rows[command.y][command.x]
            node.main_loop = True
            max_steps = max(max_steps, visited[key])

            if node.north_open:
                new_command = Command()
                new_command.steps = command.steps + 1
                new_command.y = command.y - 1
                new_command.x = command.x
                queue.append(new_command)

            if node.south_open:
                new_command = Command()
                new_command.steps = command.steps + 1
                new_command.y = command.y + 1
                new_command.x = command.x
                queue.append(new_command)

            if node.west_open:
                new_command = Command()
                new_command.steps = command.steps + 1
                new_command.y = command.y
                new_command.x = command.x - 1
                queue.append(new_command)

            if node.east_open:
                new_command = Command()
                new_command.steps = command.steps + 1
                new_command.y = command.y
                new_command.x = command.x + 1
                queue.append(new_command)

    if not is_part_2:
        return max_steps
    else:
        new_rows = list()
        for row in rows:
            new_row = list()

            for col in row:
                new_row.append(col)

                new_col = Node()
                new_col.is_empty = True
                new_row.append(new_col)

            new_rows.append(new_row)

            new_row = list()
            for i in range(len(row) * 2):
                col = Node()
                col.is_empty = True
                new_row.append(col)

            new_rows.append(new_row)

        i = 0
        j = 0
        width = len(new_rows[0])
        height = len(new_rows)

        for row in new_rows:
            row_string = ""
            for col in row:
                if col.original:
                    row_string += "#"
                else:
                    row_string += "."

        while i < height:
            j = 0
            while j < width:
                node = new_rows[i][j]
                if node.main_loop:
                    if node.north_open and i >= 2:
                        new_rows[i - 1][j].main_loop = True
                        new_rows[i - 2][j].main_loop = True
                    if node.south_open:
                        new_rows[i + 1][j].main_loop = True
                        new_rows[i + 2][j].main_loop = True
                    if node.west_open and j >= 2:
                        new_rows[i][j - 1].main_loop = True
                        new_rows[i][j - 2].main_loop = True
                    if node.east_open:
                        new_rows[i][j+1].main_loop = True
                        new_rows[i][j + 2].main_loop = True

                j = j + 2
            i = i + 2

        # Find first empty node
        x = 0
        y = 0
        for row in new_rows:
            x = 0
            found = False
            for col in row:
                if not col.main_loop:
                    found = True
                    break

                x += 1
            if found:
                break

            y += 1

        visited = dict()
        queue = deque()
        first_command = Command()
        first_command.x = x
        first_command.y = y
        queue.append(first_command)

        while len(queue) > 0:
            command = queue.popleft()
            key = f"{command.y}-{command.x}"
            if key in visited:
                continue

            node = new_rows[command.y][command.x]
            node.flooded = True
            visited[key] = True

            add_to_fill_queue(queue, new_rows, command.x, command.y, "North")
            add_to_fill_queue(queue, new_rows, command.x, command.y, "South")
            add_to_fill_queue(queue, new_rows, command.x, command.y, "East")
            add_to_fill_queue(queue, new_rows, command.x, command.y, "West")

        count = 0
        for i in range(len(new_rows)):
            for j in range(len(new_rows[i])):
                node = new_rows[i][j]
                if node.original and not node.main_loop and not node.flooded:
                    count += 1

        return count


def can_access(rows, x, y, direction):
    if direction == "North":
        new_y = y - 1

        if new_y >= 0:
            return rows[new_y][x].south_open
        else:
            return False
    elif direction == "South":
        new_y = y + 1

        if new_y < len(rows):
            return rows[new_y][x].north_open
        else:
            return False
    elif direction == "West":
        new_x = x - 1

        if new_x >= 0:
            return rows[y][new_x].east_open
        else:
            return False
    elif direction == "East":
        new_x = x + 1
        if new_x < len(rows[y]):
            return rows[y][new_x].west_open
        else:
            return False
    else:
        raise "Invalid Direction"


def add_to_fill_queue(queue, rows, x, y, direction):
    new_x = x
    new_y = y

    if direction == "North":
        new_y = y - 1
    elif direction == "South":
        new_y = y + 1
    elif direction == "West":
        new_x = x - 1
    elif direction == "East":
        new_x = x + 1
    else:
        raise "Invalid direction"

    if new_x < 0 or new_x >= len(rows[0]) or new_y < 0 or new_y >= len(rows):
        return

    node = rows[new_y][new_x]
    if not node.main_loop:
        command = Command()
        command.x = new_x
        command.y = new_y
        queue.append(command)


class Command:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.steps = 0


class Node:
    character = ""
    original = False
    north_open = False
    east_open = False
    south_open = False
    west_open = False
    is_s = False
    is_empty = False
    flooded = False
    main_loop = False

    x = 0
    y = 0

