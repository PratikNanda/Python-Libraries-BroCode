# reshape() = Changes the shape of an array
#                      w/o altering its underlying data
#                      array.reshape(rows, columns) or array.reshape(layers, rows, columns)

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # array is [ 1  2  3  4  5  6  7  8  9 10 11 12] and shape is (12,)

array = array.reshape(6,2) # array is [[ 1  2]
                                    #  [ 3  4]
                                    #  [ 5  6]
                                    #  [ 7  8]
                                    #  [ 9 10]
                                    #  [11 12]] and shape is (6, 2)

array = array.reshape(4,3) #    array is [[ 1  2  3]
                                        # [ 4  5  6]
                                        # [ 7  8  9]
                                        # [10 11 12]] and shape is (4, 3)

array = array.reshape(3,2,2) # array is [[[ 1  2]
                                        #   [ 3  4]]

                                        #  [[ 5  6]
                                        #   [ 7  8]]

                                        #  [[ 9 10]
                                        #   [11 12]]] and shape is (3, 2, 2)

print(f"array is {array} and shape is {array.shape}")

# array = array.reshape(2, 6)
# array = array.reshape(3, 4)
# # array = array.reshape(4, 4) # Too many elements
# # array = array.reshape(2, 4) # Too few elements
# array = array.reshape(4, 3)
# array = array.reshape(2, 2, 3) # 3D
# array = array.reshape(3, 2, 2) # 3D

# # -1 NumPy will automatically infer the correct size for that dimension