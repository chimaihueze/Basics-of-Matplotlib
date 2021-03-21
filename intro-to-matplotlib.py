# What is Matplotlib?
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

import matplotlib

print(matplotlib.__version__)

# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt

# Now the Pyplot package can be referred to as plt.

import numpy as np

x = np.array([0, 10])
y = np.array([0, 15])

plt.plot(x, y)
print(plt.show())