import csv
import math

def h(x, thetaZero, thetaOne):
    return x * thetaOne + thetaZero

def g(x, thetaZero, thetaOne, w):
    return pow(x * thetaOne + thetaZero - w, 2)

with open('input_7.csv', mode ='r') as file:
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
                y += g(int(row[col]), int(th0), int(th1), int(row[col+1]))
                col += 2
            y = (y + lambd * (pow(th0, 2) + pow(th1, 2)))/ (2 * m)
            print(y)
            line_count += 1

