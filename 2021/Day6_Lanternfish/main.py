class Lanternfish:
    def __init__(self, file):
        with open(file) as f:
            self.ages = {age: 0 for age in range(9)}
            for fish in list(map(int, f.read().split(","))):
                self.ages[fish] += 1

    def updateDay(self):
        new = self.ages[0]
        for age in range(8):
            self.ages[age] = self.ages[age + 1]
        self.ages[6] += new
        self.ages[8] = new


def findFish(days, file):
    lanternfish = Lanternfish(file)
    for _ in range(days):
        lanternfish.updateDay()
    print(sum(lanternfish.ages.values()))


if __name__ == "__main__":
    findFish(256, "Day6Input.txt")
