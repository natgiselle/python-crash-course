# Exercise 3-6: More Guests
# You just found a bigger dinner table, so now more space 
# is available. 
# Think of three more guests to invite to dinner.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
# Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print statement to the end of your program informing people
# that you found a bigger dinner table.
guests=["Chappell Roan","Ariana Grande"]
message=" you are invited to dinner!"
# The insert () method has 2 arguements first is the index in which
# you want to insert the element followed be a comma and second arguement 
# that is what you want for that element a string, integer, etc.
guests.insert(0, "Pharrell Williams")
guests.insert(2, "Steve Lacy")
guests.append("Mac Miller")

# Lists can have a combination of various types for elements but if 
# printing you must convert it to a string so that the for loop works 
# when inserting an integer.
# guests.insert(2, 365)
for celebrity in guests:
    print(str(celebrity) + message)
print("Because I found a bigger dining table, you are all able to join.")