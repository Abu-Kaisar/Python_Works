import numpy as np

# Declaration and Initialization
# Basic features of Numpy Array
# Topic :-
#           np.array([LIST])
#           .dtype, .ndim, .nbytes,
#           .size, .shape, .itemsize
#


array_1D = np.array([1,2,3,4])
print(array_1D)

array_2D  = np.array([[1,2,3,4], [5,6,7,8]])
print(array_2D)

print("----------array_1D----------")
print("Type: ", array_1D.dtype)
print("Dimension: ", array_1D.ndim)
print("Shape: ", array_1D.shape)
print("Size: ", array_1D.size)
print("Total elements: ", array_1D.itemsize)
print("Memory Size: ", array_1D.nbytes)

print("----------array_2D----------")
print("Type: ", array_2D.dtype)
print("Dimension: ", array_2D.ndim)
print("Shape: ", array_2D.shape)
print("Size: ", array_2D.size)
print("Total elements: ", array_2D.itemsize)
print("Memory Size: ", array_2D.nbytes)
