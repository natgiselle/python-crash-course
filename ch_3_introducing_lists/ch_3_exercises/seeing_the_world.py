# Exercise 3-8: Seeing the World
# Think of at least five places in the world you’d like to visit.
# Store the locations in a list.
# Make sure the list is not in alphabetical order.
# Print your list in its original order. 
# Don’t worry about printing the list neatly, just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. 
# Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. 
# Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

places = ["Colombia","Spain","Japan","Italy","Brazil"]

# The sorted() function which means it takes arguements inside of the parenthesis 
# reverse() and sort() are methods which means they are called with a dot following
# The object for example: object.method()
# Not all methods can take parameters such as reverse() but sort() can take an arguement such as object.sort(reverse = True)

# # returns a new sorted list without modifying the original
print("Origintal list:\n", places)
print("\nSorted List:\n",sorted(places))
print("\nUnchanged Original List:\n", places)
print("\nReverse Sorted List:\n",sorted(places, reverse = True))
print("\nUnchanged Original List:\n", places)
places.reverse()
print("\nReverse Order List:\n", places)
places.reverse()
print("\nUnchanged Original List:\n", places)
places.sort()
print("\nSort List:\n",places)

# .reverse() and .sort() modify the original list in place and return None
# When you print or store the method call itself (e.g., print(list.sort())), 
# You get None because that's what the method returns
# To see the actual changes, print the list name directly without the method
# Example: 
# list.sort() or list.reverse() then print(list) ✓ 
# NOT print(list.sort()) or  print(list.reverse()) ✗



places.sort(reverse = True)
print("\nSort List:\n",places)