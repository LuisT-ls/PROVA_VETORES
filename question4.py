import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

print((a1==a2).all())
print((a3==a2).all())
