import data


def exponent_det(d):
    exponent = 0
    for i in range(5):
        for j in range(12):
            if d[i] >= 2**j and j > exponent:
                exponent = j
    return exponent


def ratio_0_to_1(bdata, exp):
    count = [0, 0]
    sep_data = [[], []]
    mask = 2 ** exp
    for e in bdata:
        filtered_e = e & mask
        if filtered_e > 0b0:
            count[1] += 1
            sep_data[1].append(e)
        else:
            count[0] += 1
            sep_data[0].append(e)
    return count, sep_data


def part_one(str_data):
    bin_data = [int(entry, 2) for entry in str_data]
    gamma_r = 0b0
    mask = 0b0
    # get exponent
    exponent = exponent_det(bin_data)

    for e in range(exponent, -1, -1):
        count, sep_data = ratio_0_to_1(bin_data, e)
        if count[0] < count[1]:
            gamma_r = 2**e | gamma_r
        mask |= 2**e
    epsilon_r = mask ^ gamma_r

    print(bin(gamma_r))
    print(bin(epsilon_r))
    print(gamma_r*epsilon_r)


def part_two(str_data):
    bin_data = [int(entry, 2) for entry in str_data]
    exponent = exponent_det(bin_data)

    # do O2
    subset_data = bin_data
    for e in range(exponent, -1, -1):
        if len(subset_data) > 1:
            count, sep_data = ratio_0_to_1(subset_data, e)
            if count[0] > count[1]:
                subset_data = sep_data[0]
            else:
                subset_data = sep_data[1]
    o2 = subset_data[0]
    print(o2)

    # do CO2
    subset_data = bin_data
    for e in range(exponent, -1, -1):
        if len(subset_data) > 1:
            count, sep_data = ratio_0_to_1(subset_data, e)
            if count[0] > count[1]:
                subset_data = sep_data[1]
            else:
                subset_data = sep_data[0]
    co2 = subset_data[0]
    print(co2)
    print(o2 * co2)


if __name__ == "__main__":
    test_data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                 "01010"]
    part_one(test_data)
    d3_data = data.Data(3)
    d3_data.get_preview()
    part_one(d3_data.data_str)
    part_two(test_data)
    part_two(d3_data.data_str)

