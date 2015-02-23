import knnpy
c = knnpy.knn()
data,lab = c.createdata()
c.do([1.2,1.3],data,lab,7)
