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
from Day11 import day11
from Day12 import day12
from Day13 import day13
from Day14 import day14
from Day15 import day15
from Day16 import day16
from Day17 import day17

if __name__ == '__main__':
    input_file = "./inputs/real-17.txt"
    day = "17"
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
        "11": day11,
        "12": day12,
        "13": day13,
        "14": day14,
        "15": day15,
        "16": day16,
        "17": day17
    }

    answer = day_functions[day](input_file, part2)
    print(f"Answer: {answer}")
