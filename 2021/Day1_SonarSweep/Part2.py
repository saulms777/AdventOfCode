with open("Day1Input.txt") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

windows = []
for el in range(len(numbers) - 2):
    windows.append(numbers[el] + numbers[el + 1] + numbers[el + 2])

increase = 0
for el in range(len(windows) - 1):
    if windows[el] < windows[el + 1]:
        increase += 1

print(increase)
