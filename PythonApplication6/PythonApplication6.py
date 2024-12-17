# ChatGPT

import numpy as np

# Create an array from a Python list
array = np.array([1, 2, 3, 4])
print("Array:", array)

# Create an array of zeros
zeros = np.zeros((2, 3))  # 2x3 matrix of zeros
print("Zeros:\n", zeros)

# Create an array of ones
ones = np.ones((3, 2))  # 3x2 matrix of ones
print("Ones:\n", ones)

# Create a range of numbers
range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print("Range:", range_array)

# Create a linearly spaced array
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced points between 0 and 1
print("Linspace:", linspace)


# Arrays for demonstration
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print("Addition:", a + b)

# Element-wise multiplication
print("Multiplication:", a * b)

# Scalar multiplication
print("Scalar Multiplication:", a * 2)

# Exponentiation
print("Exponentiation:", a ** 2)


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access a specific element
print("Element (1,2):", array[1, 2])  # Row 1, Column 2

# Slice rows and columns
print("First row:", array[0, :])  # First row
print("Second column:", array[:, 1])  # Second column

# Boolean indexing
print("Elements > 5:", array[array > 5])


array = np.array([1, 2, 3, 4, 5])

# Sum of all elements
print("Sum:", np.sum(array))

# Mean (average)
print("Mean:", np.mean(array))

# Standard deviation
print("Standard Deviation:", np.std(array))

# Minimum and maximum
print("Min:", np.min(array))
print("Max:", np.max(array))


# Two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(matrix1, matrix2)  # Or matrix1 @ matrix2
print("Matrix Multiplication:\n", result)

# Transpose
print("Transpose:\n", matrix1.T)

# Determinant
det = np.linalg.det(matrix1)
print("Determinant:", det)

# Inverse
inverse = np.linalg.inv(matrix1)
print("Inverse:\n", inverse)


# Reshape
array = np.array([1, 2, 3, 4, 5, 6])
reshaped = array.reshape(2, 3)  # 2x3 matrix
print("Reshaped:\n", reshaped)

# Concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concat = np.concatenate((a, b))
print("Concatenated:", concat)


# Generate random numbers
random_array = np.random.random((2, 2))  # Uniformly distributed random numbers
print("Random Array:\n", random_array)

# Random integers
rand_ints = np.random.randint(0, 10, (3, 3))  # 3x3 matrix of random integers from 0 to 9
print("Random Integers:\n", rand_ints)

# Normal distribution
normal_dist = np.random.normal(0, 1, 5)  # 5 random numbers from a normal distribution (mean=0, std=1)
print("Normal Distribution:", normal_dist)


# Scalar broadcasting
array = np.array([1, 2, 3])
print("Add scalar:", array + 5)

# Broadcasting with a different shape
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 2, 3])
result = matrix + vector  # The vector is broadcast across rows
print("Broadcasted Addition:\n", result)


array = np.array([3, 1, 4, 1, 5, 9])

# Sort the array
sorted_array = np.sort(array)
print("Sorted Array:", sorted_array)

# Find indices of specific values
indices = np.where(array == 1)
print("Indices of 1:", indices)

# Find the index of the maximum element
max_index = np.argmax(array)
print("Index of Max:", max_index)


array = np.array([1, 2, 3, 4, 5, 6])

# Mask even numbers
mask = array % 2 == 0
print("Even Numbers:", array[mask])

# Set all odd numbers to -1
array[array % 2 != 0] = -1
print("Modified Array:", array)
