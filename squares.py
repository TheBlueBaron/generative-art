import random

from PIL import Image, ImageDraw

image = Image.new('RGB', (2560, 1440))
width, height = image.size

rectangle_width = 150
rectangle_height = 150

number_of_rectangles_in_layer = random.randint(15, 50)
number_of_layers = 5

draw_image = ImageDraw.Draw(image)

draw_image.rectangle([(0, 0), (width, height)], fill=(0, 0, 0, 255))

for i in range(number_of_layers):

    for j in range(number_of_rectangles_in_layer):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)

        rectangle_constraints = [(rectangle_x, rectangle_y), (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
        
        draw_image.rectangle(rectangle_constraints, fill=((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

image.save('./squares.png')
