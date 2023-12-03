from Day01 import day01
from Day02 import day02

if __name__ == '__main__':
    input_file = "./inputs/real-02.txt"
    day = "02"
    part2 = True

    day_functions = {
        "01": day01,
        "02": day02
    }

    answer = day_functions[day](input_file, part2)
    print(f"Answer: {answer}")


