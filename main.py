from Day01 import day01

if __name__ == '__main__':
    part1_test = day01("./inputs/test-01.txt", False)
    print(f"Part 1 Test: {part1_test}")

    part1_real = day01("./inputs/real-01.txt", False)
    print(f"Part 1 Real: {part1_real}")

    part2_test = day01("./inputs/test-01-b.txt", True)
    print(f"Part 2 Test: {part2_test}")

    part2_real = day01("./inputs/real-01.txt", True)
    print(f"Part 2 Real: {part2_real}")
