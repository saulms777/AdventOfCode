with open("Day1Input.txt") as file:
    numbers = [int(line.strip()) for line in file.readline()]

increase = 0
for el in range(len(numbers) - 1):
    if numbers[el] < numbers[el + 1]:
        increase += 1

print(increase)
