# Exercise 3.9: Dinner Guests

'''
Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
use len() to print a message indicating the number of people you are 
inviting to dinner.
'''

people = ["Sabrina Carpenter", "Ariana Grande", "Kali Uchis"]
message = " I would like to invite you to dinner!"
people[0] = "Chappell Roan"
for person in people:
    print(person + message)
print(f"I am inviting {len(people)} guests to dinner!")