import random
import turtle_pil

from PIL import Image, ImageDraw

image = Image.new('RGBA', (1280, 1440))
width, height = image.size

def generate_gradient(color1: tuple[int, int, int], color2: tuple[int, int, int], 
                      width: int, height: int):
    base = Image.new('RGBA', (width, height), color1)
    top = Image.new('RGBA', (width, height), color2)
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

bound_top_left = (0 - width / 2, (height / 2) + (height / 8))
bound_bottom_right = (width + (width / 2), (height + (height / 2)))

draw_image.ellipse((bound_top_left, bound_bottom_right), fill=((
    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
    outline=(0, 0, 0), width=(4))

rectangle_width = 100
rectangle_top_left = ((width / 2) - (rectangle_width / 2), height / 4)
rectangle_bottom_right = ((width / 2) + (rectangle_width / 2), (height - (height / 4)))

draw_image.rectangle((rectangle_top_left, rectangle_bottom_right), fill=(
    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), outline=(0, 0, 0), width=(3))

monolith_border = 6
elementary_rule = 22

ca_draw_data = generate_ca_data(int(((height / 2) - (monolith_border * 2))), 
                                int((rectangle_width - (monolith_border * 2))), True, elementary_rule)

for y in range (int((height / 2) - (monolith_border * 2))):
    for x in range (rectangle_width - (monolith_border * 2)):
        if ca_draw_data[y][x]: draw_image.point((x + (width / 2) - (rectangle_width / 2) + monolith_border, y + height / 4 + monolith_border), (0, 0, 0))

size = 5
positions = []

AXIOM = 'X'
RULES = { 'X' : 'F+[[X]-X]-F[-FX]+X',
          'F' : 'FF',
          '[' : '[',
          ']' : ']',
          '+' : '+',
          '-' : '-' }

ITERATIONS = 5

def l_system(start, rules):
    out_system = ''
    for c in start:
        s = rules[c]
        out_system += s

    return out_system

s = AXIOM
for i in range(ITERATIONS):
    s = l_system(s, RULES)

turtle_pil.left(90)
turtle_pil.pensize(3)
turtle_pil.penup()
turtle_pil.goto(0, 0 - turtle_pil.window_height() / 2)
turtle_pil.pendown()

for op in s:
    if op == "F":
        turtle_pil.forward(size)
    if op == "G":
        turtle_pil.forward(size)
    elif op == "+":
        turtle_pil.left(random.randint(20, 40))
    elif op == "-":
        turtle_pil.right(random.randint(20, 40))
    elif op == "[":
        positions.append((turtle_pil.heading(), turtle_pil.position()))
    elif op == "]":
        heading, position = positions.pop()
        turtle_pil.penup()
        turtle_pil.goto(position[0], position[1])
        turtle_pil.setheading(heading)
        turtle_pil.pendown()

turtle_pil.done()

tree = Image.open('./output.png')
tree_alpha = tree.convert('RGBA')
tree_data = tree_alpha.getdata()

new_data = []
for d in tree_data:
    if d[0] == 255 and d[1] == 255 and d[2] == 255:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(d)

tree_alpha.putdata(new_data)

image.alpha_composite(tree_alpha, (int(width / 8 * 4.5), int(height / 8 * 2.5)))

image.save('./monolith.png')