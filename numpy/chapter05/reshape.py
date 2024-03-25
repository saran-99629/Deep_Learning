import numpy as np  
# a=[]
# for i in range(0,12):
#     a.append(int(input('value=')))
ar = np.array([1,2,3,4,5,6,7,8,9,0,11,12])
print(np.shape(ar))
ar1 = np.reshape(ar, (3,4))
ar2 = np.reshape(ar, (2,6))
print(ar1)
print(ar2)