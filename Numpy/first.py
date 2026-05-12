import numpy as np

# a = np.array([10,20,30,40,50])
# print(a)
# print(type(a))

# b = np.array((10,30,50,70))
# print(b)

# c = np.array({1,1,1,1,3,4,5,6,8})
# print(c)

# functions
# arange(start, end, step)
# k = np.arange(1,11,2)
# print(k)

# zeros
# n = np.zeros((2,2,2))
# print(n)

# # ones
# l = np.ones((2,2,2))
# print(l)

# eye(n)
# e = np.eye(6)
# print(e)
# print(e.shape)

# linespace (start, stop, nums of elements)
# s = np.linspace(1,2,20)
# print(s)

# shape
# e = np.eye(4)
# print(e)
# print(e.shape)

# reshape
re1 = np.random.randint(1,100,15)
print(re1)
re2 = re1.reshape(5,3)
print(re2)