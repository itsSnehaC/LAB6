#HISTOGRAM
import matplotlib.pyplot as plt
import numpy as np
#170: VALUES SHOULD BE CONCENTRATED AT 170
#10: STANDARD DEVIATION
#250: NO OF VALUES
x=np.random.normal(170,10,250)
plt.hist(x)
plt.title("Height of histogram")
plt.xlabel("Height of person in cm")
plt.ylabel("No of persons")
plt.show()