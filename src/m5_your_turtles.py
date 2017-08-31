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
import math
window = rg.TurtleWindow()
window.delay(0.25)

#Define turtle for drawing
redTurtle = rg.SimpleTurtle()
redTurtle.pen = rg.Pen('red',10)

#define array of colors
colors = ['red','orange','yellow','green','blue','purple']

#cycle through every color in the array
for i in range(6):
    #Set pen color to the color based on position in array, arranged for rainbow
    redTurtle.pen = rg.Pen(colors[i],10)
    #Move forward to starting position and face up
    redTurtle.pen_up()
    redTurtle.forward(10*i)
    redTurtle.pen_down()
    redTurtle.left(90)
    #Make a 180 degree arc
    for k in range(180):
        #18 because 180, number has to relate to pi because it's a circular arc
        redTurtle.forward(2-((math.pi / 18)*i))
        redTurtle.right(1)
    #Return to initial position and orientation
    redTurtle.pen_up()
    redTurtle.go_to(rg.Point(0,0))
    redTurtle.pen_down()
    redTurtle.left(90)

#define second turtle
blackTurtle = rg.SimpleTurtle()
blackTurtle.pen = rg.Pen('black',10)
#move black turtle down 5 because that is the radius of the pen
blackTurtle.pen_up()
blackTurtle.go_to(rg.Point(0,-5))
blackTurtle.pen_down()
#draw black underline
blackTurtle.forward(230)

#close window on click
window.close_on_mouse_click()