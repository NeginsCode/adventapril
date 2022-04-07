import data


def part_one():
    d2_data = data.Data(2)
    direction = d2_data.data_str[::2]
    value = [int(val) for val in d2_data.data_str[1::2]]
    horizontal = 0
    depth = 0
    for i in range(len(direction)):
        if direction[i] == "forward":
            horizontal += value[i]
        elif direction[i] == "down":
            depth += value[i]
        elif direction[i] == "up":
            depth -= value[i]
    print(horizontal * depth)


def part_two():
    aim = 0
    horizontal = 0
    depth = 0
    d2_data = data.Data(2)
    direction = d2_data.data_str[::2]
    value = [int(val) for val in d2_data.data_str[1::2]]
    #direction = ["forward", "down", "forward", "up", "down", "forward"]
    #value = [5, 5, 8, 3, 8, 2]
    for i in range(len(direction)):
        if direction[i] == "forward":
            horizontal += value[i]
            depth += (aim*value[i])
        elif direction[i] == "down":
            aim += value[i]
        elif direction[i] == "up":
            aim -= value[i]
    print(horizontal * depth)


if __name__ == "__main__":
    part_one()
    part_two()
