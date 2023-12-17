
def day11(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()
    nodes = list()

    if is_part_2:
        row = 0
        for line in lines:
            col = 0
            for char in line.rstrip():
                if char == "#":
                    node = Node()
                    node.row = row
                    node.col = col
                    nodes.append(node)

                col += 1
            row += 1

        increment_amount = 999999
        row = 0
        for line in lines:
            has_galaxies = False
            for char in line:
                if char == "#":
                    has_galaxies = True
                    break

            if not has_galaxies:
                for node in nodes:
                    if node.row > row:
                        node.row_add += increment_amount

            row += 1

        width = len(lines[0]) - 1
        height = len(lines)

        for i in range(width):
            has_galaxies = False
            for j in range(height):
                if lines[j][i] == "#":
                    has_galaxies = True
                    break

            if not has_galaxies:
                for node in nodes:
                    if node.col >= i:
                        node.col_add += increment_amount

        for node in nodes:
            node.row += node.row_add
            node.col += node.col_add

        answer = 0
        node_count = len(nodes)
        for i in range(node_count):
            for j in range(i, node_count):
                width_change = abs(nodes[i].col - nodes[j].col)
                height_change = abs(nodes[i].row - nodes[j].row)
                answer += width_change + height_change

        return answer

    else:

        new_lines = list()

        width = len(lines[0]) - 1
        for line in lines:
            has_galaxies = False
            for char in line:
                if char == "#":
                    has_galaxies = True

            if not has_galaxies:
                new_line = list()
                for char in line.rstrip():
                    new_line.append(".")

                new_lines.append(new_line)

            new_line = list()
            for char in line.rstrip():
                new_line.append(char)
            new_lines.append(new_line)

        height = len(new_lines)

        row = 0
        col = 0
        while col < width:
            has_galaxies = False
            row = 0
            while row < height:
                if new_lines[row][col] == "#":
                    has_galaxies = True
                    break
                row += 1

            if not has_galaxies:
                row = 0
                for line in new_lines:
                    new_lines[row] = line[0:col] + ["."] + line[col:]
                    row += 1
                col += 1
                width += 1

            col += 1

        for line in new_lines:
            col = 0
            for char in line:
                if char == "#":
                    node = Node()
                    node.row = row
                    node.col = col
                    nodes.append(node)

                col += 1
            row += 1

        for line in new_lines:
            row_string = ""
            for char in line:
                row_string += str(char)

        # Calculate distances for each pair
        answer = 0
        node_count = len(nodes)
        for i in range(node_count):
            for j in range(i + 1, node_count):
                width_change = abs(nodes[i].col - nodes[j].col)
                height_change = abs(nodes[i].row - nodes[j].row)
                answer += width_change + height_change

        return answer


class Node:
    def __init__(self):
        self.row = 0
        self.col = 0

        self.row_add = 0
        self.col_add = 0

