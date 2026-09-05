import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50,60,70,80,])
y=np.array([100,120,130,140,150,160,170,180])
plt.plot(x,y,'o:r',mfc='b')
plt.title("Health data of A2 batch",loc='left')
plt.xlabel("Average pulse rate")
plt.ylabel("Burnt calories")
plt.show()