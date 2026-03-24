# Exercise 4.10: Slices
'''
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

Print the message, The first three items in the list are:
Then use a slice to print the first three items from that program's list.

Print the message, Three items from the middle of the list are:
Use a slice to print three items from the middle of the list.

Print the message, The last three items in the list are:
Use a slice to print the last three items in the list 
'''

# modifying list from 4_2_animals.py
animals = ['cat', 'dog', 'bird', 'hamster', 'guinea pig', 'turtle', 'goldfish', 'crab', 'snail', 'frog']

print("The first three items in the list are:")
for animal in animals[:3]:
    print(f"  {animal}")

print("\nThree items from the middle of the list are:")
for animal in animals[3:6]:
    print(f"  {animal}")

print("\nThe last three items in the list are:")
for animal in animals[-3:]:
    print(f"  {animal}")