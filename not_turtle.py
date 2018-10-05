# try this either as a .py file or in the python shell
import turtle

# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        turtle.color('red')
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20

# import turtle

def turtle_go():
    turtle.forward(15)
    turtle.right(25)

turtle_go()    