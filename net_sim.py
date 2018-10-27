import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import util


scores = [0] * 100

# testing against uniform distribution
all_traps = range(1, 100)
util.sim(all_traps, scores, 10000)
#print(scores)

# testing against multiples of 5
all_traps = range(5, 100, 5)
util.sim(all_traps, scores, 10000)
#print(scores)

# testing against multiples of 10
all_traps = range(10, 100, 10)
util.sim(all_traps, scores, 10000)
#print(scores)

# testing against multiples of 25
all_traps = range(25, 100, 25)
util.sim(all_traps, scores, 10000)

for i in range(0, 100):
    print(i, scores[i])

plt.plot(scores)
plt.savefig("sim.png")
