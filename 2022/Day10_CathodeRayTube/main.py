def part1(file):
    with open(file, "r") as f:
        f = f.read().split("\n")

    cycle = 0
    increase = [1]
    signals = []
    for command in f:
        if command[:4] == "noop":
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                signals.append(cycle * sum(increase))
        elif command[:4] == "addx":
            for _ in range(2):
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    signals.append(cycle * sum(increase))
            increase.append(int(command[5:]))

    print(signals)
    print(sum(signals))


def part2(file):
    with open(file, "r") as f:
        f = f.read().split("\n")

    cycle = 0
    sprite = [0, 1, 2]
    print(f"Sprite position: {''.join(['#' if i in sprite else '.' for i in range(40)])}")
    print()
    crt = []
    row = ""
    for command in f:
        if command[:4] == "noop":
            cycle += 1
            print(f"Start cycle {cycle}: begin executing noop")
            row += "."
            print(f"Current CRT row: {row}")
            print(f"End of cycle {cycle}: finish executing noop")
            print()
            if len(row) == 40:
                crt.append(row)
                row = ""
        elif command[:4] == "addx":
            print(f"Start cycle {cycle}: begin executing {command}")
            cycle += 1
            row += "#" if cycle in sprite else "."
            print(f"Current CRT row: {row}")
            print()
            if len(row) == 40:
                crt.append(row)
                row = ""

            cycle += 1
            row += "#" if cycle in sprite else "."
            print(f"Current CRT row: {row}")
            sprite = [e + int(command[5:]) for e in sprite]
            print(f"End of cycle {cycle}: finish executing {command}")
            print(f"Sprite position: {''.join(['#' if i in sprite else '.' for i in range(40)])}")
            print()
            if len(row) == 40:
                crt.append(row)
                row = ""

    print(row)


if __name__ == "__main__":
    # part1("Day10Input.txt")
    part2("ExampleInput.txt")
