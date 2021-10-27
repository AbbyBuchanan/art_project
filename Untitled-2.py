import turtle as trtl
import random as rand 
circle = trtl.Turtle()

orange_circle = "orange"
shape = "circle"
size = 5

circle.shape(shape)
circle.fillcolor(orange_circle)
circle.shapesize(size)

circle.penup()
def circle_clicked(x, y):
  change_position()

def change_position():
  new_xpos = rand.randint(-300,300)
  new_ypos = rand.randint(-300,300)
  circle.goto(new_xpos,new_ypos)








wn = trtl.Screen()
circle.onclick(circle_clicked)
wn.setup(width=800,height=800)
wn.addshape('confetti.gif')
wn.mainloop()