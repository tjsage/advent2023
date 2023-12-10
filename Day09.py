
def day09(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    answer = 0

    for line in lines:
        clean_line = line.rstrip()
        parts = clean_line.split(" ")
        num_list = list()
        for part in parts:
            num_list.append(int(part))

        answer += calculate_diffs(num_list, is_part_2)

    return answer


def calculate_diffs(input_list, is_part_2):
    length = len(input_list)
    output = list()

    only_zeros = True
    for i in range(1, length):
        diff = input_list[i] - input_list[i - 1]
        if diff != 0:
            only_zeros = False
        output.append(diff)

    if only_zeros:
        if is_part_2:
            return input_list[0] - output[0]
        else:
            return output[len(output) - 1] + input_list[len(input_list) - 1]
    else:
        if is_part_2:
            diff = calculate_diffs(output, is_part_2)
            return input_list[0] - diff
        else:
            diff = calculate_diffs(output, is_part_2)
            return diff + input_list[len(input_list) - 1]




