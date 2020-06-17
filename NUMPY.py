import numpy as np
def exists(x,lst):

    for y in lst:
        if abs(y-x)<0.0001:
            return True
    return False

randomArray=np.random.rand(20)*20
#print(randomArray)

randomArray=randomArray.reshape(4,5)
print("Initial")
print(randomArray)



#print(randomArray)
maxValues=np.max(randomArray,axis=1)
print('\n')
print("Max Values")
print(maxValues)
print('\n')
print(np.where(randomArray == np.max(randomArray, axis=1).reshape(-1,1), 0, randomArray))


