from Day01 import day01
from Day02 import day02

if __name__ == '__main__':
    day = 2

    if day == 1:
        part1_test = day01("./inputs/test-01.txt", False)
        print(f"Part 1 Test: {part1_test}")

        part1_real = day01("./inputs/real-01.txt", False)
        print(f"Part 1 Real: {part1_real}")

        part2_test = day01("./inputs/test-01-b.txt", True)
        print(f"Part 2 Test: {part2_test}")

        part2_real = day01("./inputs/real-01.txt", True)
        print(f"Part 2 Real: {part2_real}")

    elif day == 2:
        part1_test = day02("./inputs/test-02.txt", False)
        print(f"Part 1 Test: {part1_test}")

        part1_real = day02("./inputs/real-02.txt", False)
        print(f"Part 1 Real: {part1_real}")

        part2_test = day02("./inputs/test-02.txt", True)
        print(f"Part 2 Test: {part2_test}")

        part2_real = day02("./inputs/real-02.txt", True)
        print(f"Part 2 Real: {part2_real}")
