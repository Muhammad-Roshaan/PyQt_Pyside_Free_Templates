# Dictionaryclass6
# 15-3-2024

my_dictionary = {"name": "faheem",  
                 1 : "java",
                 "class" : "cs",
                 2 : "python"
                 }
my_dictionary2 = {"name" : "Faseeh",                                  
                  "class" : "Advance Python",
                  "game" : "snooker",
                  1 : "Java"
                }

for i in my_dictionary.values():
    print(i)
for i in my_dictionary.items():
    print(i)
for i in my_dictionary.keys():
    print(i)
for i in my_dictionary:
    print(i, ":", my_dictionary[i])
# merge = {**my_dictionary,**my_dictionary2}
# print(merge)
# my_dictionary.update(my_dictionary2)
# print(my_dictionary)
# print(my_dictionary["name"])
# my_dictionary["name"] = "Hamza"
# x = my_dictionary.get(1)
# x = "hello World"
# my_dictionary.update({1 : "Python"})
# print(my_dictionary)
# print(my_dictionary.keys())
# print(my_dictionary.items())
# print(my_dictionary.values())
# print(my_dictionary.pop(1))
# print(my_dictionary.popitem())
# my_dictionary.clear()
# print(my_dictionary)
# del my_dictionary
# print(my_dictionary)
# my_dictionary1 = my_dictionary.copy()
# var2 = dict(my_dictionary)
# print(my_dictionary1)
# print(type(var2))
# print(type(my_dictionary1))

list = ["ali","hamza","ahsan"]
for i in list:
    print(i)
    
#------Dictionary comprehention--------
string = "hello"
key =['a','b','b','d','e']
values = [1,2,3,4,5]
my_dict = {x:y for (x,y) in  zip(key, values)}
print(my_dict)

my_dict2 = {x:x*2  for x in range(1,12)}
print(my_dict2)