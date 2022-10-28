with open("Day3Input.txt") as file:
    bits = [number.strip() for number in file.readlines()]


def main(inp, type):
    numbers = inp.copy()
    for el in range(12):
        if len(numbers) > 1:
            temp = [number[el] for number in numbers]
            if temp.count("0") <= len(temp) / 2:
                if type == "oxygen":
                    keep = "1"
                else:
                    keep = "0"
            else:
                if type == "oxygen":
                    keep = "0"
                else:
                    keep = "1"
            numbers = [bit for bit in numbers if bit[el] == keep]
    return numbers


print(int(main(bits, "oxygen")[0], 2) * int(main(bits, "CO2")[0], 2))
