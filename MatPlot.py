import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
w = np.linspace(0, 20, 200)
print(w)
plt.plot(w, np.sin(w))       # Plot the sine of each x point
plt.show()                   # Display the plot


x = list(range(0, 10))
y = list(range(-10, 0))

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, y)
plt.show()
