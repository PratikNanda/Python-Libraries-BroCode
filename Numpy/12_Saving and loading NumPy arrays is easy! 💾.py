import numpy as np

#----Save a numpy array

    # array = np.array([[1, 2, 3],[4, 5, 6]])

    # np.save("data", array)


# ------ Loading a numpy array

# array = np.load("data.npy")
# print(array)


#--------- Save Multiple arrays

# array1 = np.array([[1, 2, 3], [4, 5, 6]])
# array2 = np.array([2022, 2023, 2024, 2025])
# array3 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

# np.savez("data", array1, array2, array3)
# np.savez_compressed("data_compressed", array1, array2, array3)

# print("NumPy data was saved!")

# -- Load Multiple arrays

arrays = np.load("data.npz")

# print(arrays)  #NpzFile 'data.npz' with keys: arr_0, arr_1, arr_2

print(arrays["arr_0"])
print(arrays["arr_1"])
print(arrays["arr_2"])