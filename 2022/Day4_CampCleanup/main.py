def part1(file):
    with open(file, "r") as f:
        count = 0
        for pair in f.read().split("\n"):
            ranges = [set(range(int(a[:a.index("-")]), int(a[a.index("-") + 1:]) + 1)) for a in pair.split(",")]
            if ranges[0] <= ranges[1] or ranges[1] <= ranges[0]:
                count += 1
        print(count)


def part2(file):
    with open(file, "r") as f:
        count = 0
        for pair in f.read().split("\n"):
            ranges = [set(range(int(a[:a.index("-")]), int(a[a.index("-") + 1:]) + 1)) for a in pair.split(",")]
            if len(ranges[0] & ranges[1]) != 0:
                count += 1
        print(count)


if __name__ == "__main__":
    part1("Day4Input.txt")
    part2("Day4Input.txt")
