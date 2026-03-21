# Exercise 4.6: Odd NUmbers
'''
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number.
'''
# can also do
# odd_nums = list(range(1,21,2)) is faster
# odd_nums = [num for num in range(1,21) if num % 2 != 0] is without using step
odd_nums = [num for num in range(1,21,2)] # is typical when using conditionals as shown above
for num in odd_nums:
    print(num)