# my_dictionary = {
#     "name":"Ash",
#     "country":"Canada",
#     "spoken_lang":"tagalog",
#     "age" : 8
# }
# print my_dictionary["spoken_lang"]
# print my_dictionary["age"]
# my_dictionary["spoken_lang"] = "German"
# print my_dictionary["spoken_lang"]
# ----------
# for i in my_dictionary:
#     print my_dictionary[i]


# print my_dictionary["name"]," is my name."   
# print my_dictionary["age"]," is my age." 
# print my_dictionary["country"]," is where I was born." 
# print my_dictionary["spoken_lang"]," is one of the languages I speak."  
# ----------
# person_1 = {
#     "name":"ray","position":"dad","language_spoke":"Tagalog"
#     }
# person_2 = {
#     "name":"nic","position":"mom","language_spoke":"English"
#     }
# person_4 = {
#     "name":"ash","position":"oldest son","language_spoke":"English"
#     }    


# print person_2["language_spoken"]   

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }
for key, data in context.items():
    #print data
    for value in data:
        print "Question #", value["id"], ": ", value["content"]
        print "----"