#BUILT-IN FUNCTION BYTES()

"""
returns an immutable bytes object initialized with the given size and data

"""
message='Python is fun'
print(bytes(message,encoding='utf-8'))

"""
SYNTAX
    bytes([source[, encoding[, errors]]])
    bytes() method returns a bytes object which is an immutable (cannot be modified) sequence of integers in the range 0 <=x < 256.
PARAMETERS
    source (Optional) - source to initialize the array of bytes.
    encoding (Optional) - if the source is a string, the encoding of the string.
    errors (Optional) - if the source is a string, the action to take when the encoding conversion fails (Read more: String encoding)

    Type                   	Description
    String                  	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
    Integer                 	Creates an array of provided size, all initialized to null
    Object                  	A read-only buffer of the object will be used to initialize the byte array
    Iterable	                Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
    No source (arguments)   	Creates an array of size 0
    
RETURN VALUE    
    The bytes() method returns a bytes object of the given size and initialization values.


"""

print('------------------------------\n')
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
print('------------------------------\n')
size = 5

arr = bytes(size)
print(arr)
print('------------------------------\n')
rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)
print('------------------------------\n')

print('------------------------------\n')