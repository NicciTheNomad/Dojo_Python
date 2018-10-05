# def filter(sI):
#     print isinstance(sI, list)
# filter(['ray','nic','may','ash','oli']) 
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


def type_check(var_1):
    print type(var_1)
    if (var_1 < 100 and type(var_1 =='int')):
        print str(var_1) + ": is a small number"
    if (var_1 > 99 and type(var_1) == 'int'):
        print str(var_1) + ": is a large number."   
    if type(var_1) == 'list':
        print "list"     
   
type_check(sI)
type_check(sS)
type_check(bI) 
type_check(spL)

# class X(object):
#     a = 1
# X = type('X', (object,), dict(a=1))   
# print type(X)

