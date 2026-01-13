#Take a string and print its length without using len()
n="apple"
print(len(n))
#Given a string, convert it to uppercase
txt1="python"
print(txt1.upper())
#Given a string, convert it to lowercase.
txt2="BANANA"
print(txt2.lower())
#Take a string and remove spaces from both ends.
txt3="       python   "
print(txt3.strip())
#Given a string, replace all spaces with underscores (_).
txt4="learning python is fun"
print(txt4.replace(' ','-'))
#Input a sentence and count how many times the letter 'a' appears
txt5=input("enter your string:")
print(txt5.count("a"))
#Check whether a string starts with "Hello".
txt6='Hello! world'
print(txt6.startswith('Hello'))
#Given a string, check whether it contains only digits.
txt7="123python"
print(txt7.isdigit())
#take a string and capitalize only the first character.
print(txt7.capitalize())
#Given a full name string, convert it into title case
name=input("enter your full name:").strip().title()
print(name)
#Take a string and count total number of vowels
txt8="hello, there!"
vowel_count=(txt8.count('a')+txt8.count('e')+txt8.count('i')+txt8.count('o')+txt8.count('u'))
print("total no.of vowels :",vowel_count)
#Input a sentence and find the number of words
txt9=input("enter your sentence:").strip()
count_words=txt9.count(" ")+1
print("no.of words in your string is :",count_words)
#take a string and swap uppercase letters to lowercase and vice versa.
txt10="PyThoN LeRninG Is FuN"
print(txt10.swapcase())
#Given a string, find the last occurrence of a character
txt11="earth have gravity"
#finding last occurence
print(txt11.rfind("a"))
#Take a string and reverse it using slicing
title1="Banana"
print("string reverse:",title1[::-1])
#Given a string, check if it is a palindrome using slicing
print("is given string is palindrome:",title1[:]==title1[::-1])
#Input an email-like string and check if it contains '@' and '.'.
email=input('enter your email ID:')
print('@' in email and '.' in email)

