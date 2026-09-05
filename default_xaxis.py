#DRAW A LINE WITH DEFAULT X-AXIS STARTING WITH O
import matplotlib.pyplot as plt
import numpy as np
y_points = np.array([3,8,1,10,5,7])
#ypoints = data on y-axis
#marker = marker style
#ls = line style
#lw = line width
#ms = marker size
#mec = marker edge color
#mfc = marker face color
plt.plot(y_points, marker = 'o', ls = '--', lw = 2, ms = 20, mec = 'r', mfc = 'y')
plt.show()