
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", 'nicci']
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas",'dog']
# def make_dict(list1, list2):
#   new_dict = zip(name,favorite_animal)
#   return new_dict
# print make_dict(name,favorite_animal)  


# -------------------
# countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# country_specialities = zip(countries,dishes)
# # print country_specialities
# # /------------
# array = []
# my_dict = {}
# countries_tup = ()
# dishes_tup = ()
 
# for i in countries:
#     print i
#     countries_tup = (i)
#     print countries_tup
#     keys = countries_tup

# for j in countries:
#     print j
#     dishes_tup = (j)
#     print dishes_tup
#     values = dishes_tup
# print values

# dict = {key[k]: values[k] for k in range(len(keys))}    

# keys = ('name', 'age', 'food')
# values = ('Monty', 42, 'spam')    
# dict = {keys[i]: values[i] for i in range(len(keys))}
# -----
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks"]
# dict = {name[i]: favorite_animal[i] for i in range (len(name))}

# print (dict)


# keys = ('1', '2', '3','4', '5')
# values = ('11', 22, '33', '44','55', '66')    
# dict = {keys[i]: values[i] for i in range(len(keys))}
# print (dict)

first = ('a', 'b', 'c')
second = ('aa', 'bb', 'cc', 'dd')

if len(first) > len(second): 
    dict ={second[i]: first[i] for i in range(len(second))}
    print dict 
else:
    dict ={first[i]: second[i] for i in range(len(first))}
    print dict    
