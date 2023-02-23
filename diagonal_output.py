from PIL import Image, ImageDraw
import colorsys
import math

# Set the size of the color wheel and the radius of the circle
size = 200
radius = size / 2

# Create an array of RGB color values
colors = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 128, 0),    # Green
    (0, 0, 255),    # Blue
    (128, 0, 128),  # Purple
]

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
        if distance <= radius:
            # Calculate the angle of the pixel relative to the center of the circle
            angle = math.atan2(y - radius, x - radius)
            
            # Map the angle to an index in the array of colors
            index = round(angle / (2 * math.pi / len(colors)))
            color = colors[index % len(colors)]
            
            # Calculate the saturation based on the distance from the center of the circle
            s = distance / radius
            
            # Convert the color and saturation to RGB color values
            r = int(color[0] * s)
            g = int(color[1] * s)
            b = int(color[2] * s)
            
            # Draw the pixel with the calculated color
            draw.point((x, y), (r, g, b))

# Save the image
image.show()
