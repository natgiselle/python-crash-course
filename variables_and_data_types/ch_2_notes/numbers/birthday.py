# Numbers Lesson 3: Avoiding Type Errors with the str() Function
# Often, you’ll want to use a variable’s value within a message. For example,
# say you want to wish someone a happy birthday. You might write code
# like this:
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)
# Outputs Type Error
# message = "Happy " + age + "rd Birthday!"
#           ~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

# Proper usage of str() function is:
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

