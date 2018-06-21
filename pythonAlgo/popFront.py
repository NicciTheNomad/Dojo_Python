def newList(arr):
    arr.sort()
    print arr
    y = []
    w = []
    for z in range(len(arr)/2,len(arr)):
        print z
        w.append(arr[z])
        # print w
    w.append(0)
    print w

    for x in range(0,len(arr)/2):
        y.append(arr[x])
        # print y

    for i in range(len(w)-2,-1,-1):  
        print i
        w[i+1] = w[i]
        print w

    w[0] = y
    print w           

newList([19,2,54,-2,7,12,98,32,10,-3,6])