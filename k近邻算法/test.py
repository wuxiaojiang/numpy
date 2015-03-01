import knnpy
c = knnpy.knn()
data,lab = c.createdata()
b = c.do([0.7,0.6],data,lab,3)
print b
