# def printLine():
#     line = []
#     prev_val = 1
#     line.append('x')
#     for i in range(1, 7):
#         line.append( str(i))
#     print line
#     for y in range(1,7):
#         line[0] = (y)
#         if (int(line[0]) > 1):
#             for y in range(1, 7):
#                 line[y] = str(line[0]*(y ))
#         print line
# printLine()

def printLine():
    line = []
    prev_val = 1
    line.append('x')
    for i in range(1, 13):
        line.append( str(i))
    print line
    for y in range(1,13):
        line[0] = (y)
        if (int(line[0]) > 1):
            for y in range(1, 13):
                line[y] = str(line[0]*(y ))
        print line
printLine()