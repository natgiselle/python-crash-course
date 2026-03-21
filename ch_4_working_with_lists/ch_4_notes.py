# list comprehension
nums = [n for n in range(1,13) if n % 2 == 0]

print('list comprehension: even numbers')
print(nums)
for evens in nums:
    print(evens, end = ' ')
print()

# initializing and iterating over a list (without list comprehension)
print("typical list initalization & iteration: even numbers")
nums = []
for num in range(1,13):
    if num % 2 == 0:
        nums.append(num)
        # print(nums[(num//2) - 1]) is a fragile way to index each num in nums but works in this case!
        print(num)

# functions input is a list func(list):
print()
print(f"minimum function: {min(nums)}")
print(f"maximum function: {max(nums)}")
print(f"sum function: {sum(nums)}")
print()
# list slicing
print(f"all values in nums list using nums[:]\n{nums[:]}")
print()
print("can be used to create list copies")
new_nums = nums[:]
print(f"all values in new_nums list using nums[:]\n{nums[:]}")
print()
print("iterating over sliced nums list which only goes up to index 2 which is 3rd item in the list: ")
print("original nums list (6 elements) index from 0 to 5 included: ")
print("for num in nums:")
for num in nums:
    print(num, end = ' ')
print()
print()
print("sliced nums list (2 elements) index from 0 to 2 EXCLUDING element at index 2\n\t\t  it stops at index 2 element 3\nworks just like the range function with START, STOP (EXCLUDED!!), STEP: ")
print("for num in nums[:2]:")
for num in nums[:2]:
    print(num, end = ' ')