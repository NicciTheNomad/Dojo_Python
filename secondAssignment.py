# words = "It's Thanksgiving day. It's my birthday, too!"

# print words.find('day')
# 18
# /-----
# print words.replace('i','II',2)
# It's ThanksgIIvIIng day. It's my birthday, too!
# >>> print words.replace('day','month')
# It's Thanksgiving month. It's my birthmonth, too!

# >>> x = [2,54,-2,7,12,98]
# >>> print min(x)
# -2
# >>> print max(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> print max(x)
# 98

# >>> print x[len(x)-1]
# 98
# >>> x = ["hello",2,54,-2,7,12,98,"world"]
# print "hello nicci, work hard"

# def firstLast(arr):
#     first = arr[0]
#     last = arr[len(arr)-1]
#     return first + last

# print firstLast(["hello",2,54,-2,7,12,98,"world"])

# print y = (x[0], x[len(x)-1])

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