
def day03(input_file, is_part_2):
    answer = 0

    row_count = 0
    col_count = 0
    grid = list()
    file = open(input_file, 'r')
    lines = file.readlines()

    for line in lines:
        current_col_count = 0
        row_count += 1
        clean_line = line.rstrip()

        row = list()
        for char in clean_line:
            current_col_count += 1
            row.append(char)

        col_count = max(current_col_count, col_count)
        grid.append(row)

    if not is_part_2:
        for i in range(row_count):
            current_number = ""
            symbol_adjacent = False
            for j in range(col_count):
                cell = grid[i][j]

                if cell.isnumeric():
                    current_number += cell

                    has_symbol_neighbor = \
                        (is_symbol(grid, i - 1, j - 1, row_count, col_count)
                            or is_symbol(grid, i - 1, j, row_count, col_count)
                            or is_symbol(grid, i - 1, j + 1, row_count, col_count)
                            or is_symbol(grid, i, j - 1, row_count, col_count)
                            or is_symbol(grid, i, j + 1, row_count, col_count)
                            or is_symbol(grid, i + 1, j - 1, row_count, col_count)
                            or is_symbol(grid, i + 1, j, row_count, col_count)
                            or is_symbol(grid, i + 1, j + 1, row_count, col_count)
                        )

                    if has_symbol_neighbor:
                        symbol_adjacent = True

                else:
                    if len(current_number) > 0 and symbol_adjacent:
                        answer += int(current_number)

                    current_number = ""
                    symbol_adjacent = False

        if len(current_number) > 0 and symbol_adjacent:
            answer += int(current_number)
    else:
        for i in range(row_count):
            for j in range(col_count):
                answer += get_gear_ratio(grid, i, j, row_count, col_count)

    return answer


def is_symbol(grid, row, col, row_count, col_count):
    if row < 0 or col < 0:
        return False

    if row >= row_count or col >= col_count:
        return False

    cell = grid[row][col]
    if not cell.isnumeric() and cell != '.':
        return True
    else:
        return False


# get_gear_ration will return the gear ratio if the
# given cell is a valid gear. Otherwise, it will
# return 0
def get_gear_ratio(grid, row, col, row_count, col_count):
    adjacent_numbers = list()
    start_row = row - 1
    start_col = col - 1

    if grid[row][col] != "*":
        return 0

    for i in range(start_row, start_row + 3):
        last_number = 0
        for j in range(start_col, start_col + 3):
            if i < 0 or j < 0:
                continue

            if i >= row_count or j >= col_count:
                continue

            cell = grid[i][j]
            if cell.isnumeric():
                # Use this variable ot make sure we don't take the same number
                # multiple times
                number = get_number(grid, i, j, row_count, col_count)
                if number != last_number:
                    adjacent_numbers.append(number)
                    last_number = number

    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        return 0


def get_number(grid, row, col, row_count, col_count):
    i = row
    j = col

    while j >= 0:
        if not grid[i][j].isnumeric():
            break

        j = j - 1

    j = j + 1
    number = ""
    while j < col_count:
        if grid[i][j].isnumeric():
            number = number + grid[i][j]
        else:
            break

        j += 1

    if len(number) > 0:
        return int(number)
    else:
        return 0











