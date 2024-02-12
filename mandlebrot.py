from PIL import Image
import numpy as np

# Mandelbrot calculation
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Image size (pixels), max iterations, and scale to zoom into the Mandelbrot set
width, height = 800, 800
max_iter = 100
scale = 1.0/(width/3)

# Image center point (real, imaginary)
center = (-0.7, 0.0)  # Adjust to focus on different parts of the Mandelbrot set

# Create a new image in RGB mode
img = Image.new('RGB', (width, height), 'black')
pixels = img.load()

# Generate the Mandelbrot image
for x in range(width):
    for y in range(height):
        # Convert pixel coordinate to complex number
        c = complex(center[0] + (x - width/2)*scale, center[1] + (y - height/2)*scale)
        # Compute the number of iterations
        m = mandelbrot(c, max_iter)
        # The color depends on the number of iterations
        color = 255 - int(m * 255 / max_iter)
        # Paint pixel
        pixels[x, y] = (color, color, color)

# Display the image
img.show()

# Optionally, save the image to a file
img.save("mandelbrot.png")
