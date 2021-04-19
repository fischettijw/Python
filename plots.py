import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
x = np.linspace(55, 99, 100)
print('np.linspace(55, 99, 100)', x)
x = np.arange(10)
print('np.arange(10)', x)
x = np.arange(3.0, 30.0, 5)
print('np.arange(3.0, 30.0, 5)', x)

input("Press Enter to continue...")


x = np.linspace(0, 11, 100)
y = np.linspace(11, 0, 100)
plt.plot(x, y)
plt.show()

plt.figure('Title on the TOP')
plt.plot(x, np.sin(x))
plt.show()

plt.plot(x, np.sin(x), label="sin(x)", color='red')

plt.title('This is the title')
plt.legend(prop={'size': 16}, loc='best')


plt.xlabel('label-x')
plt.ylabel('label-y')
plt.legend(['this is the time'], loc='lower right', fontsize=12)

plt.show()


x1 = [1, 2, 3]

y1 = [4, 5, 6]

x2 = [1, 3, 5]

y2 = [6, 5, 4]

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(["Dataset 1", "Dataset 2"])


plt.show()
