#Create a dictionary with keys: name, age, course and print it
mydict={
    'name':'john',
    'age':20,
    'course':'python'
}
print(mydict)
#How do you access the value of a key that does not exist in a dictionary?
print(mydict.get("gender","key not found"))
#Add a new key college to an existing dictionary.
mydict["college"]="undergraduate"
print(mydict)
#Update the value of age in a dictionary.
mydict.update({'age':23})
print(mydict)
#Delete a key-value pair using del.
del mydict["college"]
print(mydict)
#Remove the last inserted item using a dictionary method.
mydict.popitem()
print(mydict)
#Find the (number of key-value pairs in a dictionary.
print(len(mydict))
#Print only keys of a dictionary using a loop.
for x in mydict:
    print(x)
#Print only values of a dictionary.
for y in mydict:
    print(mydict[y])#print(mydict.values())
#Check whether a key exists in a dictionary or not
if "name" in mydict:
    print("yes,the key is present in dictionary")
else:
    print("key is not in the dictionary")
#Given a dictionary, print all keys and values using a loop.
for x,y in mydict.items():
    print(x,":",y)
#Merge two dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
#Create a dictionary from a list of numbers where  ey = number, value = square of that number
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(squares)
#Count how many times each character appears in a string using a dictionary.
text="python"
char_count={}
for ch in text:
    if ch!=" ":
        char_count[ch]=char_count.get(ch,0)+1
print(char_count)
#Find the key with the maximum value in a dictionary.
marks={
    'a':40,
    'c':59,
    'e':60,
    'd':56
     }
max_key=max(marks,key=marks.get)
print(max_key)
#Sort a dictionary by keys
sort_keys=dict(sorted(marks.items()))
#Find the sum of all values in a dictionary.
values_sum=sum(marks.values())
print(values_sum)
#From a dictionary, print only items where value is greater than 50.
items={
    'milk':59,
    'bread':15,
    'apples':80,
    'jam':25,
    'sause':9
}
for x in items:
    if items[x]>=50:
        print(x,":",items[x])
#or
for key,values in items.items():
    if values >= 50:
        print(key,":",values)
#Remove all items with value less than 10.
keys_to_remove=[]
for keys, values in items.items():
    if values<10:
        keys_to_remove.append(key)
for keys in keys_to_remove:
        del items[keys]
print(items)
#Replace all negative values with 0
data = {'a': 10, 'b': -5, 'c': 3, 'd': -2}
for key,value in data.items():
    if value <0:
        data[key]=0
print(data)
#Check whether all values in a dictionary are unique.
data = {'a': 10, 'b': 20, 'c': 10}
values = list(data.values())
if len(values) == len(set(values)):
    print("All values are unique")
else:
    print("Duplicate values found")
#Create a nested dictionary for a student and Access science marks.
student={
    'name':"john",
    'marks':{
        'maths':80,
        'science':75
    }

}
print(student["marks"]["science"])
#Given a list of student names, count how many times each name appears.
names=['ram','sita','ram','madhu','sita']
freq={}
for name in names:
    freq[name]=freq.get(name,0)+1
print(freq)
#Convert a dictionary into a list of (key, value) tuples.
data = {'a': 1, 'b': 2, 'c': 3}
result = list(data.items())
print(result)







