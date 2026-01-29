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
#constructing dictionary using dict()
person = dict(name = "John", age = 36, country = "Norway")
print(person)
print(type(person))

#
