# Exercise 3-7: Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time 
# for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-6. 
# Add a new line that prints 
# a message saying that you can invite only two people for dinner.
guests=["Chappell Roan","Ariana Grande"]
message=" you are invited to dinner!"
guests.insert(0, "Pharrell Williams")
guests.insert(2, "Steve Lacy")
guests.append("Mac Miller")
# Use pop() to remove guests from your list one at a time until only 
# two names remain in your list. 


# Each time you pop a name from your list,print a message to that 
# person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list,
# letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an 
# empty list. 
# Print your list to make sure you actually have an empty list at the
# end of your program.
print("Sorry, I can only invite two people for dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"{removed_guest} I am sorry to inform you that you cannot be invited due to minimal space.")
    
for celebrity in guests:
    print(f"Hello {celebrity}! Luckily, your spot at the dining table has been saved.")

del guests[0]
del guests[0]
print(guests)