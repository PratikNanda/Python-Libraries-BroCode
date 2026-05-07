import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])


# array[start:end:step]


# ---------Row slicing ---------

# print(array[-4])  # [1 2 3 4] 'print(array[-4])'
# print(array[1])  # [5 6 7 8] 'print(array[-3])'
# print(array[2])  # [ 9 10 11 12] 'print(array[-2])'
# print(array[3])  # [13 14 15 16] 'print(array[-1])'
# print(array[4])  # IndexError: index 4 is out of bounds for axis 0 with size 4


# print(array[0:3]) # output    [[ 1  2  3  4]   Same output for this 'print(array[:-1]) '
#                             #  [ 5  6  7  8]
#                             #  [ 9 10 11 12]]

# print(array[1:4]) # output      [[ 5  6  7  8]
                                # [ 9 10 11 12]
                                # [13 14 15 16]]

# print(array[0:4:2]) # output     [[ 1  2  3  4] same output for this 'print(array[::2])  '
#                                 # [ 9 10 11 12]]

# print(array[::-1])  # output is.  [[13 14 15 16]
                                #  [ 9 10 11 12]
                                #  [ 5  6  7  8]
                                #  [ 1  2  3  4]]

# --------Column Slicing ------------------   

# print(array[:,0]) # [ 1  5  9 13] same for print(array[:,-4])
# print(array[:,1]) # [ 2  6 10 14]  same for print(array[:,-3])
# print(array[:,2]) # [ 3  7 11 15]  same for print(array[:,-2])
# print(array[:,3]) # [ 4  8 12 16]  same for print(array[:,-1])

# print(array[:,0:3]) # output is [[ 1  2  3]
                                # [ 5  6  7]
                                # [ 9 10 11]
                                # [13 14 15]]

# print(array[:,1:4]) # output is [[ 2  3  4]      or print(array[:,1:])
                                #  [ 6  7  8]
                                #  [10 11 12]
                                #  [14 15 16]]

# ---every second column
# print(array[:,::2])
# print(array[:,1::2])
# print(array[:,::-1])
# print(array[:,::-2])

# output of above 4 print statements

# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# [[ 2  4]
#  [ 6  8]
#  [10 12]
#  [14 16]]

# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]
#  [16 15 14 13]]

# [[ 4  2]
#  [ 8  6]
#  [12 10]
#  [16 14]]


# --------Row and column Slicing ------

print(array[:2,:2])
# output 
# [[1 2]
#  [5 6]]

print(array[:2,2:])
# output 
# [[3 4]
#  [7 8]]

print(array[2:,:2])
# output 
# [[ 9 10]
#  [13 14]]


print(array[2:,2:].reshape(1,-1))
# output 
# [[11 12 15 16]]