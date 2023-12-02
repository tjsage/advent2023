
def day01(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    answer = 0

    for line in lines:
        adjusted_line = line
        if is_part_2:
            leftover = adjusted_line
            adjusted_line = ""

            while len(leftover) > 0:
                if leftover[0].isnumeric():
                    adjusted_line += leftover[0]
                elif leftover.startswith("one"):
                    adjusted_line += "1"
                elif leftover.startswith("two"):
                    adjusted_line += "2"
                elif leftover.startswith("three"):
                    adjusted_line += "3"
                elif leftover.startswith("four"):
                    adjusted_line += "4"
                elif leftover.startswith("five"):
                    adjusted_line += "5"
                elif leftover.startswith("six"):
                    adjusted_line += "6"
                elif leftover.startswith("seven"):
                    adjusted_line += "7"
                elif leftover.startswith("eight"):
                    adjusted_line += "8"
                elif leftover.startswith("nine"):
                    adjusted_line += "9"
                else:
                    adjusted_line += leftover[0]

                leftover = leftover[1:]

        first_digit = -1
        second_digit = -1

        for char in adjusted_line:
            if char.isnumeric():
                value = int(char)
                if first_digit == -1:
                    first_digit = value

                second_digit = value

        answer += (first_digit * 10) + second_digit

    return answer


