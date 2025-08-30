# Strings Lesson 1: Changing Case in a String with Methods

# The title() method capitalizes the first character of each word written when a space is placed

name = "ada lovelace"
print(name.title())

# The upper() method creates an output of your string with all characters in uppercase
print(name.upper())

# The lower() method creates an output of your string with all characters in lowercase
print(name.lower())

# Strings Lesson 2: Combining or Concetating Strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name

print(full_name)

# Strings Lesson 3: Adding Whitespace to Strings with Tabs or Newlines

# Whitespace refers to any nonprinting character such as space, tabs, and end of line symbols
# The \t is a tab escape sequence
print("\tPython")

# The \n is a newline escape sequence
print("\nPython")

# These escape sequences can be use in a single print statement multiple times
print("Languages:\nPython\nC\nJavaScript")

# Strings Lesson 4: Stripping Whitespace

favorite_language = ' python '
print(favorite_language)

# The rstrip() method ensures no whitespace exists at the right end of the string
print(favorite_language.rstrip())

# The lstrip() method ensures no whitespace exists at the left end of the string
print(favorite_language.strip())

# The strip() method ensures no whitespace exists to both ends of the string
print(favorite_language.strip())

# Strings Lesson 5: Avoiding Syntax Errors with Strings

# Single '' Quotes: Apostrophy Error
# Will output SyntaxError: unterminated string literal
# single_quote_message = 'One of Python's strengths is its diverse community.'

# Has invalid syntax indicating that it doesnt consider it as valid Python code
# print(single_quote_message)

# Double "" Quotes: No Error

# Will output string correctly without the Syntax Error 
double_quote_message = "One of Python's strengths is its diverse community."

# Use double "" quotes as common practice to avoid apostrophe syntax errors
print(double_quote_message)

# Double Quotes: Including Quotations Inside a String Error
# Will output SyntaxError: invalid syntax
# quote = ""hi""

# In order to avoid this error you must do the single ''quotes and inside 
# use the double quotes so that it prints the double quotes as well
quote = '"hi"'
print(quote)







