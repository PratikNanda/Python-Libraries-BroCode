import numpy as np


# ---------zeros function ------------
    # array = np.zeros((5))
        # output
        # [0. 0. 0. 0. 0.]
    # array = np.zeros((2,1,6))
        # output
        # [[[0. 0. 0. 0. 0. 0.]]

        #  [[0. 0. 0. 0. 0. 0.]]]

# ---------ones function ------------

    # array = np.ones(8)
        # output
        # [1. 1. 1. 1. 1. 1. 1. 1.]
    # array = np.ones((3,2,2))
        # output[[[1. 1.]
        #   [1. 1.]]

        #  [[1. 1.]
        #   [1. 1.]]

        #  [[1. 1.]
        #   [1. 1.]]]

# ---------full function ------------

    # array = np.full(5,3)
        # output
        # [3 3 3 3 3]
    # array = np.full((2,4,3),3)
        # output
        # [[[3 3 3]
        #   [3 3 3]
        #   [3 3 3]
        #   [3 3 3]]

        #  [[3 3 3]
        #   [3 3 3]
        #   [3 3 3]
        #   [3 3 3]]]

# ---------eye function ------------

    # array = np.eye(4)
        # output
        # [[1. 0. 0. 0.]
        #  [0. 1. 0. 0.]
        #  [0. 0. 1. 0.]
        #  [0. 0. 0. 1.]]
    # array = np.eye(4,2)
        # output
        # [[1. 0.]
        #  [0. 1.]
        #  [0. 0.]
        #  [0. 0.]]

# ---------empty function ------------

    # array = np.empty((2,2,3))
        # output
        # [[[6.23042070e-307 3.56043053e-307 1.60219306e-306]
        #   [2.44763557e-307 1.69119330e-306 1.78022342e-306]]

        #  [[1.05700345e-307 3.11525958e-307 1.78018403e-306]
        #   [2.04722549e-306 8.34450230e-308 1.42404727e-306]]]

# ---------arange function ------------

    # array = np.arange(1,10,2)
        # output
        # [1 3 5 7 9]

    # array = np.arange(0,40,1).reshape(2,20)
        # output
        # [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
        #  [20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]]

# ---------linspace function ------------

    # array = np.linspace(1,10,4)
        # output
        # [ 1.  4.  7. 10.]
    # array = np.linspace(1,100,6)
        # output
        # [  1.   20.8  40.6  60.4  80.2 100. ]

print("# output",f"# {array}", sep="\n")