import numpy as np
from numba import jit
"""Simple Markov chain:
        Initial state: State 1
        Probability of transition:
            State 1 -> State 0: 0.2
            State 0 -> State 1: 0.1
"""
n = 1_000_000_000
@jit
def markov_chain():
    state = np.ones(n, dtype=np.int_)
    trans = np.random.uniform(size=n)

    for i in range(n-1):
        if state[i]==0:
            if trans[i]<.1:
                state[i+1]=1
            else:
                state[i+1]=0
        elif trans[i]<.2:
                state[i+1]=0
    return 1 - state.mean()

print(f"Time in State 0: {markov_chain():%}")
