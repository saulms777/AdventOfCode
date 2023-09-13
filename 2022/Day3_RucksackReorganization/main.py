def part1(file):
    with open(file, "r") as f:
        print(sum([ord("".join(set(line[:len(line) // 2]) & set(line[len(line) // 2:]))) - (96 if "".join(set(line[:len(line) // 2]) & set(line[len(line) // 2:])).islower() else 38) for line in f.read().split("\n")]))  # NOQA: E501


def part2(file):
    with open(file, "r") as f:
        print(sum([ord("".join(set(group[0]) & set(group[1]) & set(group[2]))) - (96 if "".join(set(group[0]) & set(group[1]) & set(group[2])).islower() else 38) for group in zip(*(iter(f.read().split("\n")),) * 3)]))  # NOQA: E501


if __name__ == "__main__":
    part1("Day3Input.txt")
    part2("Day3Input.txt")
