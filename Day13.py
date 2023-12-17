
def day13(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    answer = 0
    rows = list()
    for line in lines:
        if len(line) <= 1:
            answer += process_rows(rows, is_part_2)
            rows = list()
            continue

        row = list()
        for char in line.rstrip():
            row.append(char)

        rows.append(row)

    if len(rows) > 0:
        answer += process_rows(rows, is_part_2)

    return answer


def process_rows(rows, is_part_2):
    # Process rows
    i = 0
    middle_row = 0
    allowed_differences = 0
    if is_part_2:
        allowed_differences = 1

    for i in range(len(rows) - 1):
        differences = 0
        for j in range(len(rows[i])):
            if rows[i][j] != rows[i + 1][j]:
                differences = differences + 1
                if differences > allowed_differences:
                    break

        if differences <= allowed_differences:
            up = i - 1
            down = i + 2

            while up >= 0 and down < len(rows):
                for col in range(len(rows[i])):
                    if rows[up][col] != rows[down][col]:
                        differences += 1
                        if differences > allowed_differences:
                            break

                if differences <= allowed_differences:
                    up = up - 1
                    down = down + 1
                else:
                    break

            if differences == allowed_differences:
                middle_row = i + 1
                break

    # Process columns
    middle_column = 0
    for i in range(len(rows[0]) - 1):
        differences = 0
        for j in range(len(rows)):
            if rows[j][i] != rows[j][i + 1]:
                differences += 1
                if differences > allowed_differences:
                    break

        if differences <= allowed_differences:
            left = i - 1
            right = i + 2

            while left >= 0 and right < len(rows[0]):
                for row in range(len(rows)):
                    if rows[row][left] != rows[row][right]:
                        differences += 1
                        if differences > allowed_differences:
                            break

                if differences <= allowed_differences:
                    left = left - 1
                    right = right + 1
                else:
                    break

            if differences == allowed_differences:
                middle_column = i + 1
                break

    return (100 * middle_row) + (1 * middle_column)







