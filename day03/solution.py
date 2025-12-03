import sys


def biggest_recurse(bank: list[int], ignore_end: int) -> int:
    a = max(bank[: -ignore_end if ignore_end != 0 else None])
    curr_index = bank.index(a)
    if ignore_end == 0:
        return a
    return a * 10**ignore_end + biggest_recurse(bank[curr_index + 1 :], ignore_end - 1)


def part1(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        bank = list(map(int, list(line)))
        pair = biggest_recurse(bank, 1)
        result += pair
    return result


def part2(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        bank = list(map(int, list(line)))
        pair = biggest_recurse(bank, 11)
        result += pair
    return result


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
