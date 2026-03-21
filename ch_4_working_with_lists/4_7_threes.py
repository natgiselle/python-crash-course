# Exercise 4.7: Threes
'''
Make a list of the multiples of 3 from 3 to 30.
Use a for loop to print the numbers in your list.
'''
numbers = [n for n in range(3,31) if n % 3 == 0]
for mul_of_3 in numbers:
    print(mul_of_3)