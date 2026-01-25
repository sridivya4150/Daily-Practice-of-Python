#A list stores the names of five students in a classroom. Create the list and access the first and last student names.
students_list=['jennie','jimmy','justin','rian','flynn']
print("the first student namen in the list:",students_list[0])
print("the last student name in the list:",students_list[-1])
#A list contains daily temperatures recorded for a week. Create the list and slice the temperatures of the first three days.
temperature=[90,78,83,45,90,93,89]
print('the temperature of the first three days:',temperature[0:4])
#A list stores prices of items in a shopping cart. Create the list and access the price of the third item.
store_prices=[70,120,250,30]
print(store_prices[2])
'''A list stores login details of a user in the order:
 username, email, phone number, password. Create the list 
and unpack these details into separate variables'''
user_login=['john','john@gmail.com',5645678923,123456]
user_name,email,phone_number,password=user_login[0],user_login[1],user_login[2],user_login[3];
print('user name:',user_name)
print('email:',email)
print('phone number:',phone_number)
print('password:',password)
'''A list contains marks obtained by a student in six subjects.
 Create the list, slice the first four marks,
 and access the second mark from the sliced list.'''
student_marks=[45,42,41,40,39,47]
sliced_list=student_marks[1:5]
print(sliced_list[2])


