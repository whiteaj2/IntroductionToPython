"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andrew White.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

#Objective is to create a rainbow using loops, and only rosegraphics functions learned in video and previous modules
#Can be accomplished with one turtle and one for loop( by using clones, I think(haven't tested) ) but not the objective

import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(0.25)

#Define turtles for different colors
#Not efficient but simple
redTurtle = rg.SimpleTurtle()
redTurtle.pen = rg.Pen('red',10)

orangeTurtle = rg.SimpleTurtle()
orangeTurtle.pen = rg.Pen('orange',10)

yellowTurtle = rg.SimpleTurtle()
yellowTurtle.pen = rg.Pen('yellow',10)

greenTurtle = rg.SimpleTurtle()
greenTurtle.pen = rg.Pen('green',10)

blueTurtle = rg.SimpleTurtle()
blueTurtle.pen = rg.Pen('blue',10)

purpleTurtle = rg.SimpleTurtle()
purpleTurtle.pen = rg.Pen('purple',10)

#Change turtles orientation from right to up
redTurtle.left(90)
#Create a 180 degree arc
for i in range(180):
    #Red turtle moves forward 2, the rest move forward by a 0.18 decrement
    redTurtle.forward(2.0)
    redTurtle.right(1)

#Move turtle to starting position and rotate
orangeTurtle.pen_up()
orangeTurtle.forward(10)
orangeTurtle.pen_down()
orangeTurtle.left(90)
#Rest of code is copied from my previous code and repurposed
for i in range(180):
    orangeTurtle.forward(1.82)
    orangeTurtle.right(1)

yellowTurtle.pen_up()
yellowTurtle.forward(20)
yellowTurtle.pen_down()
yellowTurtle.left(90)
for i in range(180):
    yellowTurtle.forward(1.64)
    yellowTurtle.right(1)

greenTurtle.pen_up()
greenTurtle.forward(30)
greenTurtle.pen_down()
greenTurtle.left(90)
for i in range(180):
    greenTurtle.forward(1.46)
    greenTurtle.right(1)

blueTurtle.pen_up()
blueTurtle.forward(40)
blueTurtle.pen_down()
blueTurtle.left(90)
for i in range(180):
    blueTurtle.forward(1.28)
    blueTurtle.right(1)

purpleTurtle.pen_up()
purpleTurtle.forward(50)
purpleTurtle.pen_down()
purpleTurtle.left(90)
for i in range(180):
    purpleTurtle.forward(1.10)
    purpleTurtle.right(1)

#close window on click
window.close_on_mouse_click()