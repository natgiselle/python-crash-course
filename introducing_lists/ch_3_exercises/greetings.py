# Exercise 3-2: Greetings
# Start with the list you used in Exercise 3-1, but instead of 
# just printing each person’s name, print a message to them . 
# The text of each message should be the same, but each message 
# should be personalized with the person’s name .

names = ['aNtHoNy', 'aLoNdRa', 'mAiTe', 'mIcHeLlE', 'cHlOe']

# Below I have the same messages printed but with different 
# changes to the name and concatenation method for practice
print("My friend ", names[0].title(), " is very epic!", sep = "")
print("My friend " +  names[1].upper() + " is very epic!")
print("My friend", names[2].lower(),"is very epic!")
print("My friend " + names[3] + " is very epic!")
print("My friend " + names[4].title() + " is very epic!")
