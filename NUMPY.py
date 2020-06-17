import numpy as np

randomArray=np.random.rand(20)*20
print("Initial")
print(randomArray)
print('\n')
randomArray=randomArray.reshape(4,5)
print("After reshape")
print(randomArray)
print('\n')
print('after replacing max values')
print(np.where(randomArray == np.max(randomArray, axis=1).reshape(-1,1), 0, randomArray))


