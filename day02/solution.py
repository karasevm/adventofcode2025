import sys
from math import ceil, floor


def dupe_in_range(num_to_check: int, start: str, end: str):
    return num_to_check >= int(start) and num_to_check <= int(end)


def part1(input_string: str) -> int:
    answer = 0
    list_of_ranges = input_string.split(",")
    for num_range in list_of_ranges:
        start, end = num_range.split("-")
        start_half = start[: floor(len(start) / 2)]
        if start_half == "":
            start_half = 0
        end_half = end[: ceil(len(end) / 2)]
        for possible_half in range(int(start_half), int(end_half) + 1):
            if dupe_in_range(int(f"{possible_half}{possible_half}"), start, end):
                answer += int(f"{possible_half}{possible_half}")
    return answer


def part2(input_string: str) -> int:
    list_of_ranges = input_string.split(",")
    found_dupes = set()
    for num_range in list_of_ranges:
        start, end = map(int, num_range.split("-"))
        for to_test in range(start, end + 1):
            test_str = str(to_test)
            dupe_size = len(str(to_test)) // 2
            while dupe_size > 0:
                if len(test_str) % dupe_size != 0:
                    dupe_size -= 1
                    continue
                for i in range((len(test_str) // dupe_size) - 1):
                    if (
                        test_str[dupe_size * i : dupe_size * (i + 1)]
                        != test_str[dupe_size * (i + 1) : dupe_size * (i + 2)]
                    ):
                        break
                else:
                    found_dupes.add(to_test)
                    break
                dupe_size -= 1
    return sum(found_dupes)


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
        print(f"Part 1 answer: {part1(lines[0])} Part 2 answer: {part2(lines[0])}")
