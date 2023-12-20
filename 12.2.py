import csv
import pprint

def mostCommon(lst):
    flatList = []
    for item in lst:
        flatList.append(item[1])
    return max(set(flatList), key=flatList.count)

with open('input_13.csv', mode ='r') as file:
    csvFile = csv.reader(file, delimiter=',')
    line = 0
    yy = []
    for row in csvFile:
        if line == 0:
            n = int(row[0])
            k = int(row[1])
            yy = []
            line += 1
        else:
            if line > n:
                line = 0
            elif line == n:
                temp = [int(row[0]), int(row[1])]
                yy.append(temp)
                line = 0
                ii = sorted(yy)
                ii = ii[:k]
                print(mostCommon(ii))
            else:
                temp = [int(row[0]), int(row[1])]
                yy.append(temp)
                line += 1
''''' right one:
import csv
from collections import Counter

def knn_sort_and_get_most_frequent_class(file_path):
    results = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        for line in reader:
            # Read the first line to get n and k
            n, k = map(int, line)

            # Read the next n lines to get the pairs
            pairs = [tuple(map(int, next(reader))) for _ in range(n)]

            # Sort the list of tuples by the first element (x)
            sorted_pairs = sorted(pairs, key=lambda pair: pair[0])

            # Get the first k pairs
            first_k_pairs = sorted_pairs[:k]

            # Extract the indices from the first k pairs
            indices = [pair[1] for pair in first_k_pairs]

            # Find the most frequent index in the first k pairs
            most_frequent_index = max(set(indices), key=indices.count)

            results.append(most_frequent_index)

    return results

# Example usage:
file_path = 'input_13.csv'  # Change this to the actual file path
results = knn_sort_and_get_most_frequent_class(file_path)
for i in results:
    print(i, " ")
'''




