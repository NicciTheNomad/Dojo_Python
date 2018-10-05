
def funFunc(start, stop):
    for i in range(start,stop+1):
        if i%2 == 0:
            print "number is ", i,'. This is an even number.'
        else:
            print "number is ", i,'. This is an odd number.'

funFunc(1,2)    


# ----------------
def multi(arr,num):
    for i in range(0,len(arr)):
        arr[i] *= num
    return arr
print multi([1,2,3],5)    


# -------------
# def multi(arr,num):
#     # t_arr = []
#     for i in range(0,len(arr)):
#         print(arr[i]*num)
# multi([1,2,3],5) 
# -------
def layered_multiples(arr):
    new_array = []
    for b in arr:
        array_val = []
        # val_to_print = arr[b]
        for c in range(0,b):
            # print arr[0]
            # val_to_print = arr[b]
            array_val.append(arr[0])
        new_array.append(array_val)
    return new_array
x = layered_multiples(multi([1,2,3],3))
print x
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
