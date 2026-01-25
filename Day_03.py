#strings 
#multiline string is created by using triple single(''') or double quotes("")
#lenth of the string use len()
title=" learning python is fun"
print(len(title))
#multiline string
title1=''' learning python
            is so nice'''
print(title1)
#STRING CONCATENATION
a='hello'#assigning a string to variable
b=input("enter you name:")#taking string as input
#by using + operator
print(a+" "+b)
#by using f string
print(f"{a} loves {b}")
#by using format()
print('{} likes {}'.format(a,b))
#by using join()
table=['food','delicious','yummy']
print(" ".join(table))
#ESCAPE SEQUENCE IN STRINGS
print('hello\nworld')#print the word after \n in next line
print('hello \t world')#print one tab space between two words
print('hello\\world')#adds backslash
print("sita \'loves\' rama")#adds the single quote to that word
print("i want become a \"best\" for myself")#adds the double quote to that word
#STRING FORMATING
first_name='brad'
second_name='Pitt'
#old method for formating
print("%s %s is nice person"%(first_name,second_name))
#new method for string formating
print("{} {} is a bad person".format(first_name,second_name))
#string interpolation
#f-strings
print(f"{a} hated {b}")
x=10
y=20
print(f'{x}+{y}={x+y}')
#STRINGS AS SEQUENCES FO CHARACTERS/PYTHON ACCESSING METHODS
#unpacking character
word='python'
a,b,c,d,e,f=word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#Accessing Character in String by Index
#for positive index----left to right
a1=word[0]
print(a1)
print(word[1])#like this also we can access
#for negative index--right to left index
'''0    1   2   3   4   5----posite index
   p    y   t   h   o   n   
  -6   -5  -4   -3  -2  -1 -----negative index'''
b1=word[-1]
print(b1)
print(word[-6])
#slicing in python strings
language=' elephant '
#string repeatation
print(language*4)
#for positive
first_slice=language[0:4]#starting at 0 and upto 4 but not including 4
second_slice=language[5:7]
print(first_slice)
print(second_slice)
print(language[0:3])#like this also we can slice and access the string
#for negative
first_slice1=language[-8:-4]
second_slice1=language[-3:-1]
print(first_slice1)
print(second_slice1)
print(language[-8:-1])
print(language[8:])
print(language[:])
#REVERSING A STRING
print(language[::-1])
#skipping characters while slicing
print(language[0:3:2])
#reversing string by using reversed()
print("".join(reversed(language)))
#loops through string
apple="apple"
for x in apple :
    print(x)
#check string
txt='the best things in life are free!'  
print("free" in txt)  
#not in
print("expensive" not in txt)
#string is immutable(they cannot be changed after they are created)
s="python is fun"
s='P'+s[1:]#creating new string
print(s)
#deleting string
del s

#--------------------------------------------------
#string methods
title='i love learning python'
#capitalize()-converts the first letter of the string into capital letter(a--->A)
print(title.capitalize())
#casefold()-covets string into lower case
title1='I Love Learning Python'
print(title1.casefold())
#lower()-converts string into lower cases
print(title1.lower())
'''Here, we observe that these two methods do the same thing,
i.e., converting a string into lowercase. However,
lower() is mainly suitable for English and is not very useful
when Unicode characters are involved. casefold() is stronger
and can handle Unicode characters, so it is safer 
and better than lower() in most cases'''
#center()-it alien the word in center (Returns a centered string)
title2='Python'
print(title2.center(20,"*"))#syntax-->string.center(length,character)
# It is our choice whether to give a fill character or not.
# By default, it uses a space (" ") as the fill character.
print(title2.center(20))
#count()-it counts no.of times a specified value occurs in the string
title3='learning python is fun'
print(title3.count('n'))
#syntax-->string.count(value,start,end)
print(title3.count('n',3,10))
#encoded()-converts the string into bytes by using a specified encoding
title4="My name is Ståle"
print(title4.encode())
#syntax-->string.encode(encoding=encoding,errors=errors)
print(title4.encode(encoding='ascii',errors="ignore"))
#endswith()-returns true if the string ends with the specified value
#sytax-->string.endswith(value,start,end)
# By default, the starting index of a string is 0.
# By default, the ending index is the length of the string.
title5='i like apples'
print(title5.endswith('s'))
print(title5.endswith('lik',1,5))
print(title5.endswith('a'))
#upper()-converts all characters to uppercase.
s1= "python"
print(s1.upper())
#title()-capitalizes the first letter of every word in a string
s2= "python is easy"
print(s2.title())
#strip()-emoves spaces from both the beginning and end of the string.
s3= "  hello  "
print(s3.strip())
#lstrip()-removes only left-side spaces
print(s3.lstrip())
#rstrip()-removes only right-side spaces
print(s3.rstrip())
#replace()-replaces one substring with another and returns a new string
s4= "I love Java"
print(s4.replace("Java", "Python"))
#find()-This method finds the index position of a substring.#
# If not found, it returns -1 (no error).
s5= "python"
print(s5.find("th"))
#find have rfind() &lfind()
#index()-This works like find() but raises an error if the substring is not found.
print(s5.index("p"))
#startswith()-This method checks whether a string starts with a given value.
print(s5.startswith("p"))
#isalpha()-Returns True if the string contains only alphabets
print(s5.isalpha())
#isdigit()-Returns True if the string contains only digits.
print("123".isdigit())
#isalnum()-Returns True if the string contains alphabets and digits only.








