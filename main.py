import turtle
import math
from tkinter import Tk, Scale, HORIZONTAL

# Setup screen
screen = turtle.Screen()
screen.title("Fractal Tree Visualizer")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Improve speed with tracer
screen.tracer(0)

# Create turtle
tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()
tree.color("white")
tree.width(2)
tree.penup()

# Global parameters
angle = 30
depth = 8
wind_speed = 0.3
wind_factor = 0

# Draw a branch
def draw_branch(t, length, angle, depth, wind_factor):
    if depth == 0:
        t.color("green")
        t.stamp()
        return

    # Branch swaying effect
    sway = math.sin(wind_factor) * 10
    t.pendown()
    t.forward(length)

    # Left branch
    t.left(angle + sway)
    draw_branch(t, length * 0.7, angle, depth - 1, wind_factor * 1.2)
    t.right(angle + sway)

    # Right branch
    t.right(angle + sway)
    draw_branch(t, length * 0.7, angle, depth - 1, wind_factor * 1.2)
    t.left(angle + sway)

    # Back to trunk
    t.penup()
    t.backward(length)

# Animation control
def update_tree():
    global wind_factor
    wind_factor += wind_speed

    tree.clear()
    tree.goto(0, -250)
    tree.setheading(90)
    draw_branch(tree, 120, angle, depth, wind_factor)
    screen.update()
    screen.ontimer(update_tree, 30)

# Tkinter for interactive controls
root = Tk()
root.title("Fractal Tree Controls")

# Create sliders
angle_slider = Scale(root, from_=5, to=90, resolution=1, orient=HORIZONTAL, label="Angle")
angle_slider.set(angle)
angle_slider.pack(fill="x")

depth_slider = Scale(root, from_=1, to=14, resolution=1, orient=HORIZONTAL, label="Depth")
depth_slider.set(depth)
depth_slider.pack(fill="x")

wind_slider = Scale(root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label="Wind Speed")
wind_slider.set(wind_speed)
wind_slider.pack(fill="x")

# Update parameters in real-time
def update_parameters():
    global angle, depth, wind_speed
    angle = angle_slider.get()
    depth = depth_slider.get()
    wind_speed = wind_slider.get()
    root.after(50, update_parameters)

# Start animation and parameter updates
update_parameters()
update_tree()

# Run the Tkinter event loop
root.mainloop()
