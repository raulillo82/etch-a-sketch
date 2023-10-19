from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup (width=1200, height=900, startx=None, starty=100)
screen.colormode(255)

step_size = 10
shift_range = 10

t.speed("fastest")

def move_forwards():
    t.forward(step_size)
def move_backwards():
    t.backward(step_size)
def rotate_counterclockwise():
    t.setheading(t.heading() + shift_range)
def rotate_clockwise():
    t.setheading(t.heading() - shift_range)
def clear():
    t.pu()
    t.clear()
    t.home()
    t.pd()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
