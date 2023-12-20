import csv
import math

def g(hValue):
    return 1 / (1 + math.exp(-hValue))

def classificationСostFunction(yTrue, yPred, a, b, c, regularizationRate):

    totalSum = 0
    sumOfWeights = 0
    m = 1

    totalSum += -1 * yTrue * math.log2(yPred) - (1 - yTrue) * math.log2(1 - yPred)

    for l in range(len(a)):
        sumOfWeights += pow(a[l], 2)
    for l in range(len(b)):
        sumOfWeights += pow(b[l], 2)
    for l in range(len(c)):
        sumOfWeights += pow(c[l], 2)

    return totalSum / (2 * m) + regularizationRate * sumOfWeights


with open('input_11.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line_count = 0
    a = []
    b = []
    c = []
    lambdao = 0
    for row in csvFile:
        if line_count % 2 == 0:
            x0 = 1
            x1 = float(row[0])
            x2 = float(row[1])
            y = float(row[2])
            line_count += 1
        else:
            a = []
            b = []
            c = []
            for i in range(0, 3):
                a.append(float(row[i]))
            for i in range(3, 6):
                b.append(float(row[i]))
            for i in range(6, 9):
                c.append(float(row[i]))
            lambdao = float(row[9])
            line_count += 1
            a1 = g(x0*a[0] + x1*a[1] + x2*a[2])
            a2 = g(x0*b[0] + x1*b[1] + x2*b[2])

            c2 = g(1*c[0] + a1*c[1] + a2*c[2])
            c3 = classificationСostFunction(y, c2, a, b, c, lambdao)
            print(round(c3, 2))











