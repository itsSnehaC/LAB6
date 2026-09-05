#SET FONT PROPERTIES OF THE GRAPH
import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50,60,70,80,])
y=np.array([100,120,130,140,150,160,170,180])
plt.plot(x,y,'o:r',mfc='b')
plt.title("Health data of A2 batch",loc='left')
plt.xlabel("Average pulse rate")
plt.ylabel("Burnt calories")
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
plt.plot(x,y,'o:r',mfc='b')
plt.title("Health data of A2 batch",loc='left',fontdict=font1)
plt.xlabel("Average pulse rate",fontdict=font2)
plt.ylabel("Burnt calories",fontdict=font2)
plt.grid()
plt.show()