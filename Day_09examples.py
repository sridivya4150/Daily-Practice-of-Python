#Create an empty set and add three elements to it.
set1=set()
set1.update((1,2,3))
print(set1)
#Remove an element from a set using remove() and discard().
set1={1,2,3,4,5}
set1.remove(2)
print(set1)
set1.discard(0)
print(set1)
#Check whether an element exists in a set.
print("is 1 in set1:",1 in set1)
#Create a set from a list and remove duplicates.
lst=[1,2,3,4,5,5,6]
set1=set(lst)
print(set1)
#Iterate through a set and print all elements.
set1={'a','b','c','d'}
for x in set1:
    print(x)
#Take two sets and find their union
set1={1,2,3,5}
set2={4,5,6}
print(set1.union(set2))
#Find the intersection of two sets
print(set1.intersection(set2))
#Find the difference between two sets
print(set1.difference(set2))
#Find the symmetric difference of two sets.
print(set1.symmetric_difference(set2))
#Check whether one set is a subset of another.
print(set1.issubset(set2))
#Remove all elements from a set
print(set1.clear())
#Convert a string into a set and count unique characters.
string="i love python"
set1=set(string)
print(set1)
print(len(set1))
#Remove duplicate values from a list using a set.
lst=[4,5,6,7,8,9,9]
set1=set(lst)
print(lst)
#Find common elements between two lists using sets.
set1={"apple","banana","grape"}
set2={"apple","orange","kiwi"}
print(set1.intersection(set2))
#Find elements present in list A but not in list B
print(set1.difference(set2))
#Merge multiple sets into one.
set1={1,2,3}
set2={4,5,6}
set3={8,9,0}
set4=set1.union(set2,set3)
print(set4)
#Create a frozen set and try modifying it.
f_set=frozenset((1,2,3,))
f1_set=frozenset((4,5,))
#adding elements into frozenset
print(f_set.intersection(f1_set))
#Store sets inside another set (hint: which type works?).
#to store set inside set we need to use frozensets
a=frozenset({"apple","banana"})
b=frozenset({'grape','cherry'})
c={a,b}
print(c)
#Find the maximum and minimum element from a set.
set1=(1,6,7,8,9)
print(max(set1))
print(min(set1))
#Remove random elements from a set until it becomes empty
set1={1,23,45,6,7,8}
while set1:
    print(set1.pop())
print(set1)
#Find all unique vowels in a given string using sets.
text = "programming is awesome"
unique_vowels = set(text.lower()) & set("aeiou")
print(unique_vowels)

    