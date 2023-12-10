from Day01 import day01
from Day02 import day02
from Day03 import day03
from Day04 import day04
from Day05 import day05
from Day06 import day06
from Day07 import day07
from Day08 import day08
from Day09 import day09
from Day10 import day10

if __name__ == '__main__':
    input_file = "./inputs/test-10c.txt"
    day = "10"
    part2 = True

    day_functions = {
        "01": day01,
        "02": day02,
        "03": day03,
        "04": day04,
        "05": day05,
        "06": day06,
        "07": day07,
        "08": day08,
        "09": day09,
        "10": day10,
    }

    answer = day_functions[day](input_file, part2)
    print(f"Answer: {answer}")

    #619 too high
