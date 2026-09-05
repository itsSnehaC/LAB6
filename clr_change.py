import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50,60,70,80,])
y=np.array([100,120,130,140,150,160,170,180])
plt.grid(axis='x')
plt.grid(axis='y')
plt.grid(color='green',linestyle='--',linewidth=0.5)
plt.show()