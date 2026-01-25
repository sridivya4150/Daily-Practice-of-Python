#removing elements from list--remove(),pop(),clear(),del
#remove-Removes the first occurrence of an element
fruit_basket=['apple','orange','pineapple','orange']
fruit_basket.remove("orange")
print(fruit_basket)
#pop()-Removes the element at a specific index or the last element if no index is specified.
fruit_basket.pop(0)
print(fruit_basket)
fruit_basket.pop()
print(fruit_basket)
#clear()-remove all items
fruit_basket.clear()
print(fruit_basket)
#del--Deletes an element at a specified index
fruit_basket1=['apple','grape','guava','strawberry']
del fruit_basket1[0]
print(fruit_basket1)
#loop through a list-for,while
vegetables=['tomato','potato','cucumber','cabbage']
#loop through a list by using for loop
for x in vegetables:
    print(x)
#loop through a list by using while loop
i=0
while i < len(vegetables):
    print(vegetables[i])
    i=i+1
#looping using list comprehension
my_list=[34,56,5,7,8]
comprehension_list=[print(x) for x in my_list]
#its create new list
#list comprehension with if condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#creating new list using for
numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    squares.append(x * x)
print(squares)
#sorting list items--sort(),sorted()
#sort()--sorts the original list alphanumerically,ascending by default
numbers1=[8,4,56,72,31]
numbers1.sort()
print(numbers1)#o/p:[4,8,31,56,72]
#sorting alphabetically
fruit_basket=["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_basket.sort()
print(fruit_basket)
#sort descending ---using reverse keyword argument
numbers2=[32,45,61,67,90]
numbers2.sort(reverse = True)
print(numbers2)
fruit_basket1=["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_basket1.sort(reverse = True)
print(fruit_basket1)#sorts capital letter being sorted before lower case letters
#by using sorted()--returns the ordered list without modifying the original list 
numbers = [5, 2, 8, 1, 3]
a = sorted(numbers)
print(a)
print(numbers)
#copying lists--copy(),using list(),slice operator
#by using copy
lst = ['item1', 'item2']
lst_copy = lst.copy()
print(lst_copy)
#by using list()
lst_copy1=list(lst)
print(lst_copy1)
#by sing slice operator
lst_copy2=lst[:]
print(lst_copy2)
#joining  lists--by using operator'+',append(),extend()
#by using plus operator '+'
list1=['a','b','c','d']
list2=[1,2,3]
list3=list1+list2
print(list3)
#by using append()--by only using loop 
list4=['e','f','g','h']
list5=[6,7,8,9]
for x in list5:
    list4.append(x)
print(list4)
#by using extend()
list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]
list6.extend(list7)
print(list7)
#list methods--append(),clear(),copy(),count(),extend(),index(),insert(),pop(),remove(),reverse(),sort()




