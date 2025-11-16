# Exercise 3-3: Your Own List 
# Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, 
# such as “I would like to own a Honda motorcycle .”

# There will be two lists where one is for the color of car
# and the other is the specific car model.

# Below I am practicing the change in quotation just to
# get used to the variations again.
colors = ['cool cyan','hot pink','pastel yellow']
cars = ["volkswagen beatle","Honda S2000","Mazda Mx5 Miata"]

print("I would like to own a " + colors[2] + " " + cars[0].title() + " car.")
print("I would like to own a",colors[1],cars[1],"car.")
print("I would like to own a ",colors[0]," ",cars[2]," car.", sep = "")
