import numpy as np
from numba import jit
import time
"""Simple Markov chain with a Numba-compiled loop:
        Initial state: State 1
        Probability of transition:
            State 1 -> State 0: 0.2
            State 0 -> State 1: 0.1
"""
n = 100_000_000

state = np.ones(n, dtype=np.int_)
trans = np.random.uniform(size=n)

@jit(nopython=True)
def markov_chain(state, trans):
    for i in range(n-1):
        if state[i]==0:
            if trans[i]<.1:
                state[i+1]=1
            else:
                state[i+1]=0
        elif trans[i]<.2:
                state[i+1]=0
    return state

def run():
    start = time.time()
    state = np.ones(n, dtype=np.int_)
    trans = np.random.uniform(size=n)
    s0 = 1 - markov_chain(state, trans).mean()
    end = time.time()
    t = end - start
    return s0,t

r = run()
print(f"Time in State 0: {r[0]:.4%}. Calc time incl compile: {r[1]:.2}s")

r = run()
print(f"Time in State 0: {r[0]:.4%}. Calc time incl compile: {r[1]:.2}s")

