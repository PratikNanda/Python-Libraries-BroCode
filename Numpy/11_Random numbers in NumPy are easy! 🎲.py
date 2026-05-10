import numpy as np


# -----------random integer
    # rng = np.random.default_rng()

    # print(rng.integers(1,7))
    # print(rng.integers(low = 1, high = 100))
    # print(rng.integers(low = 1, high = 100, size=(2,2)))


# --------random uniform

    # np.random.seed(seed = 1) # only 1 output everytime

    # print(np.random.uniform())
    # print(np.random.uniform(low = -1, high = 1))
    # print(np.random.uniform(low = -1, high = 1, size = (1,4)))

# ------- Shuffling the array

rng = np.random.default_rng()

# array = np.array([1,2,3,4,5,6])

# print(array)
# rng.shuffle(array)
# print(array)

# -----------random choice

fruits = np.array(["Apple", "Orange", "Banana", "Coconut", "Pineapple"])

# fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
print(rng.choice(fruits, size=(3, 3)))