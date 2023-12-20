import csv
import math

def g(hValue):
    return 1 / (1 + math.exp(-hValue))

def f(x, theta0, theta1):
    totalSum = x * theta1 + theta0
    return totalSum

def h(x, thetaZero, thetaOne, w):
    return -w * math.log2(g(f(x, thetaZero, thetaOne))) - (1 - w) * math.log2(1 - g(f(x, thetaZero, thetaOne)))

with open('input_8.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvFile:
        col = 0
        y = 0
        if line_count % 2 == 0:
            m = int(row[0])
            th0 = int(row[1])
            th1 = int(row[2])
            lambd = float(row[3])
            line_count += 1
        else:
            while col < m*2:
                y += h(int(row[col]), int(th0), int(th1), int(row[col+1]))
                col += 2
            y = y / (2 * m)
            t = lambd / (2 * m) * (pow(th0, 2) + pow(th1, 2))
            r = y + t
            print(round(r, 2))
            line_count += 1