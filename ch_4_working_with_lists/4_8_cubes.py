# Exercise 4.8: Cubes
'''
A number raised to the third power is called a cube.
For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
and use a for loop to print out the value of each cube.
'''
# avoid list comprehension in this specific exercise
'''
 cubes = [n ** 3 for n in range(1,11)] # must match the same variable for ex: num for num in blank pet for pet in blank
for num in cubes: # here its just iterating over to print the list items (cubes)  so it does NOT give error if you use a different name for the elements in the list ( different scope)
    print(num)
'''

cubes = []
for num in range(1,11):
    cube = num ** 3
    cubes.append(cube)
    print(cubes[num-1]) # must be index of num-1 because it would then try to find an 11th item with index 10 which doesnt exist as there is only 10 items
