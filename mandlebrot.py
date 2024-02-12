import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import colorsys


# Mandelbrot calculation function

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n, False  # Not in the Mandelbrot set
        z = z*z + c
    return max_iter, True  # In the Mandelbrot set


def generate_mandelbrot(center, scale, size, max_iter):
    width, height = size
    img = Image.new('RGB', size)
    draw = ImageDraw.Draw(img)

    for x in range(width):
        for y in range(height):
            re = center[0] + (x - width / 2) / scale
            im = center[1] + (y - height / 2) / scale
            c = complex(re, im)
            m, in_set = mandelbrot(c, max_iter)

            if in_set:
                color = (0, 0, 0)  # Black for points in the set
            else:
                # Generate a color based on the iteration count
                hue = m / max_iter
                saturation = 1
                value = m < max_iter
                r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
                color = (int(r * 255), int(g * 255), int(b * 255))

            draw.point([x, y], color)

    return img




# Function to update the image based on the zoom level and center
def update_image(event=None, zoom_in=True):
    global center, scale, max_iter

    if event:
        # Calculate the new center based on the click position
        x, y = event.x, event.y
        center = (center[0] + (x - size[0] / 2) / scale,
                  center[1] + (y - size[1] / 2) / scale)

    # Adjust the scale for zooming
    if zoom_in:
        scale *= 2
    else:
        scale /= 2

    img = generate_mandelbrot(center, scale, size, max_iter)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(size[0] / 2, size[1] / 2, image=tk_img)
    canvas.image = tk_img  # Keep a reference!

# Initial parameters
center = (-0.7, 0.0)  # Center of the view
scale = 400  # Scale factor
size = (800, 800)  # Size of the Tkinter window
max_iter = 100  # Maximum iterations

# Setup Tkinter window
window = tk.Tk()
window.title("Interactive Mandelbrot Set")

canvas = tk.Canvas(window, width=size[0], height=size[1])
canvas.pack()

# Bind mouse events to the canvas
canvas.bind("<Button-1>", lambda event: update_image(event, zoom_in=True))  # Left click to zoom in
canvas.bind("<Button-3>", lambda event: update_image(event, zoom_in=False))  # Right click to zoom out

# Display the initial Mandelbrot set
update_image()

window.mainloop()
