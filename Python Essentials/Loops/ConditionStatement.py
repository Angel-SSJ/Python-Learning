# CONTROL STATEMENTS
condition = False
if condition is True:
    print("""The condition
  was true""")
else:
    print('''The condition
  was False''')

## OPERATOR TERNARY ##

#Ternary Operator
print('\n')
print('Ternary Operator')


def is_adult(age):
  if age > 18:
    return True
  else:
    return False


def is_adult2(age):
  return True if age > 18 else False

user_age = int(input())

webpage = 'about_whiskey.html' if user_age >= 21 else 'sorry.html'

if user_age >= 21:
    webpage = 'about_whiskey.html'
else:
    webpage = 'sorry.html'

