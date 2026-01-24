#swapping of two number(simple)
a,b=2,3
a,b=b,a
print(a)
print(b)
#counting character in the string
title= 'I am learnig python'
print(len(title))
#type of the variable
print(type(title))
#converting base using int() 
print(int('110', 2))
print(int('12', 8))
print(int('1A', 16))
#Tea Stall bill
tea_price=int(input("enter the price of the tea:"))
numof_cups=int(input("enter the no.of cups wants:"))
bill=tea_price*numof_cups
print("Total bil:",bill)
# Digital Clock
total_seconds = int(input("Enter number of seconds: "))
minutes = total_seconds // 60
seconds_rem = total_seconds % 60
print(minutes, "min", seconds_rem, "sec")
