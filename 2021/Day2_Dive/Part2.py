with open("Day2Input.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

direction = [line[:line.index(" ")] for line in instructions]
amount = [int(line[line.index(" ") + 1:]) for line in instructions]

forward = 0
aim = 0
depth = 0
for el in range(len(instructions)):
    if direction[el] == "forward":
        forward += amount[el]
        depth += amount[el] * aim
    elif direction[el] == "down":
        aim += amount[el]
    elif direction[el] == "up":
        aim -= amount[el]

print(forward * depth)
