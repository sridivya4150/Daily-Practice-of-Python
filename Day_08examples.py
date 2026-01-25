#Create a tuple with 5 elements and print it
tuple1=(1,2,3,4,5)
print(tuple1)
#Find length of a tuple
t = (10, 20, 30, 40)
print(len(t))
'''An e-commerce app stores product dimensions as (length, width, height).
Find the volume of the product.'''
dimensions = (10, 5, 2)
volume = dimensions[0] * dimensions[1] * dimensions[2]
print(volume)
'''A movie rating system stores ratings as (user_id, movie_id, rating).
Find the average rating from multiple such tuples.
'''
ratings = ((1,101,4), (2,101,5), (3,101,3))
avg = sum(r[2] for r in ratings) / len(ratings)
print(avg)
'''Daily temperatures of a week are stored in a tuple.
Find the highest and lowest temperature.
'''
temperature=(30,32,35,31,29,34,33)
print("max temperature:",max(temperature))
print("min temperature:",min(temperature))
'''An online order status is stored as (order_id, status).
Update the status from "Placed" to "Delivered".
'''
order = (1234, "Placed")
order = (order[0], "Delivered")
print(order)







