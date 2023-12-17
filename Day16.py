def day16(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()
    rows = list()

    for line in lines:
        clean_line = line.rstrip()
        row = list()
        for char in clean_line:
            row.append(char)

        rows.append(row)

    if is_part_2:
        best = 0

        # Top Row
        i = 1
        stop = len(rows[0]) - 1
        while i < stop:
            answer = calculate(rows, 0, i, "down")
            best = max(answer, best)
            i += 1

        # Bottom Row
        i = 1
        stop = len(rows[0]) - 1
        while i < stop:
            answer = calculate(rows, len(rows) - 1, i, "up")
            best = max(answer, best)
            i += 1

        # Left Column
        i = 1
        stop = len(rows) - 1
        while i < stop:
            answer = calculate(rows, i, 0, "right")
            best = max(answer, best)
            i += 1

        # Right column
        i = 1
        stop = len(rows) - 1
        while i < stop:
            answer = calculate(rows, len(rows[0]) - 1, 0, "left")
            best = max(answer, best)
            i += 1

        # Corners
        # Top Left
        best = max(best, calculate(rows, 0, 0, "right"))
        best = max(best, calculate(rows, 0, 0, "down"))

        # Top Right
        best = max(best, calculate(rows, 0, len(rows[0]) - 1, "left"))
        best = max(best, calculate(rows, 0, len(rows[0]) - 1, "down"))

        # Bottom Left
        best = max(best, calculate(rows, len(rows) - 1, 0, "right"))
        best = max(best, calculate(rows, len(rows) - 1, 0, "up"))

        # Bottom Right
        best = max(best, calculate(rows, len(rows) - 1, len(row[0]) - 1, "left"))
        best = max(best, calculate(rows, len(rows) - 1, len(row[0]) - 1, "up"))

        return best
    else:
        return calculate(rows, 0, 0, "right")


def calculate(rows, start_row, start_col, direction):
    visited = dict()
    traverse(direction, start_row, start_col, rows, visited)
    answer = 0

    # build new dictionary that doesn't consider direction
    visited_simple = dict()
    for key in visited.keys():
        parts = key.split("-")
        new_key = f"{parts[0]}-{parts[1]}"

        if new_key not in visited_simple:
            visited_simple[new_key] = True
            answer += 1

    return answer


def traverse(direction, row, col, rows, visited):
    while True:
        if row < 0 or col < 0 or row >= len(rows) or col >= len(rows[0]):
            return

        key = f"{row}-{col}-{direction}"
        if key in visited:
            return

        visited[key] = True

        cell = rows[row][col]
        if cell == ".":
            if direction == "right":
                col = col + 1
            elif direction == "left":
                col = col - 1
            elif direction == "up":
                row = row - 1
            elif direction == "down":
                row = row + 1
            else:
                raise "Invalid Direction"
        elif cell == "\\":
            if direction == "right":
                row = row + 1
                direction = "down"
            elif direction == "left":
                row = row - 1
                direction = "up"
            elif direction == "up":
                col = col - 1
                direction = "left"
            elif direction == "down":
                col = col + 1
                direction = "right"
            else:
                raise "Invalid Direction"
        elif cell == "/":
            if direction == "right":
                row = row - 1
                direction = "up"
            elif direction == "left":
                row = row + 1
                direction = "down"
            elif direction == "up":
                col = col + 1
                direction = "right"
            elif direction == "down":
                col = col - 1
                direction = "left"
            else:
                raise "Invalid Direction"
        elif cell == "-":
            if direction == "right":
                col = col + 1
            elif direction == "left":
                col = col - 1
            elif direction == "up":
                traverse("left", row, col - 1, rows, visited)
                traverse("right", row, col + 1, rows, visited)
                return
            elif direction == "down":
                traverse("left", row, col - 1, rows, visited)
                traverse("right", row, col + 1, rows, visited)
                return
            else:
                raise "Invalid Direction"
        elif cell == "|":
            if direction == "right":
                traverse("up", row - 1, col, rows, visited)
                traverse("down", row + 1, col, rows, visited)
                return
            elif direction == "left":
                traverse("up", row - 1, col, rows, visited)
                traverse("down", row + 1, col, rows, visited)
                return
            elif direction == "up":
                row = row - 1
            elif direction == "down":
                row = row + 1
            else:
                raise "Invalid Direction"
        else:
            raise "Invalid Char"

