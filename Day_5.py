#Lists
#creating a list---by using [],list()
#by using--[]
fruits=["apple","banana","cherry"]
#printg list as output
print(fruits)#list is ordered,changeable,and allow duplicate values
#by using list()
veggies=list(('carrot','tomato','potato'))
print(veggies)
print(type(veggies))
#creating empty list
empty_list=[]
print(empty_list)
#determining lenth of the list--len()
print("the length of the fruits:",len(fruits))
print("the length of the veggies:",len(veggies))
print("the length of the  empty_list:",len(empty_list))
#list allows duplicate values
marks=[34,56,76,87,90,56]
print(marks)
#taking list as user input
user_list=list(input("enter your list:").split())
print("the list your entered is:",user_list)
print("type of user_list",type(user_list()))
print("the length of your list is:",len(user_list))
#list is a collection data type it can have any data type
#list with mixed data types
list1 = ["abc", 34, True, 40, "mango"]
print(list1)
#determining list elements type
print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))
print(type(list1[3]))
print(type(list1[4]))
#Access Items-by using index----positive/negative
print(" accessing first element in the list1:",list1[0])#using positive index
print("accessing last element in the list1:",list1[-1])#using negative index
#slicing items from a list-----syntax:list[start : end : step]
#List slicing is used to get a part (sub-list) from an existing list
print(list1[0:2])#using positive index
print(list1[:])
print(list1[-5:])#using negative index
#reversing a list using negative index
print(list1[::-1])
#change item value
numbers=[2,3,4,5,6,7]
numbers[0]="apple"
print(numbers)
#changing a range of item values
numbers[1:3]=['bad','good']
print(numbers)
#if we insert more than we replace, it add in the list along with all
numbers[1:3]=['bad','good',90,0]
#When you insert fewer elements than you replace, the list shrinks
numbers = [2, 3, 4, 5, 6, 7]
numbers[1:4] = [99]
print(numbers)
#unpacking list items
first_item, second_item, third_item, *rest = numbers
#here,*variable is Extended Iterable Unpacking-
'''Extended unpacking allows one variable (with *)
 to collect multiple remaining values into a list while unpacking an iterable.'''
print(first_item)     
print(second_item)  
print(third_item)     
print(rest)   
   


