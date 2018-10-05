def characterFind(array,character):
    char_list = []
    for i in range(0,len(array)):
        for c in array[i]:  
            if c == character:
                char_list.append(array[i])
                print array[i]
                print char_list
               
characterFind(['nicci','boquitbr','ray','maya'],'r')     


#Minadaya code for checking array item type
def list_type (list):
    total = 0
    new_list = [] 
    for x in list:
        #print x
        if type (x) == int:
            total+= x
            #print "this is an integer"
            # print "sum", total
        else:
            if type (x) == str:
                print "sting:", x
        if isinstance (list, str):
            print "this is a list of strings"
        # else:
            # if isinstance (list, int):
                # print "this is a list of numbers"
            # else:
                # print "this is a mixed list" 
    # print "sum", total 
    # print 'new list: ', new_list       



# list_type (['nicci', 1,'work',2,3,'boo', 'o'])