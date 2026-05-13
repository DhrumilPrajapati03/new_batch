import numpy as np

l = [1,2,3,4,5,6,-5,-9]
a = np.array(l)
minimum = a.min()
print(minimum)

argmini = a.argmin()
print(argmini)

maximum = a.max()
print(maximum)

argmaxi = a.argmax()
print(argmaxi)

add = a.sum()
print(add)

meann = a.mean()
print(meann)