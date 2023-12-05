from Day01 import day01
from Day02 import day02
from Day03 import day03
from Day04 import day04

if __name__ == '__main__':
    input_file = "./inputs/real-04.txt"
    day = "04"
    part2 = True

    day_functions = {
        "01": day01,
        "02": day02,
        "03": day03,
        "04": day04
    }

    answer = day_functions[day](input_file, part2)
    print(f"Answer: {answer}")


