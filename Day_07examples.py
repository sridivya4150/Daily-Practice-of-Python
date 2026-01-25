'''A shopping cart stores prices of items in a list.
 Create the list, add a new item price, remove one price, and display the updated cart.
'''
cart = [45, 60, 80, 120]
cart.append(90)
cart.remove(60)
print(cart)
'''A list contains daily temperatures of a week. 
Create the list and display the highest and lowest temperatures
'''
temps = [28, 30, 27, 31, 29, 26, 32]
print(max(temps))
print(min(temps))
'''A school stores roll numbers of students present today in a list.
 Create the list and display the roll numbers of the first three students.
'''
roll_numbers = [101, 102, 103, 104, 105]
print(roll_numbers[:3])
'''A user’s login details are stored in a list in the order:
 username, email, phone number, password. Create the list and unpack 
 these details into separate variables.
'''
login_details = ["madhu", "madhu@gmail.com", "9876543210", "pass123"]
username, email, phone, password = login_details
print(username, email, phone, password)
'''A fitness app stores daily step counts in a list. Create the list,
 add today’s steps, and display the total number of days recorded.
'''
steps = [4500, 6200, 7100]
steps.append(8000)
print(len(steps))
'''A movie playlist stores movie names in a list.
 Create the list, insert a new movie at a specific
   position, and reverse the playlist.
'''
movies = ["Avatar", "Titanic", "Inception"]
movies.insert(1, "Interstellar")
movies.reverse()
print(movies)
'''A list stores marks obtained by a student in different subjects.
 Create the list, sort the marks, and remove the lowest mark.
'''
marks = [78, 85, 62, 90, 55]
marks.sort()
marks.pop(0)
print(marks)
