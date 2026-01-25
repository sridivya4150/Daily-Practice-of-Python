#creating list with repeated element
a=[2]*5
print(a)
#append items in list---appen(),extend(),insert()
#append()-Adds an element at the end of the list.
b=[10,45,67,78]
print(b.append(78))#
#append list to list
print(b.appen([4,"hello"]))#it append the that list as single item
#insert()-Adds an element at a specific position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#extend()-Adds multiple elements to the end of the list.
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)
