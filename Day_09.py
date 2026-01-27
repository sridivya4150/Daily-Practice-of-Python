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
set4=set("apple")
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
#accesing items--using for loop,using keyword in
#by using for loop
fruits={"apple","banana","cherry"}
for x in fruits:
    print(x)
#by using in keyword
print("banana"in fruits)
#if not present
print("banana" not in fruits)
#adding items-add(),updat()
#once a set is created,you cannot change its items,but you can add new items
set1={1,2,3,4,1,5,2}
#by using add()--only single  item
set1.add("apple")
print(set1)
#by using update()--multiple items
set1.update(('greem','white'))
print(set1)
#the object in the update() method does not have to be a set.
set2=["ant","bat"]
print(set1.update(set2))
#remove set items-remove(),discard()
#remove()--removes a specified element from the set.
set1 = {1, 2, 3, 4, 5}
set1.remove(3)#raises error if the element is not present in set
print(set1)  
#discard()-removes specified element from the set.
fruits={"apple","banana","cherry"}
fruits.discard("banana")
print(fruits)#does not raises error if the element is not prese in set
#we can use pop() to remove an item,but this method will remove a random item.
numbers={1,2,3,4,5}
numbers.pop()
print(numbers)
#clear()-removes all items in the set
numbers.clear()
print(numbers)
#del -- delete complete set
del numbers
#join sets--union(),update(),intersection(),difference(),symmetric_difference()
#union(),update()-methods joins all items from both sets
#union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.union(set2))
#instead of union() we can use | operator
set3=set1|set2
print(set3)
#joining multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)#or set1|set2|set3|set4
print(myset)
#join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
print(x.union(y))#| only joins sets with sets not other data types
#update()-insets all items from one set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#union(),update() both exclude any duplicate items
#intersection()---method will return a new set,that only contains the items that are present in both sets.
set1={2,3,4,5,6}
set2={9,8,7,6,5}
print(set1.intersection(set2))#we can use & operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.intersection(set2)
print(set3)#& operator only allows you to join sets with sets
#intersection_update()-it will change thee original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.intersection_update(set2))
#difference()-a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.difference(set2)
print(set3)#we can use '-' operator
#difference_update()-method will keep the items from the first set that are not in the other set.
set1.difference_update(set2)
print(set1)
#symmetric_difference()-method will keep only elements that are not present in both sets
print(set1.symmetric_difference(set2))#we can use ^ operator
#symmetric_difference only change the original set instead of returnig a new set.
#frozenset--it is immutable version of a set
#creating a frozenset()
x=frozenset({"apple","banana","cherry"})
print(x)
#creating empty frozenset()
nu=()
ef=frozenset(nu)
print(ef)
#frozenset()  methods-copy(),difference(),intersection(),isdisjoint(),issubset(),issuperset(),symmetric_difference(),union()
#copy()--copies a frozenset
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
c=A.copy()
print(c)
#difference()-Returns a new frozenset with the difference
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)
#intersection()-Returns a new frozenset with the intersection
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)
#isdisjoint()-Returns whether two frozensets have an intersection
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))
#issubset()-'<',"<=" -returns true if this frozenset is a subset of another
a={1,2,3,4,5}
b={3,4}
print(b.issubset(a))
#issuperset()-'>'">="--returns true if this frozenset is a superset of another
print(a.issuperset(b))
#set methods
#add()-adds an element to the set
fruits={"apple","banana","cherry"}
fruits.add("grape")
print(fruits)
#clear()-removes all the elements fromt the set
fruits.clear()
print(fruits)
#copy()-returns a copy of the set
set1={12,2,3,4}
set2=set1.copy()
print(set3)
#pop()-removes an random element from the set
















