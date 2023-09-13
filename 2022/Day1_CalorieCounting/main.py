def part1(file):
    with open(file, "r") as f:
        print(max([sum(tuple(map(int, elf.split("\n")))) for elf in f.read().split("\n\n")]))


def part2(file):
    with open(file, "r") as f:
        print(sum(sorted([sum(tuple(map(int, elf.split("\n")))) for elf in f.read().split("\n\n")], reverse=True)[:3]))


if __name__ == "__main__":
    part1("Day1Input.txt")
    part2("Day1Input.txt")
