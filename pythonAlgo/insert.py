def newList(arr,index_val,newNew):
    arr.append(0)
    for i in range(len(arr)-2,-1,-1):  
        arr[i+1] = arr[i]     
    arr[index_val] = newNew
    print arr
newList([1,-2,3],0,0)
newList([1,-2,3],1,0)
# newList([1,-2,3],7,0)