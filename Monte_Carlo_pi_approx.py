import numpy as np
import quantecon as qe

def approx_pi():
    n = 10000000
    a = np.random.uniform(size=(2,n))
    b = np.sqrt(np.sum(a**2, axis=0))
    appr_pi = 4*np.mean(b < 1)
    error = 100*np.absolute(np.pi - appr_pi)/np.pi
    return appr_pi, error, n

qe.tic()
pi_a = approx_pi()
qe.toc()

print(f"Approx pi: {pi_a[0]}, iterations: {pi_a[2]:.2E}, error: {pi_a[1]:.2E}%")
