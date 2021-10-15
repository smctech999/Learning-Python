
# In this program we'll learn about string manipulation.

# First we'll assign some variables.

name = 'ada lovelace'
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
favorite_language = 'python '
favorite_language2 = ' python '
famous_quote = f'Yoda once said, "Do or do not. There is no try."'	

# Next are some examples of how to manipulate strings.

# Case manipulation
print(name.title())
print(name.upper())
print(name.lower())
print(full_name)
print(f"Hello, {full_name.title()}!")
print(message)

# Whitespace manipulation
print("Python")
print("\tPython")
print("Languages: \nPython\nC\nJavaScript")
print("Languages\n\tPython\n\tC\n\tJavaScript")
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language2.rstrip())
print(favorite_language2.lstrip())
print(favorite_language2.strip())

# Using Quotation marks
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
print(famous_quote)
