#function-a function is a reusable block of code or programming statements designed to perform a certain task
#to define function or declare function we use def keyword
def addition():
    a=2
    b=3
    sum=a+b
    print(sum)
addition()
#return values-function can send data back to the code that called them using the return statement.
def get_greeting():
    return "hello from a function"
message = get_greeting()
print(message)
#calling function multiple times
def fruits():
    print("the basket is full")
fruits()
fruits()
fruits()
#convert temperature from fahrenheit to celsius
def temperature_conversion(fahrenheit):
    return (fahrenheit-32)*5/9
print(temperature_conversion(65))
print(temperature_conversion(79))
print(temperature_conversion(50))
#we can use return value directly
def welcome():
    return "hii there welcome!!!"
print(welcome())
#if function doesnot have a return statement,it returns none by default
#function defiitions cannot be empty.
#creating function without any code-using pass
def my_function():
    pass
#Arguments-information can be passed into functions as arguments
def arg(fname):
    print(fname + ",how are you?")
print(arg("emil"))
print(arg("thonas"))
print(("jake"))
#parameter -it is the variable listed inside the parentheses in the function definition
#argument-it is the actual value that is sent to the function when it is called
def fun(name):       #name is a parameter
    print("hello",name)
fun("jake")          #'jake' is an argument
#number of arguments
#functiojn must be called with the correct number of arguments
def checking_funti(fname,lname):
    print(fname + " " +lname)
checking_funti("jake","blommy")
#if we try to call the function with the wrong number of arguments ,you will get an error
#default parameter values---we can assign default parameter values .if the function is called without an argument,it uses the default value
def default_values(name="friend"):
    print("Hello",name)
default_values("james")
default_values()
#keyword arguments-we can send arguments with the key=value syntax.it can be often shortened to kwargs in python documentation
def animal(type,name):
    print("i have a",type)
    print("my",type + "'s name is",name)
animal(type="dog",name="lucy")
#for keyword arguments order doesn't matter
animal(name="jen",type="cat")
#positional arguments-call a function with arguments without using keyword,they are called positional arguments
animal("rat","buddy")
#switching the order changes the result
animal("lucy","dog")
def funt(a,b):
    return a+b
result=funt(4,5)
print(result)
#specifying that function can have only positional arguments
def greeting(name,/):
    print("Hello",name)
greeting("john")#if we specify the keyword arguments it shows error
#like that we can only take keyword-only arguments by given * before the parameters
def greetings(*,name):
    print("Hello",name)
greetings(name="mary")
#combining positional-only and keyword only
def addit(a,b,/,*,c,d):
    return a+b+c+d
result=addit(5,10,c=15,d=8)
print(result)
#args and kwargs
def animal(*name):
#args becomes a tuple containing all the passed arguments
    print("Type:",type(name))
    print("i have a pet",name[1])
    print("i have a pet",name[0])
animal("dog","cat","sheep","rat")
#combining *args with regular arguments
def  my_fun(greeting,*names):
    for name in names:
        print(greeting,name)
my_fun("hello","emil","tobias","linus")
#arbitrary keyword arguments-**kwargs--it allows function to take any number of arguments
def my_func(**name):
    print("hello,my name is :"+name["fname"])
my_func(fname="sean",lname="paul")
#unpacking arguments--using *,** operators
def unpack(a,b,c):
    return a+b+c
numbers=[1,2,3]
result=unpack(*numbers)
print(result)
def unpacking(fname,lname):
    print("Hello",fname,lname)
person={"fname":"emil","lname":"refsnes"}
unpacking(**person)










