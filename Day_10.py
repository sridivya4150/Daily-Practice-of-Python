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
#Accessing Dictionary items-by referring key,get(),keys(),values()
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
#


