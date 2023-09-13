def draw_grid(coords: set):
    print(coords)
    offset_x = min(tuple(zip(*coords))[0])
    offset_y = min(tuple(zip(*coords))[1])
    x = max(tuple(zip(*coords))[0]) + 1
    y = max(tuple(zip(*coords))[1]) + 1
    print(x, y, offset_x, offset_y)
    grid = [["."] * (y - offset_y) for _ in range(x - offset_x)]
    for coord in coords:
        grid[coord[1] - offset_y][coord[0] - offset_x] = "*"
    grid.reverse()
    for row in grid:
        print("".join(row))
    print()


def part1(file):
    with open(file, "r") as path:
        path = tuple([(line.split()[0], int(line.split()[1])) for line in path.read().split("\n")])
        print(path)

    visited = {(0, 0)}
    head = [0, 0]
    tail = [0, 0]
    direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for instruction in path:
        for _ in range(instruction[1]):
            head[0] += direction[instruction[0]][0]
            head[1] += direction[instruction[0]][1]
            if (abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 1) \
                    or (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 2):
                if direction[instruction[0]][0] == 0:
                    tail[0] = head[0]
                    tail[1] += direction[instruction[0]][1]
                elif direction[instruction[0]][1] == 0:
                    tail[0] += direction[instruction[0]][0]
                    tail[1] = head[1]
            elif abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2:
                tail[0] += direction[instruction[0]][0]
                tail[1] += direction[instruction[0]][1]
            visited.add((tail[0], tail[1]))

    draw_grid(visited)

    print(sorted(visited))
    print(len(visited))


def part2(file):
    with open(file, "r") as path:
        path = tuple([(line.split()[0], int(line.split()[1])) for line in path.read().split("\n")])
        print(path)

    visited = {(0, 0)}
    rope = [[0, 0] for _ in range(10)]
    direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for instruction in path:
        for _ in range(instruction[1]):
            rope[0][0] += direction[instruction[0]][0]
            rope[0][1] += direction[instruction[0]][1]
            for i in range(9):
                if (abs(rope[i][0] - rope[i + 1][0]) == 2 and abs(rope[i][1] - rope[i + 1][1]) == 1) \
                        or (abs(rope[i][0] - rope[i + 1][0]) == 1 and abs(rope[i][1] - rope[i + 1][1]) == 2):
                    if direction[instruction[0]][0] == 0:
                        rope[i + 1][0] = rope[i][0]
                        rope[i + 1][1] += direction[instruction[0]][1]
                    elif direction[instruction[0]][1] == 0:
                        rope[i + 1][0] += direction[instruction[0]][0]
                        rope[i + 1][1] = rope[i][1]
                elif abs(rope[i][0] - rope[i + 1][0]) == 2 or abs(rope[i][1] - rope[i + 1][1]) == 2:
                    rope[i + 1][0] += direction[instruction[0]][0]
                    rope[i + 1][1] += direction[instruction[0]][1]
            visited.add((rope[9][0], rope[9][1]))

    draw_grid(visited)

    print(sorted(visited))
    print(len(visited))


if __name__ == "__main__":
    # part1("ExampleInput1.txt")
    part2("ExampleInput2.txt")
