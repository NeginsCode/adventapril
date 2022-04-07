import data


def part_one(str_data):
    bin_data = [int(entry, 2) for entry in str_data]
    gamma_r = 0b0
    mask = 0b0
    count_1 = 0
    count_0 = 0
    # get exponent
    exponent = 0
    for i in range(5):
        for j in range(12):
            if bin_data[i] >= 2**j and j > exponent:
                exponent = j
    for e in range(exponent, -1, -1):
        for entry in bin_data:
            bit_mask = 2 ** e
            filtered_entry = entry & bit_mask
            if filtered_entry > 0b0:
                count_1 += 1
            else:
                count_0 += 1
        if count_0 < count_1:
            gamma_r = 2**e | gamma_r
        count_0 = 0
        count_1 = 0
        mask |= 2**e
    epsilon_r = mask ^ gamma_r

    print(bin(gamma_r))
    print(bin(epsilon_r))
    print(gamma_r*epsilon_r)


def part_two():
    pass


if __name__ == "__main__":
    test_data = [0b00100, 0b11110, 0b10110, 0b10111, 0b10101, 0b01111, 0b00111, 0b11100, 0b10000, 0b11001, 0b00010,
                 0b01010]
    #part_one(test_data)
    d3_data = data.Data(3)
    d3_data.get_preview()
    part_one(d3_data.data_str)
    part_two()
