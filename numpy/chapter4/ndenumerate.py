import numpy as np  
ar = np.array([
    [1,2,3],
    [1,2,4]
])
for i, a in np.ndenumerate(ar):
    print(i,a)