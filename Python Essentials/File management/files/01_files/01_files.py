import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesnt exist

f = open('names.txt', 'r')
# print(f.read())
# print(f.read(4)) # index 4 = line 4

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()


try:
    f=open('names.txt')
    print(f.read())
except:
    print(f'Error: File  not found, this file doesnt exist')
finally:
    f.close()
    print('\n')

# Append - create the file if it doesnt exist

f = open('names.txt', 'a')
f.write('\n')
f.write('Hello World\n')
f.close()

f = open('names.txt')
print(f.read())
f.close()

print('--------------------------------------------------------------------------------')
# if you want to read the file line by line, we can use the readlines()
with open('names.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


print('--------------------------------------------------------------------------------')
# Write (overwrite)
f = open('context.txt', 'w')
f.write('I delete all of the context\n')
f.close()

f = open('context.txt')
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesnt exist
f = open('name_list.txt', 'w')
f.close()

# Creates the specified file, but returns an error if the file exists
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')


if not os.path.exists('angel.txt'):
    with open('angel.txt', '+x') as file:
        file.write("Angel's File \n ")
        print(file.read())

else:
    print('File already exists')
    with open('angel.txt', 'r') as file:
        print('its content is: \n')
        print(file.read())


# Delete a file
# avoid an error if it doesn't exist
'''
if os.path.exists('angel.txt'):
    os.remove('angel.txt')
else:
    print('File not exists')
'''

with open('more_names.txt', 'r') as file:
    content = file.read()
    print(content)

with open('names.txt', 'w') as file:
    file.write(content)
