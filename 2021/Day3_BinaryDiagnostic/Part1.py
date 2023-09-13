with open("Day3Input.txt") as file:
    bits = [number.strip() for number in file.readlines()]

numbers = []
for el in range(12):
    numbers.append([int(number[el]) for number in bits])

gamma = ""
epsilon = ""
for el in range(12):
    if numbers[el].count(1) < 500:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))
