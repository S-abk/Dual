import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Number of Fibonacci numbers
num_points = 30

# Generate Fibonacci sequence
fib_seq = fibonacci(num_points)

# Prepare the 3D spiral coordinates
x = [np.cos(i) * fib_seq[i] for i in range(num_points)]
y = [np.sin(i) * fib_seq[i] for i in range(num_points)]
z = [i * 3 for i in range(num_points)]  # scale height to spread the spiral upwards

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=fib_seq, cmap='viridis', s=fib_seq)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Fibonacci Spiral')

plt.show()
