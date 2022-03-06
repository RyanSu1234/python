import numpy as np

listA = [2,3,7,4,1,9,5,3,6,0,6,3,3,3,5,9,0,9,7,3,2,2,3,5,6,7,8,9,0,0,8,7,2,2,4,6,7]
index = np.argsort(listA)

print(index)
print(np.array(listA)[index])











