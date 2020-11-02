import numpy as np
"""Simple Markov chain:
        Initial state: State_1
        Probability of transition:
            State_1 -> State_0: 0.2
            State_0 -> State_1: 0.1
"""
n = 10_000_000
state = np.ones(n)
trans = np.random.uniform(size=n)

for i in range(n-1):
    if state[i]==0:
        if trans[i]<.1:
            state[i+1]=1
        else:
            state[i+1]=0
    elif trans[i]<.2:
            state[i+1]=0
frac_0 = 1 - state.mean()

print(f"Time in State_0: {frac_0:%}")
