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