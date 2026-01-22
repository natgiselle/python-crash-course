# Changing, Adding, and Removing Elements
# Lists Lesson 4: Modifying Elements in a List
print("motorcycles List: ")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[0] = 'honda'
print(motorcycles)

# Lists Lesson 5: Adding Elements in a List
# The append() method allows you to add a new element to the end of a list.
motorcycles.append('harley davidson')
print(motorcycles)

# The append() method also works with empty lists.
print("\nmotorcycles_2 List: ")
motorcycles_2 = []
motorcycles_2.append("honda")
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
print(motorcycles_2)

# Lists Lesson 6: Removing Elements from a List
# The del statement will remove an element in a list of its specific index position.
# Deletes the first element at index position of 0 in the motorcycles_2 list.
del motorcycles_2[0]
print(motorcycles_2)

del motorcycles_2[1]

# Lists Lesson 7: Popping items from any Position in a List
# The pop() method will remove an item in a list at any index position by including its index within the parentheses not brackets.
# The popped item can be used if stored in a variable but it will no longer be stored in the list.
print("motorcycles List: ")
first_owned = motorcycles.pop(0)
print(motorcycles)
print("My first owned motorcycle was a " + first_owned.title() + ".")

# Lists Lesson 8: Removing an Item by Value
# The remove() method allows you to remove an item based on the first instance (occurence) of its value if you arent aware of which index position it has.
motorcycles.remove('yamaha')
print(motorcycles)


