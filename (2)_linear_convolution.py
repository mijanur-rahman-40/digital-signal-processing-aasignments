# convolution calculate
def linear_convolution(x, y, index_pos_x, index_pos_y):
    length_x = len(x)
    length_y = len(y)
    convolution_total_length = length_x + length_y - 1
    positive_index_x = length_x - index_pos_x - 1
    positive_index_y = length_y - index_pos_y - 1
    ans_index_positive = positive_index_x + positive_index_y

    result_indexes = []
    for i in range(-(convolution_total_length - ans_index_positive - 1), ans_index_positive + 1):
        result_indexes.append(i)

    c = [0] * convolution_total_length
    for i in enumerate(x):
        for j in enumerate(y):
            _i = i[0]
            _j = j[0]
            c[_i + _j] = c[_i + _j] + x[_i] * y[_j]

    return c, result_indexes


num = input("Give the values of signal x(n): ")
x_axis = [int(i) for i in num.split()]
index_pos_x = input(f"Initial index postion for x(n) (0-{len(x_axis)-1}): ")

num = input("Give the values of signal y(n): ")
y_axis = [int(i) for i in num.split()]
index_pos_y = input(f"Initial index postion y(n) (0-{len(y_axis)-1}): ")

arr, result_indexes = linear_convolution(
    x_axis, y_axis, int(index_pos_x), int(index_pos_y))
print('Array of linear_convolution result: ', arr)
print('Resultant indexes          : ', result_indexes)
