# EXCEPTIONS
'''exceptions are errors that occur during the execution of a program'''
'''try:
  some lines of code
except <ERROR1>:
  handler <ERROR1>
except <ERROR1>:
  handler <ERROR1>
except:
  if you dont specify the error it will handle all errors 
else:
  no exceptions were raised, the code ran successfully

finally:
  do something in any case
'''

try:
  result = 2 / 0
except ZeroDivisionError:
  print('Cannot divide by zero!')
finally:
  result = 1

print(result)

try:
  raise Exception('An error!')
except Exception as error:
  print(error)


class DogNotFoundException(Exception):
  pass  #we must use it when we define a class without methods or a function without code


try:
  raise DogNotFoundException()
except DogNotFoundException:
  print('Dog not found!')