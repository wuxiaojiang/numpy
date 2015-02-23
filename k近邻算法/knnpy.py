from numpy import*
import operator
import matplotlib.pyplot as plt

class knn():
    def _init_(self):
        pass
    def createdata(self):
        group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels = ['A','A','B','B']
        return group,labels
    def do(self,inx,dataset,labels,k):
        datasetsize = dataset.shape[0]
        #print datasetsize
        st = tile(inx,(datasetsize,1))
        #print st
        diffmat = st-dataset
        #print diffmat
        sqdiffmat = diffmat**2
        sqdis = sqdiffmat**0.5
        #print sqdis
        sort = sqdis.argsort()
        
