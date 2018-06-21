def newList(arr,newNew):
    arr.append(0)
    for i in range(len(arr)-2,-1,-1):  
        arr[i+1] = arr[i]     
    arr[0] = newNew
    print arr
newList([1,-2,3],0)