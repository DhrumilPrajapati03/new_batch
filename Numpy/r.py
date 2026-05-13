import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)

b = np.random.rand()
print(b)

b1 = np.random.randn()
print(b1)

# c = np.random.randint(1,100,10)
# print(c)
# d = c.reshape(2,5)
# print(d)

# N-dimensional array
k = np.array([[1,2,3,4],[5,6,7,8]],ndmin=6)
print(k)
print(k.shape)
print(k.ndim)