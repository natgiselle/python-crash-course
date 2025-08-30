# Numbers Lesson 1: Integers
# You can add (+) subtract (-) multiply (*) and divide (/) integers in Python
x = 3
y = 2
# Self-created examples below to test my understanding *only the numbers used are from textbook*.
# Use str() function to convert integer or float type into a string so that it can be concatenated in print statements
print("Operations with Integers:\n")

# Integer addition outputs integer value
z = y + x
print("2 + 3 = " + str(z) + " integer addition operation")

# Integer subtraction outputs integer value
z = x - y
print("3 - 2 = " + str(z) + " integer subtraction operation")

# Integer multiplication outputs integer value
z = y * x
print("2 * 3 = " + str(z)+ " integer multiplication operation")

# Integer exponential outputs integer value 
z = y ** x
print("2 ** 3 = 2^3 = " + str(z)+ " integer exponent operation")

# The / operator is division WITHOUT floor
# Outputs a float value when using integers
z = x / y
print("3 / 2 = " + str(z) + " integer division WITHOUT floor operation")

# The // operator is division WITH floor 
# Outputs an integer value when using integers
z = x // y
print("3 // 2 = " + str(z) + " integer division WITH floor operation")

print("--------------------------------------------------------------------\nOperations with Floats:\n")

# Use float() function to convert integer into a float type
# Variable a is float type of int type variable x now (3 into 3.0 after type conversion)
a = float(x)

# Variable b is float type of int type variable y now (2 into 2.0 after type conversion)
b = float(y)

# Float addition outputs float value as long as one of numbers is of float type
c = b + a
print("2.0 + 3.0 = 2.0 + 3 = 2 + 3.0 = " + str(c) + " float addition operation 1")

# Use the int() function to convert a float into an int type.
c = float(int(b) + int(a))
print("2.0 + 3.0 = 2.0 + 3 = 2 + 3.0 = " + str(c) + " float addition operation 2")

# Float addition outputs float value as long as one of numbers is of float type
c = a - b
print("3.0 - 2.0 = " + str(c) + " float subtraction operation")

# Float multiplication outputs float value as long as one of the numbers is of float type
c = a * b
print("3.0 * 2.0 = 3.0 * 2 = 3 * 2.0 = " + str(c) + " float multiplication operation")

# Float exponential outputs float value as long as one of the numbers is of float type
c = b ** a
print("2.0 ** 3.0 = 2.0^3 = 2^3.0 = " + str(c) + " float exponent operation")

# Float division WITHOUT floor
# When using the / operator with a float type value, it outputs a float, not an integer
c = a / b
print("3.0 / 2.0 = " + str(c) + " float division WITHOUT floor operation")

# Float division WITH floor
# The // operator rounds down to the nearest whole number but keeps float type
c = a // b
print("3.0 // 2.0 = " + str(c) + " float division WITH floor operation")




