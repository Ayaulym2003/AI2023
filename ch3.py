import csv
import math

with open('input_3.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvFile:
        col = 0
        y = 0
        if line_count % 2 == 0:
            m = int(row[0])
            th0 = int(row[1])
            th1 = int(row[2])
            line_count += 1
        else:
            while col < m*2:
                y += g(int(row[col]), int(th0), int(th1), int(row[col+1]))
                col += 2
            y = y / (2 * m)
            print(y)
            line_count += 1

