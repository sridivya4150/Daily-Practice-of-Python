#Create a list of numbers and print the first, last, and middle elements.
numbers=[56,78,9,54,23]
first,*middle,last=numbers
#printing first element
print(first)
#printing middle elements
print(middle)
#printing last element
print(last)
#Reverse a list without using the reverse() method.
lst=['hello',90,'89.8']
#revering the list by using slicing
print(lst[::-1])
#Add five elements to an empty list using a loop.
empty_list=[]
lst1=[90,78,56,34,23]
for i in lst1:
    empty_list.append(i)
print(empty_list)
#Remove all occurrences of a specific element from a list
numbers=[42,54,78,90,100,23,42]
value=42
numbers=[x for x in numbers if x != value]
print(numbers)
#Find the sum and average of elements in a numeric list.
number1=[10,20,30,40]
total=sum(number1)
average=total / len(number1)
print("Sum:",total)
print("Average:",average)
#Print only even numbers from a list using list comprehension.
list=[1,2,3,4,5,6]
even_number=[x for x in list if x%2==0]
print(even_number)
#Sort a list in descending order without using sort().
numbers = [4, 1, 6, 3, 2]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)
#Copy one list into another and prove they are different objects.
list1 = [1, 2, 3]
list2 = list1.copy()
print(list1 == list2)   
print(list1 is list2) 
