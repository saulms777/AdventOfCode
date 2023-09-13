def main(file, length):
    with open(file, "r") as f:
        f = tuple(f.read())
        for index in range(len(f) - length + 1):
            temp = f[index:index + length]
            if len(temp) == len(set(temp)):
                print(index + length)
                break


if __name__ == "__main__":
    main("Day6Input.txt", 4)
    main("Day6Input.txt", 14)
