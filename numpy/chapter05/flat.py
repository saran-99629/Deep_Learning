import numpy as np 
ar = np.array([1,2,3,4,5,6,7,8,9,12,12,13])
print(ar.shape)
reshape = np.reshape(ar, (4,3))
print(reshape)
flaten = reshape.flatten()
print(flaten)