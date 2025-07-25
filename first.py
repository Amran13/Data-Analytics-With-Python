import numpy as np;

# arr = numpy.array([1, 2, 3, 4, 5])
zeroDArray = np.array(1)
oneDArray = np.array([1,2,3])
twoDArray = np.array([[1,2,3], [4,5,6]])
threeDArray = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10, 11, 12]]])


# print(zeroDArray, oneDArray, twoDArray, threeDArray)
# print(threeDArray.ndim)
# print(threeDArray)

print(twoDArray.transpose())
