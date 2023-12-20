
import csv
import math

def g(hValue):
    return 1 / (1 + math.exp(-hValue))

a = [[2, 2, 1],
     [3, 4, 4],
     [5, 1, -1]]

b = [[1, 1, 1],
     [2, 2, 2],
     [0, 0, -1]]

c = [[1, 4],
     [5, 6],
     [0, 2]]

with open('input_8.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvFile:
        x0 = 1
        x1 = int(row[0])
        x2 = int(row[1])

        a1 = g(x0*a[0][0]+x1*a[1][0]+x2*a[2][0])
        a2 = g(x0*a[0][1]+x1*a[1][1]+x2*a[2][1])
        a3 = g(x0*a[0][2]+x1*a[1][2]+x2*a[2][2])

        b1 = g(a1*b[0][0]+a2*b[1][0]+a3*b[2][0])
        b2 = g(a1*b[0][1]+a2*b[1][1]+a3*b[2][1])
        b3 = g(a1*b[0][2]+a2*b[1][2]+a3*b[2][2])

        c1 = g(b1*c[0][0]+b2*c[1][0]+b3*c[2][0])
        c2 = g(b1*c[0][1]+b2*c[1][1]+b3*c[2][1])

        print(f'{round(c1):.2f}', end=",")
        print(f'{(math.ceil(c2*100)/100):.2f}')



