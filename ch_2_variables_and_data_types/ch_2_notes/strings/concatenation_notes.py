# Personal Notes: String Concatenation Methods
# Self-created examples below to test my understanding *not from textbook*.

# Can only concatenate the variable inside {} within the quotes if printing with fstring. 
# Can concatenate the string type variable without fstring in 2 ways.

# Concatenation Method 1: Commas for Automatic Spacing

pikmin_type = "Leaf"
# *Spaces dont matter in between commas*
print("I am the", pikmin_type,"Pikmin!") 

# Will automatically set string seperation as an empty space 
# Unless you edit it like this: 
print("I am the",pikmin_type,"Pikmin!", sep = "")

# The sep paramater is considered a seperator and it controls what character seperates printed items

# Method 2: Addition symbols

# *Spaces dont matter in between addition symbols*
print("I am the" + pikmin_type + "Pikmin!") 

# Will NOT automatically set string seperation
# Unless you edit it like this: 
print("I am the " + pikmin_type + " Pikmin!")

# sep = " " does not work here because it is with addition symbol 
# concatenation since it turns it into one combined string before 
# it can even do any seperation