# def characterFind(array,character):
#     for i in range(0,len(array)):
#         for c in array[i]:  
#             if c == character:
#                 print array[i]
               
# characterFind(['nicci','boquitb','ray','maya'],'r')     


#Minadaya code for checking array item type
def list_type (list):
    total = 0
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
        else:
            if isinstance (list, int):
                print "this is a list of numbers"
            else:
                print "this is a mixed list" 
    print "sum", total          
list_type ([1,2,3,'boo'])