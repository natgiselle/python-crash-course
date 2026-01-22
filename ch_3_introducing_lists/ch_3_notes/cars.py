# Organizing A List
# Lists Lesson 9: Sorting a List Permanently with the sort() Method

# The sort() method organizes a list into alphabtical order
cars=['bmw','audi','toyota', 'subaru']
print("Original cars List:")
cars.sort()

print("Changes order of the list permanently")
print(cars,"\n")

print("Can also do reverse order from Z-A rather than A-Z")
cars.sort(reverse=True)
print(cars,"\n")

# Lists Lesson 10: Sorting a List Temporarily with the sorted() Function
cars_2=["mazda","lexus","suzuki","honda"]
print("Original cars_2 List:\n" + str(cars_2))

# The sorted() method allows for a list to be displayed in a particular order without affecting the order of the list
print("Sorted cars_2 List:\n",cars_2.sort())

# Printing a List in Reverse Order
print(cars_2)

# The reverse() method reverses the original order of the list
cars_2.reverse()
print(cars_2)

# Finding the length of a list
cars_2_length = len(cars_2)
print(cars_2_length)
