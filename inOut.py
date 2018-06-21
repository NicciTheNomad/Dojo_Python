# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }
# my_tup = ()
# for key in my_dict:
#     my_tup = my_tup + (key,my_dict[key])
#     print my_tup


my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}
array = []
for key in my_dict:
    my_tup = (key, my_dict[key])
    array.append(my_tup)
    print my_tup
print array    
test_dict = dict(array)
print test_dict   


