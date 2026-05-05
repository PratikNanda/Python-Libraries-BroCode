import numpy as np

array1 = np.array('A') # output: array is A, dimension is 0, shape is ()
array2 = np.array(['A', 'B', 'C']) # output: array is ['A' 'B' 'C'], dimension is 1, shape is (3,)
array3 = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]) # output: array is [['A' 'B' 'C']
                                                                                        # ['D' 'E' 'F']
                                                                                        # ['G' 'H' 'I']], dimension is 2, shape is (3, 3)    
                                                                                            
array4 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]]) # output: array is [[['A' 'B' 'C']
                                                                                        #   ['D' 'E' 'F']
                                                                                        #   ['G' 'H' 'I']]

                                                                                        #  [['J' 'K' 'L']
                                                                                        #   ['M' 'N' 'O']
                                                                                        #   ['P' 'Q' 'R']]], dimension is 3, shape is (2, 3, 3)

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]]) # output: array is [[['A' 'B' 'C']
                                                                                            #   ['D' 'E' 'F']
                                                                                            #   ['G' 'H' 'I']]

                                                                                            #  [['J' 'K' 'L']
                                                                                            #   ['M' 'N' 'O']
                                                                                            #   ['P' 'Q' 'R']]

                                                                                            #  [['S' 'T' 'U']
                                                                                            #   ['V' 'W' 'X']
                                                                                            #   ['Y' 'Z' ' ']]], dimension is 3, shape is (3, 3, 3)


# print(array)
# print(array.ndim)
# print(array.shape)

# print(f"array is {array}, dimension is {array.ndim}, shape is {array.shape}")


# Chain Indexing
# print(array4[0][0][0]) # output: A

# Multi Indexing
# print(array4[0,0,0]) # output: A


# word = array[1,2,0] + array[1,2,2] + array[0,0,0] + array[2,0,1] + array[0,2,2] + array[1,0,1] # output: PRATIK
word = array[1,1,1] + array[2,0,2] + array[1,1,0] + array[1,2,0] + array[2,2,0] # output: NUMPY

print(word)

