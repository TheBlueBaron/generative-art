import random

from PIL import Image, ImageDraw

image = Image.new('RGB', (1280, 1440))
width, height = image.size

def generate_gradient(color1: tuple[int, int, int], color2: tuple[int, int, int], 
                      width: int, height: int):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []

    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)

    return base

def generate_ca_data(height: int, width: int, isRandom: bool, rule_num: int):
    if isRandom:
        initial_row = [random.randint(0, 1) for i in range(width)]
    else:
        initial_row = [0]*width
        initial_row[width / 2] = 1

    ca_data = [initial_row]

    rule = [(rule_num / pow(2, i)) % 2 for i in range(8)]

    for i in range(height - 1):
        data = ca_data[-1]

        new = [int(rule[4 * data[(j - 1) % width] + 2 * data[j] + data[(j + 1) % width]])
               for j in range(width)]
        ca_data.append(new)

    return ca_data

image = generate_gradient((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 
                          (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 
                          width, height)

draw_image = ImageDraw.Draw(image)

bound_top_left = (0 - width / 2, height / 2)
bound_bottom_right = (width + (width / 2), (height + (height / 2)))

draw_image.ellipse((bound_top_left, bound_bottom_right), fill=((
    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
    outline=(0, 0, 0), width=(4))

rectangle_width = 100
rectangle_top_left = ((width / 2) - (rectangle_width / 2), height / 4)
rectangle_bottom_right = ((width / 2) + (rectangle_width / 2), (height - (height / 4)))

draw_image.rectangle((rectangle_top_left, rectangle_bottom_right), fill=(
    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), outline=(0, 0, 0), width=(3))

monolith_border = 5
elementary_rule = 22

ca_draw_data = generate_ca_data(int(((height / 2) - (monolith_border * 2))), 
                                int((rectangle_width - (monolith_border * 2))), True, elementary_rule)

for y in range (int((height / 2) - (monolith_border * 2))):
    for x in range (rectangle_width - (monolith_border * 2)):
        if ca_draw_data[y][x]: draw_image.point((x + (width / 2) - (rectangle_width / 2) + monolith_border, y + height / 4 + monolith_border), (0, 0, 0))

image.save('./monolith.png')