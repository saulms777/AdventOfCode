with open("Day2Input.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

direction = [line[:line.index(" ")] for line in instructions]
amount = [int(line[line.index(" ") + 1:]) for line in instructions]

forward = 0
depth = 0
for el in range(len(instructions)):
    if direction[el] == "forward":
        forward += amount[el]
    elif direction[el] == "down":
        depth += amount[el]
    elif direction[el] == "up":
        depth -= amount[el]

print(forward * depth)
