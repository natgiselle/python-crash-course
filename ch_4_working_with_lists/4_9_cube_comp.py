# Exercise 4.9 Cube Comprehension
'''
Use a list comprehension to generate a list of the first 10 cubes.
'''
# [print(cube ** 3) for cube in range(1, 11)] if it wasnt asking to store values in a list you could do print
cubes = [cube ** 3 for cube in range(1, 11)] # are also allowed to use print function when doing list comprehension but WONT save the values in the list!!
for num in cubes:
    print(num)