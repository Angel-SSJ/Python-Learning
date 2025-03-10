# WITH
'''is very helpful to simplify working with exception handling
for examble when working with files each time we open a file wer must remember to close it with makes the process more transparent'''

filename = '/Users/Angel/test.txt'
try:
  file = open(filename,'r')
  content=file.read()
  print(content)
finally:
  file.close()

with open(filename, 'r') as file:
  content = file.read()
  print(content)

''' using with  it is going to make sure to automatically close the file at the end in others words we have built--in implicit exception handling as close '''