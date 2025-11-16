# What is a List?
# Lists Lesson 1: Accessing Elements in a List

# The list is enclosed with square brackets
bicycles = ["trek","cannondale","redline","specialized"]

# Putting -1 as the index value will print the last item in a list so its like counting backwards from right to left
print("\n\nIndex -1")
print(bicycles[-1]+"\n")
print("Index -2")
print(bicycles[-2]+"\n")

# The all elements in the list are fully printed with the statement below: 
print("All Elements:\n", bicycles)

# The index is the positioning of an element which starts from 0
# For example, the first element (item) in the list would be at index 0 which will print trek
print("\nIndex 0")
print(bicycles[0])

# The index bracket can also help change details of the list as elements in a list are mutable, unlike strings

# The title() function puts the element in title case
print("\nIndex 0 in Title Case")
print(bicycles[0].title())

# Lists Lesson 2: Index Positions start at 0 not 1

# Prints second element
print("\nIndex 1")
print(bicycles[1])

# Prints fourth element
print("\nIndex 3")
print(bicycles[3],"\n")

# Lists Lesson 3: Using Individual Values from a List

# The 4th element at index 3 is instead set equal to motorized
print()
bicycles[3] = "motorized"
print(bicycles[3])

message = "my first bike was a " + bicycles[2].title() + " model."
print(message)