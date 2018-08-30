import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend(numpoints = .5)
plt.show()
