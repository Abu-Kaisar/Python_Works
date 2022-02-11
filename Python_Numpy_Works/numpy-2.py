import numpy as np

# Slicing and Indexing
# Finding Specific Data

print("----------array_1D----------")
array_1D = np.array([1,2,3,4])
print(array_1D)

print("\n----------array_2D----------")
array_2D  = np.array([[1,2,3,4], [5,6,7,8]])
print(array_2D)

print("\n----------array_3D----------")
array_3D = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(array_3D)


#first element of array_1D
print("first element of array_1D")
print(array_1D[0])
#second element of array_2D
print("second element of array_2D")
print(array_2D[0,1])
#second row of array_2D
print("second row of array_2D")
print(array_2D[1,:])
#second coloumn of array_2D
print("second coloumn of array_2D")
print(array_2D[:,1])
#third element of array_3D
print("third element of array_3D")
print(array_3D[0,0,2])
#third row of array_3D
print("thirdrow of array_3D")
print(array_3D[1,0,:])
#third coloumn of array_2D
print("third coloumn of array_2D")
print(array_3D[:,:,2])


