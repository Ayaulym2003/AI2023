import csv
import math

def mini(we):
    minVal = int(we[0])
    for i in range(len(we)):
        if int(we[i]) < minVal:
            minVal = int(we[i])
    return minVal

def maxi(we):
    maxVal = int(we[0])
    for i in range(len(we)):
        if int(we[i]) > maxVal:
            maxVal = int(we[i])
    return maxVal

def mu(we):
    mua = 0
    for i in range(len(we)):
        mua += int(we[i])
    return mua/len(we)

with open('input_4.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvFile:
        v = []
        x = 0
        if line_count % 2 == 0:
            m = int(row[0])
            line_count += 1
        else:
            for i in range(len(row)):
                x = (int(row[i]) - mu(row)) / (maxi(row) - mini(row) + 1)
                v.append(x)
            for i in range(len(v)):
                if i == len(v) - 1 :
                    print(round(v[i], 2))
                else:
                    print(round(v[i], 2), end=",")
            line_count += 1


