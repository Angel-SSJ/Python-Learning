# BUILT-IN FUNCTION EXEC()
"""
    The exec() method executes a dynamically created program, which is either a string or a code object.
SYNTAX
    exec(object, globals, locals)
PARAMETERS
    object - Either a string or a code object
    globals (optional) - a dictionary
    locals (optional) - a mapping object (commonly dictionary)
RETURN VAlUES
    The exec() method doesn't return any value.
"""

# EXAMPLE 1: Python exec()
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
# EXAMPLE 2: exec() With a Single Line Program Input
    # get an entire program as input
#program = input('Enter a program:') # [print(item) for item in [1, 2, 3]]
    # execute the program
exec(program)
#Example 3: exec() with a Multi-line Input Program
    #We can pass a multi-line input program to the exec() method with the help of \n. But we need to use the compile() method to compile the program first.
    # get a multi-line program as input
#program = input('Enter a program:')

    # compile the program in execution mode
b = compile(program, 'something', 'exec')

    # execute the program
exec(b)

#Example 4 : Checking Usable code with exec()
# If I want to check the methods and variables I can use with the exec() method. I can do this with the help of the dir() method.
# import all the methods from math library
from math import *

# check the usable methods
exec('print(dir())')

#Example 5 : Blocking unnecessary methods and variable in exec()
#We can block these unnecessary methods and variables by passing the optional globals and locals parameter to the exec() method.
mycode='''a=cbrt(9)
print(a)'''

exec(mycode,{'cbrt':cbrt})
exec(mycode,{})

#Example 6: Using necessary methods and variables in exec()
from math import *

    # set globals parameter to none
globalsParameter = {'__builtins__' : None}

    # set locals parameter to take only print() and dir()
localsParameter = {'print': print, 'dir': dir}

    # print the accessible method directory
exec('print(dir())', globalsParameter, localsParameter)