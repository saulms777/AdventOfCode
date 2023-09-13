from collections import defaultdict


def main(file):
    with open(file, "r") as f:
        f = f.read().split("$ ")[1:]
        system = defaultdict(int)
        for command in f:
            if command[:2] == "cd":
                if command[3] == "/":
                    current = ["/"]
                elif command[3:5] == "..":
                    current.pop()
                else:
                    current.append(command[3:-1])
            else:
                for line in command[3:-1].split("\n"):
                    if line[:3] != "dir":
                        for i in range(len(current)):
                            system["/".join(current[:i + 1])] += int(line.split()[0])

        print(sum([size for size in system.values() if size <= 100_000]))
        print(min([size for size in system.values() if size >= system["/"] - (70_000_000 - 30_000_000)]))


if __name__ == "__main__":
    main("Day7Input.txt")
