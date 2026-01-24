#tuple-collection different data types which is ordered and unchangeable
#tuples are written with round,().
#creating tuple-(),tuple()
#by using ()
tup=("apple",2)
print(type(tup))#printing type
#creating empty tuple-
tup1=()
print(tup1)
#by using tuple()--built-in function
tup=tuple('apple')
print(tup)
#creating tuple with only single item
tup=(1,)#need to keep comma to identify as tuple
print(tup)
#creating a tuple with repetition
tup2=("hello",)*3
print(tup2)
#creating nested tuples
tup1=(0,1,2,3)
tup2=("apple","banana")
tup3=(tup1,tup2)
print(tup3)
#creating tuple with the use of loop
tup=("apple")
n=3
for i in range(int(n)):
    tup=(tup,)
    print(tup)
#tuple length
print(len(tup))
#Access Tuple items
fruits=("apple","banana","cherry")
#accessing first element in the tuple
print(fruits[0])
#accessing elements by using negative indexing
print(fruits[-1])#prints last element in the tuple
#accesing range of indexes--slicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#start at index 2(included) and end at index 5(not included)
#range of negative index
print(thistuple[-4:-1])
#unpacking tuple items
a,b,c,d,e,f,g=thistuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
#using asterisk*
item1,item2,item3,*item4=thistuple
print(item1)
print(item2)
print(item3)
print(item4)
#update tuples
#tuple is unchangeable if we need  update tuple we have to use workaround process
#workaround -concer the tuple into a list,change the list,and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"#replacing "apple" with "kiwi"
x = tuple(y)
print(x)
#adding elements-note:tuples doesnot have built-in append()
#by using workaround
numbers=(1,2,3,4,5)
y=list(numbers)
y.append("apple")
numbers=tuple(y)
print(numbers)
#removing items-using workaround
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#deleting whole tuple
del thistuple
#concatenation of tuples-+,*,+=
t1 = (1, 2)
t2 = (3, 4)
#by using '+'
t3=t1+t2
print(t3)
#by using "*"
t4=2*t1
print(t4)
#by using '+='
t1=(1,2)
t1 +=(3,4)
print(t1)
#loop through a tuple-for,while
#for loop
fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)
#while loop
i=0
while i<len(fruits):
   print(fruits[i])
   i=i+1
#tuple methods--only 2 methods exist--count(),index()
#count()-Returns the number of times a value appears in a tuple.
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))
#index()--Returns the index of the first occurrence of a value.
t = (10, 20, 30, 20)
print(t.index(20))#if value is not present rise error






