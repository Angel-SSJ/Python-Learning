# BUILT-IN FUNCTION EVAL()

"""
    The eval() method parses the expression passed to this method and runs python expression (code) within the program.
SYNTAX
    eval(expression, globals=None, locals=None)
PARAMETERS
    expression - the string parsed and evaluated as a Python expression
    globals (optional) - a dictionary
    locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
RETURN VAlUES
the result evaluated from the expression
"""
import math

# EXAMPLE 1: How eval() works in Python
x=1
print(eval('x+1'))

# EXAMPLE 2: Practical Example to Demonstrate Use of eval()
def calculatePerimeter(l):
    return 4*l

def calculateAre(l):
    return l*l

expression=input('Type a function: ')

for l in range(1,5):
    if (expression=='calculatePerimeter(l)'):
        print(f'If length is {l}, Perimeter= {eval(expression)}')
    elif (expression=='calculateAre(l)'):
        print(f'If length is {l}, Area= {eval(expression)}')
    else:
        print('Sos un pelotudo')
        break
"""
WARNINGS WHEN USING EVAL()
    Consider a situation where you are using a Unix system (macOS, Linux etc) and you have imported the os module. 
    The os module provides a portable way to use operating system functionalities like reading or writing to a file.

    If you allow users to input a value using eval(input()), the user may issue commands to change file or even delete
    all the files using the command: os.system('rm -rf *').
        from math import *
        print(eval('dir()'))
"""

# Restricting the Use of Available Methods and Variables in eval()
"""The expression is executed in the current scope. You can check the available variables and methods using following code:"""
print(eval('dir()'))

#-When both globals and locals parameters omitted
"""The globals and locals parameters (dictionaries) are used for global and local variables respectively. If the locals
 dictionary is omitted, it defaults to globals dictionary. Meaning, globals will be used for both global and local variables"""

#Example 3: Passing empty dictionary as globals parameter
from math import *
sqrt=math.sqrt

print(eval('dir()', {}))
#print(eval('sqrt(25)', {}))

#Example 4: Making Certain Methods available
print(eval('dir()',{'sqrt':sqrt,'pow':pow}))


names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

# Using square_root in Expression
print(eval('square_root(9)', names))

#Example 5: Restricting the Use of built-ins
eval(expression, {'__builtins__': None})

#-Passing globals parameters; locals parameters is omitted
"""
You can make needed functions and variables available for use by passing the locals dictionary. For example
"""

a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))




"""
Note: Sometimes, eval() is not secure even with limited names. When an object and its methods are made accessible,
almost anything can be done. The only secure way is by validating the user input.
"""