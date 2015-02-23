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
        
