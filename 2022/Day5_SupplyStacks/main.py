def parse(file):
    with open(file, "r") as f:
        f = f.read().split("\n\n")

        stacks = []
        for line in f[0].split("\n")[:-1]:
            line = list(line)
            del line[::2]
            stacks.append("".join(line)[::2])
        for index, item in enumerate(stacks):
            if len(item) < len(max(stacks, key=len)):
                stacks[index] += " " * (len(max(stacks, key=len)) - len(stacks[index]))
        stacks = [list(x)[::-1] for x in zip(*stacks)]
        for row_index, row_item in enumerate(stacks):
            for column_index in range(len(row_item) - 1, 0, -1):
                if row_item[column_index] == " ":
                    del stacks[row_index][column_index]

        instructions = [tuple(map(int, line.split(" ")[1::2])) for line in f[1].split("\n")]

        return stacks, instructions


def part1(file):
    data = parse(file)

    for instruction in data[1]:
        for _ in range(instruction[0]):
            data[0][instruction[2] - 1].append(data[0][instruction[1] - 1].pop())

    print("".join([stack[len(stack) - 1] for stack in data[0]]))


def part2(file):
    data = parse(file)

    for instruction in data[1]:
        temp = []
        for _ in range(instruction[0]):
            temp.append(data[0][instruction[1] - 1].pop())
        temp.reverse()
        for box in temp:
            data[0][instruction[2] - 1].append(box)

    print("".join([stack[len(stack) - 1] for stack in data[0]]))


if __name__ == "__main__":
    part1("Day5Input.txt")
    part2("Day5Input.txt")
