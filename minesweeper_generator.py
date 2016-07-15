# Given width, height, and number of mines, print out a minesweeper board
# that is randomly generated. Mines should be shown as a "*" and every other
# cell must contain the number of mines
# i.e.
# genereate(3, 3, 3)
# could print:
#
# * 2 0
# * 2 1
# 2 * 1
#
# * 3 *
# 1 3 *
# 1 * 2
import random


def generate(width, height, num_mines):
    matrix = []
    for row in xrange(0, height):
        row = []
        for col in xrange(0, width):
            row.append("0")
        matrix.append(row)

    insertion_point = -1
    for mine_num in xrange(0, num_mines):
        # insert at some random point. random point must allow available spaces for the rest of the mines
        max_index_for_next_mine = (width * height - 1) - (num_mines - mine_num - 1)
        insertion_point += random.randint(1, max_index_for_next_mine - insertion_point)

        insertion_row = insertion_point / height
        insertion_col = insertion_point % height

        # insert the mine
        matrix[insertion_row][insertion_col] = "*"

        # increment all the adjacent squares that are not mines
        def increment_matrix_if_valid(row, col):
            if 0 <= row < height and 0 <= col < width and matrix[row][col] != "*":
                matrix[row][col] = str(int(matrix[row][col]) + 1)

        # check up
        increment_matrix_if_valid(insertion_row - 1, insertion_col)
        # check up left
        increment_matrix_if_valid(insertion_row - 1, insertion_col - 1)
        # check up right
        increment_matrix_if_valid(insertion_row - 1, insertion_col + 1)

        # check down
        increment_matrix_if_valid(insertion_row + 1, insertion_col)
        # check down left
        increment_matrix_if_valid(insertion_row + 1, insertion_col - 1)
        # check down right
        increment_matrix_if_valid(insertion_row + 1, insertion_col + 1)

        # check left
        increment_matrix_if_valid(insertion_row, insertion_col - 1)
        # check right
        increment_matrix_if_valid(insertion_row, insertion_col + 1)

    for row in matrix:
        print " ".join(row)

    return matrix

generate(3, 3, 3)
