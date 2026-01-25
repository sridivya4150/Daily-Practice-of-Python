#Python set is an unordered collection of multiple items having different datatypes
#a set is a collection which is unordered,mutable and unindexed.
set1={"apple","banana"}
print(type(set1))
#set is unordered,so you cannot be sure in which order the items will appear
print(set1)#printing set
#set doesn't allow duplicates.Duplicates values will be ignored
set2={1,2,3,4,5,6,1}
print(set2)
#get the length of the a set
print("lenght of the set2 is :",len(set2))
#creating a set()--{},set()
#by using {}
set3={'g','m','n'}
print(set3)
#by using set()
set4=set("apple",1,3)
print(set4)
#creating empty set
set5=set()#{}--creates empty dictionary
print(set5)
#creating a set with the use of a list
set6=set(["apple",3,"banana"])
print(set6)
#creating a set with the use of a tuple
tup=("water",5,"rice")
print(set(tup))




