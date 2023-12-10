
def day06(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    time = list()
    distance = list()

    for line in lines:
        parts = line.split(":")
        data_type = parts[0]
        numbers_part = parts[1].rstrip()

        if is_part_2:
            numbers_part = numbers_part.replace(" ", "")

        numbers = numbers_part.split(" ")

        number_list = list()
        for number in numbers:
            if number.isnumeric():
                number_list.append(int(number))

        if data_type == "Time":
            time = number_list
        elif data_type == "Distance":
            distance = number_list
        else:
            raise "Invalid Data Type"

    number_of_races = len(time)
    answer = 1

    for i in range(number_of_races):
        allowed_time = time[i]
        best_distance = distance[i]

        number_of_ways_to_win = 0
        for j in range(allowed_time):
            speed = j * 1
            time_to_move = allowed_time - j
            calc_distance = time_to_move * speed

            if calc_distance > best_distance:
                number_of_ways_to_win += 1

        answer = answer * number_of_ways_to_win

    return answer




