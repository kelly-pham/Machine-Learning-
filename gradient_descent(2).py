import numpy as np
import pandas as pd

def run():
    data_points = pd.read_csv("data.csv",delimiter = ",")
    learning_rate = 0.0001
    number_of_iterarion = 1000
    [b,m] = gradient_descent(data_points,b,m,learning_rate,number_of_iteration)

if __init__ == '__main__':
    run()

def gradient_descent(data_points,b,m,learning_rate,number_of_iteration):
    n = len(data_points)
    array = []

    for i in xrange(number_of_iteration):
        predicted = np.dot(data_points,m)
        m = m - learning_rate / m * np.dot((predicted - value),data_points)
        output = compute_output(data_points,b,m )
    return pd.series(array)

def compute_output(data_points,b,m):
    n = len(data_points)
    output = np.square(np.dot(data_points,m) - b).sum() / (2 * m)
    return output

