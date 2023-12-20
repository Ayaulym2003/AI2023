import csv
import math

with open('input_11.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    for row in csvFile:
        print(round(math.pow(math.pow(float(row[0]) - float(row[2]), 2) + math.pow(float(row[1]) - float(row[3]), 2), 0.5), 2))











