t = (10,20, True, "Hello", 3.14) #immutable
print(type(t))
t[2]  = False
print(t)
   
# l = [10,20, True, "Hello", 3.14] #mutable
# l[2] = False
# print(l)

L = (i for i in range(-20,20) if i%2==0)
print(tuple(L))