class Vents:
    def __init__(self, file, part):
        with open(file) as f:
            f = f.read().split("\n")
            self.lines = tuple([tuple([tuple(map(int, pair.split(",")))
                                       for pair in line.split(" -> ")]) for line in f])

        self.vents = [[0] * 1000 for _ in range(1000)]
        self.part = part

    def drawLines(self):
        for line in self.lines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]
            if x1 == x2:
                for row in range(min(y1, y2), max(y1, y2) + 1):
                    self.vents[row][x1] += 1
            elif y1 == y2:
                for column in range(min(x1, x2), max(x1, x2) + 1):
                    self.vents[y1][column] += 1
            else:
                if self.part == 2:
                    if (y1 - y2) / (x1 - x2) == 1:
                        for el in range(abs(y1 - y2) + 1):
                            self.vents[min(y1, y2) + el][min(x1, x2) + el] += 1
                    else:
                        for el in range(abs(y1 - y2) + 1):
                            self.vents[max(y1, y2) - el][min(x1, x2) + el] += 1

    def findNumberDangerous(self):
        dangerousAreas = 0
        for column in self.vents:
            for row in column:
                if row >= 2:
                    dangerousAreas += 1
        return dangerousAreas


def part1():
    vents = Vents("Day5Input.txt", 1)
    vents.drawLines()
    print(vents.findNumberDangerous())


def part2():
    vents = Vents("Day5Input.txt", 2)
    vents.drawLines()
    print(vents.findNumberDangerous())


if __name__ == "__main__":
    part1()
    part2()
