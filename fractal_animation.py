import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the mandelbrot function
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate the fractal image
def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

# Define the plot limits and resolution
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 320, 240  # Lower resolution for better performance
max_iter = 128  # Reduce the number of iterations

# Create a figure and axis
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)

# Initialize the fractal image
x, y, fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
img = ax.imshow(fractal.T, extent=[xmin, xmax, ymin, ymax], cmap='hot', interpolation='bilinear')

def update(frame):
    global xmin, xmax, ymin, ymax
    zoom_factor = 0.95  # Adjust zoom factor for smoother animation
    xmin, xmax = zoom_factor * xmin, zoom_factor * xmax
    ymin, ymax = zoom_factor * ymin, zoom_factor * ymax
    x, y, fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
    img.set_data(fractal.T)
    img.set_extent([xmin, xmax, ymin, ymax])
    return img,

ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)
plt.show()