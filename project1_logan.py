import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("skyblue")  # sky

scale = 1.8

# house
def house_body(size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def roof(size):
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def window(size):
    t.fillcolor("skyblue")
    t.begin_fill()
    house_body(size)
    t.end_fill()

    # window pane
    t.penup()
    t.forward(size/2)
    t.left(90)
    t.pendown()
    t.forward(size)
    t.backward(size)
    t.right(90)
    t.backward(size/2)

    t.left(90)
    t.penup()
    t.forward(size/2)
    t.pendown()
    t.right(90)
    t.forward(size)
    t.backward(size)
    t.left(90)
    t.penup()
    t.backward(size/2)
    t.right(90)

# flower stem
def flower():
    t.pendown()
    t.color("darkgreen")  # stem color
    t.setheading(90)
    t.forward(20)  # stem
    t.color("red")  # petals
    t.begin_fill()
    for _ in range(6):
        t.circle(5)
        t.left(60)
    t.end_fill()
    t.penup()
    t.setheading(0)

# cloud filler
def draw_cloud(element, buffer, size=60):
    t.penup()
    t.goto(element, buffer)
    t.pendown()
    t.color("white")
    t.fillcolor("white")

    num_circles = 20
    for _ in range(num_circles):
        t.begin_fill()
        cloudx = random.randint(-size//2, size//2)
        cloudy = random.randint(-size//4, size//4)
        radius = random.randint(size//5, size//3)
        t.penup()
        t.goto(element + cloudx, buffer +cloudy)
        t.pendown()
        t.circle(radius)
        t.end_fill()
    t.penup()

# house
house_size = 100 * scale
window_size = 20 * scale
door_height = 40 * scale
door_width = 20 * scale

# grass
total_height = turtle.window_height()
total_width = turtle.window_width()
grass_bottom = -total_height // 2
grass_top = 0
grass_left = -total_width // 2
grass_right = total_width // 2
t.penup()
t.goto(0, grass_top)
t.pendown()
t.color("green")
t.begin_fill()
t.goto(grass_left, grass_top)
t.goto(grass_left, grass_bottom)
t.goto(grass_right, grass_bottom)
t.goto(grass_right, grass_top)
t.end_fill()

# clouds
for _ in range(5):
    cloud_1 = random.randint(grass_left, grass_right)
    cloud_2 = random.randint(150, 300)
    cloud_size = random.randint(50, 90)
    draw_cloud(cloud_1, cloud_2, size=cloud_size)

# house
t.penup()
t.goto(-house_size/2, -50)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
house_body(house_size)
t.end_fill()

# roof
t.left(90)
t.forward(house_size)
t.right(90)
roof(house_size)

# door
t.penup()
t.goto(-door_width/2, -50)
t.setheading(90)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(door_height)
    t.right(90)
    t.forward(door_width)
    t.right(90)
t.end_fill()

# doorknob
t.penup()
t.goto(door_width/4, -50 + door_height/2)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(3)
t.end_fill()

# windows
window_1 = [
    (-house_size/3, house_size/4),
    (house_size/6, house_size/4)
]

for element, buffer in window_1:
    t.penup()
    t.goto(element, buffer)
    t.setheading(0)
    t.pendown()
    window(window_size)

# flowers on grass
num_flowers = 35
for _ in range(num_flowers):
    flower_1 = random.randint(grass_left, grass_right)
    flower_2 = random.randint(grass_bottom + 10, grass_top - 50)
    t.penup()
    t.goto(flower_1, flower_2)
    flower()

t.hideturtle()
turtle.done()