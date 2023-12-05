from collections import deque


def day04(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    answer = 0

    if is_part_2:
        winning_numbers = list()
        my_numbers = list()

        for line in lines:
            adjusted_line = line.strip()
            parts = adjusted_line.split(":")
            number_sections = parts[1].split("|")
            line_winning = number_sections[0].split(" ")
            line_my_numbers = number_sections[1].split(" ")

            winning_numbers.append(line_winning)
            my_numbers.append(line_my_numbers)

        queue = deque()
        processed = 0
        for i in range(len(winning_numbers)):
            queue.append(i + 1)

        while len(queue) > 0:
            processed += 1
            card_number = queue.popleft()
            line_winning = winning_numbers[card_number - 1]
            line_my_numbers = my_numbers[card_number - 1]

            winning_count = 0
            for winning in line_winning:
                if winning in line_my_numbers and len(winning) > 0:
                    winning_count += 1

            for i in range(winning_count):
                queue.append(card_number + i + 1)



        answer = processed

    else:
        for line in lines:
            adjusted_line = line.strip()
            parts = adjusted_line.split(":")
            number_sections = parts[1].split("|")
            winning_numbers = number_sections[0].split(" ")
            my_numbers = number_sections[1].split(" ")

            winning_found = 0
            line_score = 0
            for winning in winning_numbers:
                if winning in my_numbers and len(winning) > 0:
                    winning_found += 1
                    line_score = pow(2, (winning_found - 1))

            answer += line_score

    return answer



