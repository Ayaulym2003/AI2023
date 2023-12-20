import csv
import math

def g(hValue):
    return 1 / (1 + math.exp(-hValue))

def h(x, theta0, theta1):
    totalSum = x * theta1 + theta0
    return totalSum

with open('input_6.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvFile:
        if len(row) == 1:
            x = 0
            theta0 = 0
            theta1 = 0
            m = int(row[0])
        else:
            x = int(row[0])
            theta0 = int(row[1])
            theta1 = int(row[2])
            print(round(g(h(x, theta0, theta1)), 2))

