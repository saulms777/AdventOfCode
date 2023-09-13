class Crabs:
    def __init__(self, file, part):
        with open(file) as f:
            self.positions = list(map(int, f.read().split(",")))
            self.positions.sort()

        self.average = 0
        self.part = part

    def findAverage(self):
        length = len(self.positions)
        if self.part == 1:
            if length % 2 == 0:
                self.average = int((self.positions[int(length / 2) - 1] + self.positions[int(length / 2)]) / 2)
            else:
                self.average = self.positions[int(length / 2)]
        else:
            self.average = int(sum(self.positions) / length)

    def calculateFuel(self):
        fuel = 0
        if self.part == 1:
            for crab in self.positions:
                fuel += abs(crab - self.average)
            return fuel
        else:
            for crab in self.positions:
                num = abs(crab - self.average)
                fuel += int(num * (num + 1) / 2)
            return fuel


if __name__ == "__main__":
    crabs = Crabs("Day7Input.txt", 2)
    crabs.findAverage()
    print(crabs.calculateFuel())
