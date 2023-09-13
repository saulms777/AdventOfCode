with open("Day4Input.txt") as file:
    file = file.read().split("\n\n")
    numbers = [int(num) for num in file[0].split(",")]
    boards = [[dict.fromkeys([int(c) for c in b.split()], 0) for b in a.split("\n")] for a in file[1:]]

print(boards)


def main():
    for num in numbers:
        for a in boards:
            for b in a:
                for c in b:
                    if c == num:
                        b[c] = 1
        winner = {}
        for a in boards:
            for b in a:
                if sum(b.values()) == 5:
                    winner = a
            for el in range(5):
                column = 0
                for b in a:
                    if b[list(b.keys())[el]] == 1:
                        column += 1
                if column == 5:
                    winner = a
        if winner != {}:
            total = 0
            for b in winner:
                for c in b:
                    if b[c] == 0:
                        total += c
            return num * total


print(main())
