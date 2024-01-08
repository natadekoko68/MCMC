import random
import time
import numpy as np
import matplotlib.pyplot as plt

n_iter = 10000
step_size = 0.5
random.seed(time.time())
x = 0
n_accept = 0

for i in range(n_iter):
    backup_x = x
    action_init = 1/2 * (x**2)
    dx = random.uniform(-step_size, step_size)
    x += dx
    action_fin = 1/2 * (x**2)

    metropolis = random.random()
    if np.exp(action_init-action_fin) > metropolis:
        n_accept += 1
    else:
        x = backup_x
    print(f"{x:.10f} \n{n_accept/(i+1)*100:.4f} \n")


