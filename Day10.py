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

    if is_part_2:
        # Find first empty node
        x = 0
        y = 0
        for row in rows:
            x = 0
            found = False
            for col in row:
                if col.is_empty:
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

            node = rows[command.y][command.x]
            node.flooded = True
            visited[key] = True

            add_to_fill_queue(queue, rows, command.x, command.y, "North")
            add_to_fill_queue(queue, rows, command.x, command.y, "South")
            add_to_fill_queue(queue, rows, command.x, command.y, "East")
            add_to_fill_queue(queue, rows, command.x, command.y, "West")

        flooded_count = 0
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                node = rows[i][j]
                if node.flooded:
                    flooded_count += 1

        total_count = len(rows) * len(rows[0])
        return total_count - flooded_count

    else:

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

        return max_steps





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

    old_node = rows[y][x]
    if not old_node.is_empty:
        if direction == "North" and not old_node.north_open:
            return
        elif direction == "South" and not old_node.south_open:
            return
        elif direction == "West" and not old_node.west_open:
            return
        elif direction == "East" and not old_node.east_open:
            return

    node = rows[new_y][new_x]
    if node.is_empty:
        command = Command()
        command.x = new_x
        command.y = new_y
        queue.append(command)
    else:
        connecting_pipe = False
        if direction == "North" and node.south_open:
            connecting_pipe = True
        elif direction == "South" and node.north_open:
            connecting_pipe = True
        elif direction == "West" and node.east_open:
            connecting_pipe = True
        elif direction == "East" and node.west_open:
            connecting_pipe = True

        if connecting_pipe:
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
    north_open = False
    east_open = False
    south_open = False
    west_open = False
    is_s = False
    is_empty = False
    flooded = False

    x = 0
    y = 0

