def part1(file):
    with open(file, "r") as f:
        print(sum([(ord(game.split(" ")[1]) - ord(game.split(" ")[0]) + 2) % 3 * 3 + ord(game.split(" ")[1]) - 87 for game in f.read().split("\n")]))  # NOQA: E501


def part2(file):
    with open(file, "r") as f:
        print(sum([(ord(game.split(" ")[1]) + ord(game.split(" ")[0]) - 151) % 3 + 1 + (ord(game.split(" ")[1]) - 88) * 3 for game in f.read().split("\n")]))  # NOQA: E501


if __name__ == "__main__":
    part1("Day2Input.txt")
    part2("Day2Input.txt")
