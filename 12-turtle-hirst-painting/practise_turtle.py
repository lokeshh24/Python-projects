
from turtle import Screen
import turtle as t
import random
tim = t.Turtle()



# for i in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# tim.forward(20)
# tim.left(90)
# tim.forward(20)
# tim.left(90)
# tim.forward(20)
# tim.left(90)
# tim.forward(20)
# tim.left(90)




# Colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'RosyBrown', 'wheat', 'SlateGray', 'SeaGreen', 'DarkOliveGreen',
#           'SaddleBrown', 'Brown', 'RosyBrown', 'MediumVioletRed', 'DarkSlateBlue', 'gold', 'DarkViolet']
# num_sides = 3
# def run_mf(num_sides):
#     angle = 360/num_sides
#     for i in range (num_sides):
#         tim.forward(50)
#         tim.left(angle)
# for shape_side_n in range (3,11):
#     tim.color(random.choice(Colors))
#     run_mf(shape_side_n)
#     num_sides +=1






# t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# direction = [0,90,180,270]
# tim.pensize(5)
# tim.speed(2000)

# for _ in range(100):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)
draw_spirograph(5)
  



screen = Screen()
screen.exitonclick()