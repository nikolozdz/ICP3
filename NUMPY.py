import numpy as np

randomArray=np.random.rand(20)*20
#print(randomArray)

randomArray=randomArray.reshape(4,5)

print(randomArray)



#print(randomArray)







print(np.where(np.max(randomArray, axis = 1)))

#np.where(np.max(a2d, axis = 1),np.array, 0)
#print(np.where(np.max(a2d, axis = 1),np.array, 0))
