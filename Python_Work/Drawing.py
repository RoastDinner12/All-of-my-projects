import time
import turtle 
turtle.title("My balls hurt")

right = int(input("Enter Right Axis: "))
forward = int(input("Enter Left Axis: "))
left = int(input("Enter Left Axis"))
backward = int(input("Enter Backwards Axis: "))

turtle.getscreen()
t = turtle.Turtle()

t.right(right)
t.forward(forward)
t.left(left)
t.back(backward)
time.sleep(5)
turtle.getscreen()



