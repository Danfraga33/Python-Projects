import random

names_string = ['Angela', 'John', 'Dan']

# names = names_string.split(" ")

num_items = len(names_string)

random_choice = random.randint(0, num_items - 1)

person_who_pays = names_string[random_choice]
# print(names_string.split(', ')

print(person_who_pays + " is going to buy the meal today!")
