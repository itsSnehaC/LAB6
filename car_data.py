#CAR DATA---->
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([5,1,15,17,19,4,2,7,3,9,12,13,16])
y1=np.array([99,95,85,86,92,93,98,88,87,89,90,91,94])
x2=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
y2=np.array([100,101,102,103,104,105,106,107,108,109,110,95,70])
plt.subplot(2,3,1)
plt.scatter(x2,y2,color='r')
#MULTIPLE SCATTER PLOT IN A SINGLE PLOT
plt.subplot(2,3,3)
plt.scatter(x1,y1,color='b')
plt.subplot(2,3,3)
plt.scatter(x2,y2,color='r')
plt.show()