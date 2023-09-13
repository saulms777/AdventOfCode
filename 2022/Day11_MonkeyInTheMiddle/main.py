from collections import deque
from math import prod


class Monkey:
    def __init__(self, items: list[int, ...], operation: tuple[str, str], check: int, true: int, false: int) -> None:
        self.items: deque = deque(items)
        self.operation: tuple[str, str] = operation
        self.check: int = check
        self.true: int = true
        self.false: int = false
        self.inspections: int = 0


def read_file(file) -> list[Monkey, ...]:
    with open(file, "r") as f:
        monkeys: list[Monkey, ...] = []
        for monkey in f.read().split("\n\n"):
            lines = monkey.split("\n")
            items: list[int, ...] = list(map(int, lines[1].strip()[16:].split(", ")))
            operation: tuple[str, str] = lines[2].strip()[21:22], lines[2].strip()[23:]
            check: int = int(lines[3].strip()[19:])
            true: int = int(lines[4].strip()[25:])
            false: int = int(lines[5].strip()[26:])
            monkeys.append(Monkey(items, operation, check, true, false))
        return monkeys


def main(file, part) -> None:
    monkeys: list[Monkey, ...] = read_file(file)
    divisor = prod(monkey.check for monkey in monkeys)
    for _ in range(20 if part == 1 else 10000):
        for index, monkey in enumerate(monkeys):
            while monkeys[index].items:
                current = monkeys[index].items.popleft()
                if monkey.operation[0] == "+":
                    current += int(monkey.operation[1])
                elif monkey.operation[0] == "*":
                    if monkey.operation[1] == "old":
                        current **= 2
                    else:
                        current *= int(monkey.operation[1])
                monkeys[index].inspections += 1
                if part == 1:
                    current //= 3
                elif part == 2:
                    current %= divisor
                if current % monkey.check == 0:
                    monkeys[monkey.true].items.append(current)
                else:
                    monkeys[monkey.false].items.append(current)

    print(prod(tuple(reversed(sorted([monkey.inspections for monkey in monkeys])))[:2]))


if __name__ == "__main__":
    main("Day11Input.txt", 1)
    main("Day11Input.txt", 2)
