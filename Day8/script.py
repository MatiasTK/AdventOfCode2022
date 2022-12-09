""" Advent of Code - Day 8 """


def is_edge(list_index, matrix_len, number_index, list_len):
    """Returns true if a number is in the edge of the matrix"""
    if list_index == 0 or list_index == matrix_len - 1:
        return True

    if number_index == 0 or number_index == list_len - 1:
        return True

    return False


def check_left(matrix_lists, actual_number, actual_number_index, actual_list_index):
    """Returns a boolean indicating if the left side of the number is visible and the number
    of visible numbers before the first number that is higher than the actual number"""
    counter = 0
    visibility = True

    for i in range(actual_number_index):
        counter += 1
        if matrix_lists[actual_list_index][i] >= actual_number:
            counter = 1
            visibility = False

    return visibility, counter


def check_right(
    matrix_lists, actual_number, actual_number_index, actual_list_index, actual_list_len
):
    """Returns a boolean indicating if the right side of the number is visible and the number
    of visible numbers before the first number that is higher than the actual number"""
    counter = 0
    visibility = True
    for i in range(actual_number_index + 1, actual_list_len):
        if matrix_lists[actual_list_index][i] >= actual_number:
            visibility = False
            counter += 1
            break
        counter += 1

    return visibility, counter


def check_top(matrix_lists, actual_number, actual_number_index, actual_list_index):
    """Returns a boolean indicating if the top side of the number is visible and the number
    of visible numbers before the first number that is higher than the actual number"""
    counter = 0
    visibility = True

    for i in range(actual_list_index):
        counter += 1
        if matrix_lists[i][actual_number_index] >= actual_number:
            visibility = False
            counter = 1

    return visibility, counter


def check_bottom(
    matrix_lists, matrix_len, actual_number, actual_number_index, actual_list_index
):
    """Returns a boolean indicating if the bottom side of the number is visible and the number
    of visible numbers before the first number that is higher than the actual number"""
    visibility = True
    counter = 0

    for i in range(actual_list_index + 1, matrix_len):
        if matrix_lists[i][actual_number_index] >= actual_number:
            visibility = False
            counter += 1
            break
        counter += 1

    return visibility, counter


file = open("input.txt", "r", encoding="utf-8")

lines = file.read().strip().split("\n")

matrix = []
for line in lines:
    l = []
    for number in line:
        l.append(int(number))

    matrix.append(l)

MATRIX_L = len(matrix)
visibles = 0
max_score = 0
for list_i, list_v in enumerate(matrix):
    list_l = len(list_v)

    for number_i, number_v in enumerate(list_v):

        if is_edge(list_i, MATRIX_L, number_i, list_l):
            visibles += 1
        else:
            scenic_score = []

            is_visible = False

            visible, score = check_left(matrix, number_v, number_i, list_i)
            if visible:
                is_visible = True
            scenic_score.append(score)

            visible, score = check_right(matrix, number_v, number_i, list_i, list_l)
            if visible:
                is_visible = True
            scenic_score.append(score)

            visible, score = check_top(matrix, number_v, number_i, list_i)
            if visible:
                is_visible = True
            scenic_score.append(score)

            visible, score = check_bottom(matrix, MATRIX_L, number_v, number_i, list_i)
            if visible:
                is_visible = True
            scenic_score.append(score)

            if is_visible:
                visibles += 1

            result = 1
            for n in scenic_score:
                result *= n
            if result > max_score:
                max_score = result


print(visibles)
print(max_score)
