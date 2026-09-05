import matplotlib.pyplot as plt
import numpy as np
x1=np.array([5,1,15,17,19,4,2,7,3,9,12,13,16])
y1=np.array([99,95,85,86,92,93,98,88,87,89,90,91,94])
#CAR DATA
#random---->numpy function to generate random data
#radiant---->numpy function to generate random integer
#100---->random integer from 0 to 99
#size(13)---->the random array will be of size 13
color=np.random.randint(100,size=(13))
size=2*np.random.randint(100,size=(13))
plt.subplot(1,3,1)
plt.scatter(x1,y1,c=color,s=size,alpha=0.3,cmap='nipy_spectral')
plt.show()
