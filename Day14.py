import time


def day14(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    rows = list()
    row_num = 0
    for line in lines:
        clean_line = line.rstrip()

        row = list()
        col_num = 0
        for char in clean_line:
            row.append(char)

            col_num += 1

        rows.append(row)
        row_num += 1

    if is_part_2:
        original = copy_rows(rows)
        cycle = 0
        difference = 0
        target = 1000000000
        visited = dict()

        while cycle < target:
            cycle = cycle + 1

            rotate(rows, "North")
            rotate(rows, "West")
            rotate(rows, "South")
            rotate(rows, "East")

            key = stringify(rows)
            if key in visited:
                last_index = visited[key]
                difference = cycle - last_index
                break
            else:
                visited[key] = cycle

        can_increment = int((target - cycle) / difference) * difference
        cycle = cycle + can_increment

        leftover_cycles = target - cycle

        for i in range(leftover_cycles):
            rotate(rows, "North")
            rotate(rows, "West")
            rotate(rows, "South")
            rotate(rows, "East")

    else:
        # Slide rocks up
        for i in range(len(rows[0])):
            last_rock = -1
            for j in range(len(rows)):
                node = rows[j][i]
                if node.char == "#":
                    last_rock = j
                elif node.char == "O":
                    node.row = last_rock + 1
                    last_rock = last_rock + 1

    #Calculate Load
    answer = 0
    height = len(rows)
    row_num = 0
    for row in rows:
        col_num = 0
        for node in row:
            if node == "O":
                answer += (height - row_num)
            col_num += 1
        row_num += 1

    return answer


def stringify(rows):
    all_cols = list()

    for row in rows:
        for col in row:
            all_cols.append(col)

    return "".join(all_cols)

def load(rows):
    answer = 0
    height = len(rows)
    row_num = 0
    for row in rows:
        col_num = 0
        for node in row:
            if node == "O":
                answer += (height - row_num)
            col_num += 1
        row_num += 1

    return answer

def rotate(rows, direction):
    if direction == "North":
        for i in range(len(rows[0])):
            last_rock = -1
            for j in range(len(rows)):
                node = rows[j][i]
                if node == "#":
                    last_rock = j
                elif node == "O":
                    if last_rock + 1 == j:
                        last_rock = last_rock + 1
                    else:
                        rows[last_rock + 1][i] = "O"
                        rows[j][i] = "."

                        last_rock = last_rock + 1
    elif direction == "South":
        for i in range(len(rows[0])):
            last_rock = len(rows)
            j = len(rows) - 1
            while j >= 0:
                node = rows[j][i]
                if node == "#":
                    last_rock = j
                elif node == "O":
                    if last_rock - 1 == j:
                        last_rock = last_rock - 1
                    else:
                        rows[last_rock - 1][i] = "O"
                        rows[j][i] = "."

                        last_rock = last_rock - 1

                j = j - 1
    elif direction == "East":
        for i in range(len(rows)):
            last_rock = len(rows[i])
            j = len(rows[i]) - 1
            while j >= 0:
                node = rows[i][j]
                if node == "#":
                    last_rock = j
                elif node == "O":
                    if last_rock - 1 == j:
                        last_rock = last_rock - 1
                    else:
                        rows[i][last_rock - 1] = "O"
                        rows[i][j] = "."

                        last_rock = last_rock - 1

                j = j - 1

    elif direction == "West":
        for i in range(len(rows)):
            last_rock = -1
            for j in range(len(rows[i])):
                node = rows[i][j]
                if node == "#":
                    last_rock = j
                elif node == "O":
                    if last_rock + 1 == j:
                        last_rock = last_rock + 1
                    else:
                        rows[i][last_rock + 1] = "O"
                        rows[i][j] = "."

                        last_rock = last_rock + 1
    else:
        raise "Invalid Direction"


def copy_rows(rows):
    new_rows = list()
    for row in rows:
        new_row = list()
        for col in row:
            new_row.append(col)

        new_rows.append(new_row)
    return new_rows


def compare(r1, r2):
    width = len(r1[0])
    height = len(r1)

    match = True
    for i in range(height):
        for j in range(width):
            if r1[i][j] != r2[i][j]:
                match = False
                break

    return match


class Node:
    def __init__(self):
        self.col = 0
        self.row = 0
        self.char = "#"

        self.new_row = 0

