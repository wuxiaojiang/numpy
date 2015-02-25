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
        sqdis = sqdiffmat.sum(axis=1)
        dis = sqdis**0.5
        print sqdis
        print dis
        classcount = {}
        sort = sqdis.argsort()
        print sort
        for i in range(k):
            vote = labels[sort[i]]
            print vote
            classcount[vote] = classcount.get(vote,0)+1
            print classcount
        
