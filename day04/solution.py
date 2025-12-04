import sys


def check_location(grid: list[list[str]], line: int, col: int) -> bool:
    offsets = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1)]
    count = 0
    for offset_col, offset_line in offsets:
        if (
            col + offset_col < 0
            or line + offset_line < 0
            or col + offset_col >= len(grid[0])
            or line + offset_line >= len(grid)
        ):
            continue
        if grid[line + offset_line][col + offset_col] == "@":
            count += 1
    return count < 4


def part1(input_list: list[str]) -> int:
    grid = [list(x) for x in input_list]
    answer = 0
    for line in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[line][col] == "@" and check_location(grid, line, col):
                answer += 1
    return answer


def part2(input_list: list[str]) -> int:
    grid = [list(x) for x in input_list]
    answer = 0
    success = True
    while success:
        success = False
        for line in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[line][col] == "@" and check_location(grid, line, col):
                    answer += 1
                    grid[line][col] = "."
                    success = True
    return answer


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
