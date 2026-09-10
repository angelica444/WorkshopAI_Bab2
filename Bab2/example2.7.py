#Example
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y1 = 3 * x + 4
y2 = 2 * (x**2) + 1
y3 = (x**3) + 9

plt.plot(x, y1, color='blue', label='y = 3x + 4')
plt.plot(x, y2, color='green', label='y = 2x^2 + 1')
plt.plot(x, y3, color='red', label='y = x^3 + 9')

plt.title('Plot Fungsi Matematika')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()