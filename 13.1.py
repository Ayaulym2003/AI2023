import csv
import math

with open('input_11.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line = 0
    yy = []
    for row in csvFile:
        if line == 0:
            m = int(row[0])
            yy = []
            line += 1
        else:
            if line > m:
                line = 0
            elif line == m:
                yy.append(int(row[0]))
                line = 0
                cntNeg = 0
                cntPos = 0
                total = len(yy)
                for i in range(total):
                    if yy[i] == 0:
                        cntNeg += 1
                    elif yy[i] == 1:
                        cntPos += 1
                print(f"{1 - ((cntPos / total) ** 2 + (cntNeg / total) ** 2):.2f}")
            else:
                yy.append(int(row[0]))
                line += 1





