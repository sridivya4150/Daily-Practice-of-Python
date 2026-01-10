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
#

