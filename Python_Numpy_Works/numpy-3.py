import numpy as np

# Types of array
# 0,1 more, float etc


print("Zero valued array_1D")
print(np.zeros(5))
print("\nZero valued array_2D")
print(np.zeros((3,5)))
print("\nZero valued array_3D")
print(np.zeros((2,3,5)))

print("One valued array_1D")
print(np.ones(4))
print("\nOne valued array_2D")
print(np.ones((2,4)))
print("\nOne valued array_3D")
print(np.ones((3,2,4)))

print("\nRandom valued array_nD")
print(np.full((2,3,4),6))

print("\nRandom valued array_nD")
print(np.full((2,3,4),6))
print("\nRandom float valued array_nD")
print(np.random.rand(3,2,2))
print("\nRandom int valued array_nD")
print(np.random.randint(4, size=(2,3,4)))
print("\nIDENTITY MATRIX")
print(np.identity(5))
