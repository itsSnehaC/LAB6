import matplotlib.pyplot as plt
import numpy as np
x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.bar(x,y,width=0.1)
plt.subplot(2,1,2)
plt.barh(x,y,color='red',height=0.5)
plt.show()