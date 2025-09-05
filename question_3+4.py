# Numpy Arrays
import numpy as np # Imports numpy library
arr = np.random.randint(1,100, size = (5,5)) # Creates a 5x5 array with random integers between 1 and 100
print("Original Array")
print(arr)
print("")
print("")
print("Minimum Value = ",arr.min()) # Finds minimum entry in the array
print("Maximum Value = ",arr.max()) # Finds maximum entry in the array
print("Mean Value = ",arr.mean()) # Finds mean of all entries in the array
print("")
print("")
norm = (arr - arr.min())/(arr.max() - arr.min()) # Normalises array such that minimum entry is assigned 0 and maximum entry is assigned 1
 #norm = arr/100
print("Normalised Array")
print(norm)
print("")
print("")
flat = norm.flatten() # Flattens array into a 1D array
sort = np.sort(flat) # Sorts the flattened array in ascending order
print("Sorted Flat Array") 
print(sort)
print("")
print("")
sliced = arr[1:4, 1:4] # Slices 
print("Sliced Array")
print(sliced)
print("")
print("")
row = sliced[0,:]
column = sliced[:,2]
product = np.dot(row,column)
print("Dot Product = ", product)