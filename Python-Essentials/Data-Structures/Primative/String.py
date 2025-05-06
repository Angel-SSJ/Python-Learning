# String
name = 'Bea'
phase = name + "is my name"
name += " is my name"
print(name)

age = str(39)
print("""Beau is
36 
years old
""")

#Stirng Methods
print('beau'.upper())
print('bEAu'.lower())
print('bEAu pERSon'.title())
print('bEAu pERSon'.islower())
print('bEAu pERSon'.isupper())

name = 'Beau'
print(name.lower())  # lower() to get a lower case version of a string
print(name.isalpha())  # isalpha() to check if a string contains only characters and is not empty
print(name.isalnum())  # isalnum() to check if a string contains characters or digits and is not empty-
print(name.islower())  # islower() to check if a string is lowercase
print(name.isupper())  # isupper() to check if a string is uppercase
print(name.isdigit()) # isdigit() to check if a string is a digit
print(name.upper())  # upper() to get an uppercase version of a string
print(name.title())  # title() to get a capitalized version of a string
print(name.startswith('B'))  # startswith() to check if the string starts with a specific substring
print(name.endswith('u'))  # endswith() to check if the string ends with a specific substring
print(name.replace('B', 'J'))  # replace() to replace a part of a string
print(name.split('u'))  # split() to split a string on a specific character separator
print(name.strip())  # strip() to trim the whitespace from a string
print(name.join(' is my name'))  # join() to append new letters to a string
print(name.find('e'))  # find() to find the position of a substring
print('au' in name)

# Escaping Characters
name = 'Be\nau'  # put a backslash in front of the character you want to escape

print(name)
name = 'Be\\au'
print(name)

# USER INPUT
print('USER INPUT')
age = input('What is your age? ')
print('Your age is ' + age)  # print(f'Your age is {age}')
name.isdigit()
