from numpy import *


def step_gradient(current_b, current_m, points, learning_rate):
    b_gradient = 0
    m_gradient = 0

    element = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[0, i]

        b_gradient = -(2 / element) * (y - (current_m * x) + current_b)
        m_gradient = -(2 / element) * x * (y - (current_m * x) + current_b)
    new_b = current_b - (b_gradient * learning_rate)
    new_m = current_m - (m_gradient * learning_rate)


def gradient_descent(points, starting_b, starting_m, learning_rate, number_of_iteration):
    b = starting_b
    m = starting_m

    for i in range(number_of_iteration):
        b, m = step_gradient(b, m, *points, learning_rate)


def compute_error(b, m, points):
    total_error = 0
    for i in range(0, learning_rate):
        x = points[0, i]
        y = points[i, 0]
        total_error += (y - (m * x) + b) ** 2
    return total_error / float(len(points))


def run():
    points = genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    number_of_iteration = 1000
    [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, number_of_iteration)


if __init__ == '__main__':
    run()
