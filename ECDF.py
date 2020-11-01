import numpy as np

class ECDF:
    "Empirical cumulative distribution function"
    def __init__(self, sample):
        self.sample = np.array(sample)
    def __call__(self,x):
        fun = np.vectorize(lambda x: sum(x>=self.sample)/len(self.sample))
        return fun(x)
