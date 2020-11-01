import numpy as np

class DiscreteRV:
    """
    Discrete random variable in [0,1] with the distribution
    provided in the initialization list q,
    where sum(q) == 1.
    """
    def __init__(self,q):
        self.dist = np.array(q).cumsum()    
    def __call__(self,k):
        u = np.random.uniform(size=k)
        return self.dist.searchsorted(u)
    def draw(self,k=1):
        return self(k)
