import random

from PIL import Image, ImageDraw

image = Image.new('RGB', (1280, 1440))
width, height = image.size

def generate_gradient(color1: tuple[int, int, int], color2: tuple[int, int, int], width: int, height: int):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []

    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)

    return base

image = generate_gradient((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width, height)

draw_image = ImageDraw.Draw(image)

bound_top_left = (0 - width / 2, height / 2)
bound_bottom_right = (width + width / 2, (height + height / 2))

draw_image.ellipse((bound_top_left, bound_bottom_right), fill=((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

image.save('./monolith.png')