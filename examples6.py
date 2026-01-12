'''A list stores prices of items in a shopping cart. Create 
the list and add a new item price at the end.
'''
items_prices=[45,60,70,89,90,100]
items_prices.append(67)
print(items_prices)

'''A list contains daily temperatures of a week.
 Create the list and access the temperature of the last day.
'''
temperature=[56,45,67,89,90]
print(temperature[-1])

'''A school stores roll numbers of students present today in a list. Write a 
program to create the list and display the roll number of the student who came second.
'''
roll_no=[54,55,56,57,58,59]
print(roll_no[1])

'''A weather app stores hourly temperature readings in a list. Write a program to 
extract the temperatures recorded during the morning hours using slicing.
'''
temperatures = [22, 23, 24, 26, 28, 30, 32, 33, 31, 29, 27, 25]
morning_temps = temperatures[6:12]
print(morning_temps)

''' 
'''
songs = ["Shape of You", "Believer", "Perfect", "Levitating"]
songs.insert(0, "Blinding Lights")
print(songs)

'''A delivery app stores distances (in km) of completed trips in a list.
 Write a program to add today’s trip distance and then display the latest distance.
'''
distances = [5.2, 12.5, 8.0, 15.3]
distances.append(4.6)
print(distances[-1])

'''An online course stores quiz scores of a student in a list. 
Write a program to add scores of two new quizzes at once
'''
quiz_score=[65,67,87,90,46,78]
quiz_score.extend([68,89])
print(quiz_score)
