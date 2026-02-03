#conditional statements in python
#if conditional statement
#if statement is the simplest form of a conditional statement.it executes a block of code if the given condition is true
age=20
if age>=18:
    print("eligible to vote")
#Multiple Statements in if Block
    print("you can vote")
    print("you have full legal rights")
#--->>this space between the if and print statement is indentation
#indentation is used to represent block of code
#Using Variables in Conditions-boolean variables
is_value=True
if is_value:
    print("Welcome")
'''Elif keyword---it allows you to check multiple expressions for true and 
execute a block of code as soon as one of the conditions evaluates to ture.
'''
a=5
b=5
if a>b:
    print('a is greater than a')
elif a==b:
    print("a and b are equal")
#Multiple elif statements
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#elif when you have multiple mutually exclusive conditions to check
#else--it is used statement is executed when the if condition evaluate to False
a=200
b=34
if a<b:
   print("a is smaller than b")
else:
   print("a is greater than b")
#else with elif
a = 345
b = 34
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#if-elif-else chain
temperature = 45
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
#Shorthand if--if you have only one statement to execute,you can put it on the same line as the if statement
a=True
if a: print("Hello,Welcom!!")
#shorthand if-else--writing if-else in same line
#syntax--value_if_true if condition else value_if_false
a = 2
b = 330
print("A") if a > b else print("B")
#it also called conditional expression and ternary operator
#Assigning a value with short hand if-else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#multiple conditions on one line
a=35
b=35
print("A")if a>b else print("=") if a==b else print("B")
#shorthand is used when conditon and actions are simple
#Logical operators--and,or,not
#and operator-True when all conditions are true
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#or operator-- True when one of the condition is true
if a>b or a>c:
   print("in both one condition is true")
#not operator-- reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#combining Multiple operators
age=25
is_student=False
has_discount=True
if (age<18 or age>65) and not is_student or has_discount:
   print("Discount applies!")
#nested if statement-if statement inside if statements
x=42
if x>10:
   print("Above ten")
   if x>20:
      print("and also above 20!")
   else:
      print("but not above 20.")
#instead of nested if we can use logical operator
#the pass statement--a placeholder statement that allows you to write syntactically correct code without executing any operations
a=33
b=200
if b>a:
   pass


