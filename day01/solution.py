import sys


def part1(input_list: list[str]) -> int:
    result = 0
    state = 50
    for line in input_list:
        delta = int(line[1:])
        if line[0] == "L":
            delta = -delta
        state += delta
        state %= 100
        if state == 0:
            result += 1
    return result


def part2(input_list: list[str]) -> int:
    result = 0
    state = 50
    lsum, rsum = 0, 0
    for line in input_list:
        delta = int(line[1:])
        one = -1 if line[0] == "L" else 1
        for _ in range(delta):
            state = (state + one) % 100
            if state == 0:
                result += 1
    print(lsum, rsum)
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
