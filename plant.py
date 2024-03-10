import turtle
import random

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

gen = turtle.Turtle()
turtle.Screen().setup(2000, 1200)
gen.speed(0)
gen.left(90)
gen.pensize(3)
gen.penup()
gen.goto(0, 0 - turtle.Screen().window_height() / 2)
gen.pendown()



s = AXIOM
for i in range(ITERATIONS):
    s = l_system(s, RULES)

for op in s:
    if op == "F":
        gen.forward(size)
    if op == "G":
        gen.forward(size)
    elif op == "+":
        gen.left(random.randint(20, 35))
    elif op == "-":
        gen.right(random.randint(20, 35))
    elif op == "[":
        positions.append((gen.heading(), gen.position()))
    elif op == "]":
        heading, position = positions.pop()
        gen.penup()
        gen.goto(position)
        gen.setheading(heading)
        gen.pendown()

turtle.exitonclick()