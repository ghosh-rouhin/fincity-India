# Importing the numpy module
import numpy as np

# Defining the function/method of returning the transpose
def transpose_Array(arr,axis):
    # Checking if the dimension of the array is 1D or above
    if len(arr.shape)==1:
        return "Cannot transpose an 1D array."
    
    # Returning the transpose of array
    return np.transpose(arr,axis)


arr = [[[1,2,3],[3,4,5]],[[1,2,3],[3,4,5]]] #Defining the Array
axis = [2,0,1] # Defining the axis

# Converting the list into numpy array
arr = np.array(arr)

# Printing the transpose.
print(transpose_Array(arr,axis))
