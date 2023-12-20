import numpy as np
import csv

def formula(x, y):
    xTranspose = x.transpose()
    multiplicationOne = np.matmul(xTranspose, x)
    inverseMat = np.linalg.inv(multiplicationOne)
    multiplicationTwo = np.matmul(inverseMat, xTranspose)
    multiplicationThree = np.matmul(multiplicationTwo, y)
    return multiplicationThree

with open('input_5.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')

    for row in csvFile:
        if len(row) == 1:
            x = []
            y = []
            m = int(row[0])
        else:
            x.append(row[:2])
            y.append(row[2])
            if len(x) == m:
                x = np.asarray(x, dtype='float64')
                y = np.asarray(y, dtype='float64')
                myList = list(np.around(np.array(formula(x, y)),2))
                for i in range(len(myList)):
                    if i == len(myList) - 1:
                        print(myList[i])
                    else:
                        print(myList[i], end=",")










