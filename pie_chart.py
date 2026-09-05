#PIE CHART
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["Apple","Banana","Cherry","Dragonfruit"]
plt.subplot(3,2,1)
plt.pie(y,labels=mylabels)
plt.subplot(3,2,2)
plt.pie(y,labels=mylabels,startangle=90)
plt.subplot(3,2,3)
myexplode=[0.2,0,0,0]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.subplot(3,2,4)
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.subplot(3,2,5)
mycolor={"black","red","blue"}
plt.pie(y,labels=mylabels,colors=mycolor)
plt.subplot(3,2,6)
plt.pie(y,labels=mylabels)
plt.legend(title="Four Fruits")
plt.show()