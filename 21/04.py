import data
import numpy as np


def get_boards(board_numbers):

    board_size = 5
    boards = []

    num_of_boards = int(len(board_numbers)/board_size**2)

    for board_index in range(num_of_boards):
        board = np.empty([board_size, board_size])
        for row_index in range(board_size):
            row = np.array(board_numbers[(board_index*board_size**2)+(row_index*board_size):
                                         (board_index*board_size**2)+(row_index*board_size)+board_size])
            board[row_index] = row
        boards.append(board)
    return boards, num_of_boards


def part_one(str_data):
    # prepare data
    drawn_numbers = [int(num) for num in str_data[0].split(',')]
    board_numbers = [int(entry) for entry in str_data[1:]]
    boards, num_of_boards = get_boards(board_numbers)

    # let's play
    # 1. draw number
    # 2. mark in boards
    # 3. check if winner
    board_score = 0
    for number in drawn_numbers:
        for board_index in range(num_of_boards):
            board = boards[board_index]
            board[board == number] = -1
            row_sum = np.sum(board, axis=0)
            col_sum = np.sum(board, axis=1)
            if row_sum[row_sum == -5] or col_sum[col_sum == -5]:
                board[board == -1] = 0
                board_score = np.sum(board) * number
                print("Board: " + str(board_index+1))
                print(board)
                print("Winning Draw: " + str(number))
                break

        if board_score > 0:
            break
    print(int(board_score))


def part_two(str_data):
    # prepare data
    drawn_numbers = [int(num) for num in str_data[0].split(',')]
    board_numbers = [int(entry) for entry in str_data[1:]]
    boards, num_of_boards = get_boards(board_numbers)
    board_score = 0

    for number in drawn_numbers:
        winning_board_i = []
        for board_index in range(0, num_of_boards, 1):
            board = boards[board_index]
            board[board == number] = -1
            row_sum = np.sum(board, axis=0)
            col_sum = np.sum(board, axis=1)
            if row_sum[row_sum == -5] or col_sum[col_sum == -5]:
                if num_of_boards - len(winning_board_i) > 1:
                    print("Winning board: " + str(board))
                    print("removing: " + str(board_index))
                    winning_board_i.append(board_index)
                else:
                    board[board == -1] = 0
                    board_score = np.sum(board) * number
                    print("Board: " + str(board_index + 1))
                    print(board)
                    print("Winning Draw: " + str(number))
                    winning_board_i.append(board_index)

        winning_board_i.sort(reverse=True)
        for index in winning_board_i:
            boards.pop(index)
        num_of_boards = len(boards)

    print(int(board_score))


if __name__ == "__main__":
    d4_data = data.Data(4)

    test_file = open("04_test.txt", "r")
    test_data = test_file.read()
    print("P1: Test set")
    part_one(test_data.split())
    print("P1: Actual set")
    part_one(d4_data.data_str)
    print("P2: Test set")
    part_two(test_data.split())
    print("P2: Actual set")
    part_two(d4_data.data_str)
