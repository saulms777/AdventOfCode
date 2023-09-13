class Segments:
    def __init__(self, file):
        with open(file) as f:
            f = f.read().split("\n")
            self.numbers = tuple([tuple([tuple(side.split(" ")) for side in line.split(" | ")]) for line in f])

    def findUniqueDigitstest(self):
        unique = 0
        for display in self.numbers:
            for number in display[1]:
                if len(number) in (2, 3, 4, 7):
                    unique += 1
        return unique

    def findUniqueDigits(self, display):
        pass

    def decodeDisplay(self, displayIndex):
        # digitSegments = ((0, 1, 2, 4, 5, 6), (2, 5), (0, 2, 3, 4, 6), (0, 2, 3, 5, 6), (1, 2, 3, 5), (0, 1, 3, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 5), (0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 5, 6))
        digitSegments = ((2, 5), (1, 2, 3, 5), (0, 2, 5), (0, 1, 2, 3, 4, 5, 6))
        decodedDisplay = [["a", "b", "c", "d", "e", "f", "g"] for _ in range(7)]
        for number in self.numbers[displayIndex][0]:
            for digit in digitSegments:
                if len(digit) == len(number):
                    for segment in digit:
                        for char in ("a", "b", "c", "d", "e", "f", "g"):
                            if char not in number and char in decodedDisplay[segment]:
                                decodedDisplay[segment].remove(char)
        print(decodedDisplay)


def part1():
    segments = Segments("Day8Input.txt")
    print(segments.findUniqueDigitstest())


def part2():
    segments = Segments("ExampleInput.txt")
    print(segments.numbers[0][0])
    segments.decodeDisplay(0)


if __name__ == "__main__":
    part2()
