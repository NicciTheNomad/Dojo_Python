# try this either as a .py file or in the python shell
import turtle

# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        turtle.color('blue')
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20
     

def characterFind(array,character):
    char_list = []
    for i in range(0,len(array)):
        for c in array[i]:  
            if c == character:
                char_list.append(array[i])
                print array[i]
                print char_list
               
characterFind(['nicci','boquitbr','ray','maya'],'r') 