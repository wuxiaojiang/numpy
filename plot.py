import numpy as np
from pylab import*
list1=[1.2,1.5,1.4,1.7,3.4,4.3,8.3]
list2 = [3,5,9,8.9,4.3,6.5,1]
for i in range(len(list1)):
    scatter(list1[i],list2[i],color='#77ffcc')
show()
