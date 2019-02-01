"""Class perceptron"""
import numpy as np
import pandas as pd
import random

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=random.random(), epochs=100):
        self.W = np.random.randint(2,size=3)
        # add one for bias
        self.epochs = epochs
        self.lr = lr
    
    def activation_fn(self, x):
        return 1 if x >= 0 else 0
 
    def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a
 
    def fit(self, X, d):
        l = []
        for _ in range(self.epochs):
            el,pe = [], []
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(x)
                e = d[i] - y
                el = np.append(el,e)
                self.W = self.W + self.lr * e * x
                #print("iter:{}\tX:{}\ty':{}\ty:{}\tW:{}\tel:{}".format(_,X[i],y,d[i],self.W,el))
                l.append({'iter': _,'X': list(X[i]),'y': int(d[i]),'y^': y,'W': list(self.W),'el': list(el), 'MAE': None})
            pe = sum([abs(i) for i in el])/len(el) #MeanAbsoluteError
            l.append({'iter': _,'X': None,'y': None,'y^': None,'W': None,'el': None, 'MAE': pe})
            if pe == 0:
                df = pd.DataFrame(l)
                return df
                break