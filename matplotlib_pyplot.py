
import matplotlib.pyplot as plt
import numpy as np

# Draw a line in a diagram from position (0,0) to position (10,15):

x = np.array([0, 10])
y = np.array([0, 15])

plt.plot(x, y)
print(plt.show())