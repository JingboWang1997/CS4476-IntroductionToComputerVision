import numpy as np
import matplotlib.pyplot as plt

A = np.load('./inputAPS0Q1.npy')

# a)
Temp = A.copy()
array = Temp.reshape((10000,))
array.sort()
array = array[::-1]
plt.plot(array)
plt.ylabel("Intensity")
plt.show()

# b)
plt.hist(A, bins=20)
plt.show()

# c)
X = A[50:, 0:50]
# np.save('./outputXPS0Q1.npy', X)
plt.imshow(X, interpolation='none')
plt.colorbar()
plt.show()

# d)
Y = A.copy()
mean = np.mean(Y)
Y -= mean
# np.save('./outputYPS0Q1.npy', Y)
plt.imshow(Y, interpolation='none')
plt.colorbar()
plt.show()

# e)
Z = np.zeros((100, 100, 3))
mean = np.mean(A)
locate = np.where(A > mean)
row = locate[0]
column = locate[1]
for i in range(row.size):
    r = row[i]
    c = column[i]
    Z[r][c][0] = 1
plt.imshow(Z, interpolation='none')
# plt.savefig('./outputZPS0Q1.png')
plt.show()
