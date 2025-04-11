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


#https://www.datacamp.com/tutorial/exception-handling-python?utm_source=google&utm_medium=paid_search&utm_campaignid=21057859163&utm_adgroupid=157296744657&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=692112538450&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1012108&utm_content=dsa~tofu~tutorial~python&accountid=9624585688&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-latam-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&gad_source=1&gclid=CjwKCAjwzMi_BhACEiwAX4YZUPrV6dUvGWMCPPIZQpl041VWeVwjBa-d6lwRbQJxIr6xj5I4hRuAHhoClZoQAvD_BwE