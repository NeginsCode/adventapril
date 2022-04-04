import pathlib
import sys
import aocd

SESSION_ID = "53616c7465645f5f4963b68e41ac272b6efc924bde3a50262103a70e98c003e4bada61305dd829d5cd1198b0baa7d8a05149c7ceb8ea512cf40a6565b72a7a92"


def get_int_values(data):
    data_str = data.split()
    return [int(entry) for entry in data_str]


def depth_measure(sonar_data):
    depth_inc = 0
    for i in range(len(sonar_data)-1):
        if sonar_data[i] < sonar_data[i+1]:
            depth_inc += 1
    print(depth_inc)


def depth_measure_window(sonar_data):
    depth_inc = 0
    pre_sum = 1000
    for i in range(len(sonar_data)-2):
        sum = sonar_data[i] + sonar_data[i+1] + sonar_data[i+2]
        if sum > pre_sum:
            depth_inc += 1
        pre_sum = sum
    print(depth_inc)


if __name__ == "__main__":
    sonar_data_text = aocd.get_data(session=SESSION_ID, day=1, year=2021)
    sonar_data_int = get_int_values(sonar_data_text)
    depth_measure(sonar_data_int)
    depth_measure_window(sonar_data_int)