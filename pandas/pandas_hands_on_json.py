from itertools import combinations

n = 4

for indices in combinations(range(n), 3):
    print(indices)