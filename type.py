
def array_type(arr):
    float_count = 0
    num_count = 0
    str_count = 0
    number = 0
    words = []
    for i in range(0,len(arr)):
        # print type(arr[i])
        if type(arr[i])==str:
            print 'i am a string'
            str_count = str_count + 1
            words.append(arr[i] + '_')
        elif type(arr[i])==int:
            print 'i am an int'
            num_count = num_count + 1
            number = number + arr[i]
        elif type(arr[i])==float:
            print 'i am an float'
            float_count = float_count + 1
            number = number + arr[i]

    num_count = num_count + float_count    
        
    if (str_count>0 and num_count>0):
        print "mix type"
        print words
        print "the numerical value is: ", number
    elif (str_count>0 and num_count == 0):
        print "all strings" 
        print words
    elif (num_count>0 and str_count == 0):
        print "all numbers"    
        print "the numerical value is: ", number   

array_type( ['magical unicorns',19,'hello',98.98,'world'])        