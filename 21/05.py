import data
import numpy as np


def part_one(str_data):
    # prepare data
    drawn_numbers = [int(num) for num in str_data[0].split(',')]
    board_numbers = [int(entry) for entry in str_data[1:]]


def part_two(str_data):
    # prepare data
    drawn_numbers = [int(num) for num in str_data[0].split(',')]
    board_numbers = [int(entry) for entry in str_data[1:]]


if __name__ == "__main__":
    d5_data = data.Data(5)

    test_file = open("05_test.txt", "r")
    test_data = test_file.read()
    print("P1: Test set")
    #part_one(test_data.split())
    print("P1: Actual set")
    #part_one(d5_data.data_str)
    print("P2: Test set")
    #part_two(test_data.split())
    print("P2: Actual set")
    #part_two(d5_data.data_str)