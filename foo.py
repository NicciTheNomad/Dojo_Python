import math

def foo(num1, num2):
    display = []
    for x in range(num1, num2):
        # print (math.sqrt(x)%1)
        if (math.sqrt(x)%1) == 0:
            display.append(x)
    print display

foo(100, 100000)    