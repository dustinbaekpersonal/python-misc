from copy import copy, deepcopy

original = [[1,2,3],2,3]

print(f"{' setting up ':*^50}")
original_assignment = original
original_copy = copy(original)
original_deepcopy = deepcopy(original)

original[0][0] = 100
original[-1] = -10

# [[100, 2, 3], 2, -10]
print(f"original = {original}")
assert original == [[100, 2, 3], 2, -10]

# [[100, 2, 3], 2, -10]
print(f"assignment = {original_assignment}")
assert original_assignment == [[100, 2, 3], 2, -10] 

# [[100, 2, 3], 2, 3]
print(f"copy = {original_copy}")
assert original_copy == [[100, 2, 3], 2, 3] 

# [[1, 2, 3], 2, 3]
print(f"deepcopy = {original_deepcopy}")
assert original_deepcopy == [[1, 2, 3], 2, 3] 