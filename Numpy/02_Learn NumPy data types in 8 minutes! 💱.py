# dtype = Keyword argument that tells NumPy what kind of values are stored in an array
#               Otherwise NumPy guesses the best data type based on your data
#               Manually setting dtype improves performance
#               & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_, <U#)
# object (object_)

# int8 = -128 to 127
# int16 = –32,768 to 32,767
# int32 = –2,147,483,648 to 2,147,483,647
# int64 = –9.22e18 to 9.22e18

# float16 = ~3-4 decimal digit precision
# float32 = ~7-8 decimal digit precision
# float64 = ~15-17 decimal digit precision


import numpy as np

array = np.array([1, 2, 3, 4, 5]) #[1 2 3 4 5] int64 40 bytes
array = np.array([1, 2, 3, 4, 5], dtype=np.int32) #[[1 2 3 4 5] int32 20 bytes
array = np.array([1, 2, 3, 4, 5], dtype=np.int16) #[1 2 3 4 5] int16 10 bytes
# array = np.array([125, 127, 129], dtype=np.int8) #OverflowError: Python integer 129 out of bounds for int8

array = np.array([1, 2, 3, 4, 5], dtype=np.float64) #[1. 2. 3. 4. 5.] float64 40 bytes
array = np.array([1, 2, 3, 4, 5], dtype=np.float32) #[1. 2. 3. 4. 5.] float32 20 bytes
array = np.array([1, 2, 3, 4, 5], dtype=np.float16) #[1. 2. 3. 4. 5.] float16 10 bytes

array = np.array([1,2,3,4,0], dtype=np.bool_) # [ True  True  True  True False] bool 5 bytes -----bool_ is numpy not bool(python default) 

array = np.array([1, 2, 3, 4, 5], dtype=np.str_) #['1' '2' '3' '4' '5'] <U1 20 bytes
array = np.array([10, 20, 30, 40, 50], dtype=np.str_) #['10' '20' '30' '40' '50'] <U2 40 bytes
array = np.array(["apple", "orange", "banana"], dtype=np.str_) #['apple' 'orange' 'banana'] <U6 72 bytes
array = np.array(["apple", "orange", "banana"], dtype="<U4") #['appl' 'oran' 'bana'] <U4 48 bytes

array = np.array([1, 2, 3, 4, 5], dtype=np.object_) #[1 2 3 4 5] object 40 bytes
array = np.array([1, 2.4, False, "Four", 5], dtype=np.object_) #[1 2.4 False 'Four' 5] object 40 bytes

#-------Converting----------

array = np.array([1, 2, 3, 4, 5])
array = array.astype(np.float16) #[1. 2. 3. 4. 5.] float16 10 bytes

array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
array = array.astype(np.int16) #[1 2 3 4 5] int16 10 bytes


print(array,end=" ")
print(array.dtype, end=" ")
print(f"{array.nbytes} bytes")
