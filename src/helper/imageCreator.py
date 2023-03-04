from PIL import Image, ImageDraw
import math
import cv2
import numpy as np

# Set the size of the color wheel and the radius of the circle
size = 4000
radius = size / 2
offset = size / 8

# Set the size for the rectangle
h = 720
w = 5

def createBars(colors):
    bars = []
    print('creating bar')
    for rgb in colors:
        bar = np.zeros((h, w, 3), np.uint8)
        bar[:] = rgb
        bars.append(bar)
    img_bar = np.hstack(bars)
    cv2.imwrite('output/bar.png', img_bar)
    print('bar completed')

def createCircle(colors):
    print('creating circle')
    # Create an array of RGB color values

    # Create a new image with a transparent background
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # Create a draw object
    draw = ImageDraw.Draw(image)
    # Draw the color wheel
    for y in range(size):
        for x in range(size):
            # Calculate the distance from the pixel to the center of the circle
            distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)
            
            # Only draw the pixel if it's inside the circle
            if offset <= distance <= radius:
                # Calculate the angle of the pixel relative to the center of the circle
                angle = math.atan2(y - radius, x - radius)
                
                # Map the angle to an index in the array of colors
                index = round(angle / (2 * math.pi / len(colors)))
                color = colors[index % len(colors)]
                
                # Calculate the saturation based on the distance from the center of the circle
                # s = distance / radius
                s= 1
                
                # Convert the color and saturation to RGB color values
                r = int(color[0] * s)
                g = int(color[1] * s)
                b = int(color[2] * s)
                
                # Draw the pixel with the calculated color
                draw.point((x, y), (r, g, b))

    # Save the image
    # image.show()
    image.save('./output/circle.png')
    print('circle completed')
