def part_1(input_arr):
    pos = 50
    multiplier = 1
    code = 0

    for line in input_arr:
        multiplier = 1 if line[0] == "R" else -1
        pos += multiplier * int(line[1:])

        while pos < 0:
            pos = 100 + pos

        while pos > 99:
            pos = pos - 100

        if pos == 0:
            code += 1

    return code


if __name__ == "__main__":
    input_arr = []

    with open(
        "/Users/jack/Programming/Practice/advent-of-code/2025/day-1/input.txt"
    ) as file:
        for line in file:
            input_arr.append(line.strip("\n"))

    code = part_1(input_arr)
    print(code)
