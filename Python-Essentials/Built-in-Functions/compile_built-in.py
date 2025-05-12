#BUILT-IN FUNCTION COMPILE()
import os
"""
The compile() method computes the Python code from a source object and returns it.
"""

codeInString = 'a= 8\nb=7\nsum=a+b\nprint("sum =",sum)'
codeObject=compile(codeInString, 'sumstring', 'exec')
exec(codeObject)


"""
SYNTAX
    compile(source, filename, mode)
PARAMETERS
    source - a normal string , a byte string, or an AST object
    filename - file from which the code is to be read
    mode - exec (can take a code block with statements, class and functions ), eval (accepts single expression) or single (has a single interactive statement)
RETURN VALUES
    a python object code

"""

print('--------------\n')
#Example 1
codeInString=f'if os.path.exists("testing_built-in_funcionts "):\n{"":<3}print("The path exist ")\nelse:\n{"":<3}print( "The path does not exist, but I will create it")\n{"":<3}os.mkdir("testing_built-in_funcionts")'
codeObject=compile(codeInString, 'compile_built-in.py', 'exec')
exec(codeObject)

#Example 2

codeInString=f'''
file="testing_built-in_funcionts.txt"
if os.path.exists(file):
    print(f"the file exists" )
else:
    print(f"the file does not exist, but I will create it")
    with open(file, "w") as f:
        f.write("Este archivo ha sido creado con built-in functions")
'''
testing= compile(codeInString, 'compile_built-in.py', 'exec')
exec(testing)

