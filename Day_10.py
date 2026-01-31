#Python dictionaries
#Dictionary-Dictionaries are used to store data values in key:value pairs
#a dictionary is a collection which is ordered,changeable and do not allow duplicates
#creating dictionary
dict={
   'a':"apple",
    'b':"banana"
}
print(dict)
#type of dictionary
print(type(dict))
#Dictionary items are presented in key:value pairs,and can be referred by using the key name
print(dict["a"])
#Dictionaries cannot have two items with same key
#Duplicate values will overwrite existing values but it can allow same item for 2 different keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(car)
#Dictionary length
print(len(car))
#Dictionarycan store any data type
exam={
    'name':'student1',
    'class':12,
    'marks':98,
    'pass': True,
    'subjects':['maths','science','social']

}
print(exam)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Accessing Dictionary items-by referring key,get(),keys(),values(),items()
#by using referring keys
print(exam["name"])
#by using get()
d = { 
    "name": "Kat",
    1: "Python", 
    (1, 2): [1,2,4] 
    }
print(d.get(1))
#by using keys()-by using this method will return a list of all the keys in the dictionary
#----------------------------------------------------------------------------------------------------------------------------------------
x=d.keys()
print(x)
#changes done to the dictionary will be reflected in the keys list.
d["age"]=22
print(x)
#values()-method will return a list of all the values in the dictionary
y=d.values()
print(y)
#any changes done in dictionary will be reflected in the values first
d["gender"]="Male"
print(y)
#items()-method will return each item in a dictionary, as tuples in a list.
print(d.items())
print(d)#printing original list
#check if key exists in dictionary
if 'gender' in d:
    print("yes,'gender' is one of the key in the d dictionary")
#-------------------------------------------------------------------------------------------------------------
#change values-by using key name,update()
#by using key name
student={
    'name':'kevin',
    'rollno':545,
    'marks':99,

}
student["name"]='ben'
print(student)
#by using update()-it will update the dictionary with the items from the given argument
#note:the argument must be a dictionary
student.update({'rollno':423})
print(student)
#------------------------------------------------------------------------------------------------------------
#adding dictionary items-by using new index key,by using update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)
#------------------------------------------------------------------------------------------------------------
#remove Dictionary items-pop(),popitem(),del,clear()
#pop()-removes the item with the specified key name and return it
print("the deleted item using pop():",thisdict.pop("color"))
print(thisdict)
#popitem-removes the last inserted item
print("the deleted item by using popitem() is:",thisdict.popitem())
print(thisdict)
#del --keyword removes the item with the specified keyname but cannot return it
del thisdict["model"]
print(thisdict)
#del can also delete the dictionary completely
del thisdict
#clear()-method empties the dictionary
items={
    'bread':20,
    'milk':123
}
items.clear()
print(items)
#-----------------------------------------------------------------------------------
#loop through a dictionary
#print all key names int the dictionary,one by one using list
cart={
    "clothes":1000,
    'slippers':243,
    'vegetables':564
}
for x in cart:
    print(x)#prints keys/we can use keys()
for x in cart:
    print(cart[x])#prints values/we can use values() 
for x,y in cart.items():
    print(x,":",y)#print both values and keys
#----------------------------------------------------------------------------------------------------------------------------------------
#copy dictionaries-copy(),dict()
cart={
    "clothes":1000,
    'slippers':243,
    'vegetables':564
}
#by using copy()
basket=cart.copy()
print(basket)
#---------------------------------------------------------------------------------------------------------------------
#Nested Dictionaries-a dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#add three dictionaries into a new dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#Access items in nested dictionaries
print(myfamily["child1"]["name"])
#Loop through nested Dictionaries
for x,y in myfamily.items():
    print(x)
    for z in y:
        print(z,":",y[z])
#------------------------------------------------------------------------------------------------------------------------------------
#Dictionary methods
#clear()-removes all the elements from the dictionary
#copy()-returns a copy of the dictionary
#fromkeys()-returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
#get()-returns the value of the specified key
#items()-returns a list containing a tuple for each key value pair
#keys()-returns a list containing the dictionary's keys
#pop()-removes the last inserted key-value pair
#popitem()-removes the last inserted keyk-value pair
#setdefault-Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)
#update()-updates the dictionary with the specified kay-value
#values()-returns a list of all the values in the dictionary






