import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy
list1=[1.2,1.5,1.4,1.7,3.4,4.3,8.3]
list2 = [3,5,9,8.9,4.3,6.5,1]
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(list1)):
    ax.scatter(list1[i],list2[i])
plt.show()
