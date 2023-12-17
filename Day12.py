
def day12(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()
    nodes = list()


    for line in lines:
        node = Node()

        clean_line = line.rstrip()
        parts = clean_line.split(" ")
        node.line = parts[0]

        raw_num_list = parts[1].split(",")
        for raw_num in raw_num_list:
            node.options.append(int(raw_num))

        nodes.append(node)

    answer = 0

    if is_part_2:
        for node in nodes:
            new_line = ""
            new_list = list()
            for i in range(5):
                new_line = new_line + node.line
                if i < 4:
                    new_line = new_line + "?"
                for num in node.options:
                    new_list.append(num)

            node.line = new_line
            node.options = new_list

    for node in nodes:
        tree = Tree()
        leaves = list()
        build_tree(node.line, tree, leaves, 0)

        index = len(node.options) - 1
        good_count = 0
        for leaf in leaves:
            is_good = True

            current = leaf

            while current:
                if current.char == "#":
                    if index < 0:
                        is_good = False
                        break
                    target_count = node.options[index]
                    while target_count > 0:
                        if current != "#":
                            is_good = False
                            break

                        target_count = target_count - 1
                        current = leaf.parent

                    if not is_good:
                        break

                    current = leaf.parent
                    if current != ".":
                        break
                    else:
                        index = index - 1

                current = current.parent
            if is_good:
                good_count += 1

        answer += good_count

    return answer


def calculate(node, prefix, index):
    start_pos = len(prefix)

    num_moves = 0
    good_springs = 0

    if index > 0 and index < len(node.options):
        good_springs = 1

    while True:
        next_input = prefix + ("." * good_springs)

        if index < len(node.options):
            next_input = next_input + ("#" * node.options[index])
        else:
            diff = len(node.line) - len(next_input)
            if diff < 0:
                break

            next_input = next_input + ("." * diff)
            num_moves += compare(node.line, next_input)
            break

        if len(next_input) > len(node.line):
            break
        else:
            check_index = start_pos
            while check_index < len(next_input):
                char = next_input[check_index]
                expected = node.line[check_index]
                if expected == "?" or expected == char:
                    check_index += 1
                    continue

                break

            num_moves += calculate(node, next_input, index + 1)

        good_springs += 1

    return num_moves


def compare(expected, actual):
    if len(expected) != len(actual):
        return 0

    for i in range(len(expected)):
        expected_char = expected[i]
        actual_char = actual[i]

        if expected_char == "?":
            continue
        elif expected_char != actual_char:
            return 0

    return 1

def build_tree(input_string, parent, leaves, level):
    if level >= len(input_string):
        leaves.append(parent)
        return

    char = input_string[level]

    if char == '#' or char == "?":
        tree = Tree()
        tree.char = '#'
        parent.left = tree
        build_tree(input_string, tree, leaves, level + 1)
    if char == "." or char == "?":
        tree = Tree()
        tree.char = '.'
        parent.right = tree
        build_tree(input_string, tree, leaves, level + 1)

    if char != "." and char != "?" and char != "#":
        raise f"Invalid Char {char}"


def calculate_tree(tree, node, index):
    answer = 0

    if tree.char == "":
        if tree.left:
            answer += calculate_tree(tree.left, node, index)
        if tree.right:
            answer += calculate_tree(tree.right, node, index)
    elif index == len(node.options):
        # At this point everything must be operational
        while True:
            tree = tree.right
            if tree.left and not(tree.right):
                return 0

            if not tree.left and not tree.right:
                return 1
    elif tree.char == "#":
        sequence_count = node.options[index]
        for i in range(sequence_count):
            if tree:
                sequence_count += 1
                tree = tree.left
            else:
                return 0

        if not(tree):
            return 0

        tree = tree.right
        if not(tree):
            return 0

        answer += calculate_tree(tree, node, index + 1)
    elif tree.char == ".":
        if tree.left:
            answer += calculate_tree(tree.left, node, index)
        if tree.right:
            answer += calculate_tree(tree.right, node, index)

    return answer


class Node:
    def __init__(self):
        self.line = ""
        self.options = list()


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.char = ""


