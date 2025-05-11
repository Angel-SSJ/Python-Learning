# BUILT-IN FUNCTION BYTEARRAY()


"""
returns a bytearray object which is an array of the given bytes
"""

prime_numbers = [2, 3, 5, 7]
print(bytearray(prime_numbers))


"""
SINTAX
    bytearray([source[, encoding[,errors]]])
    
method returns a bytearray object (i.e. array of bytes) which is mutable (can be modified) sequence of integers in the range 0 <= x < 256.
If you want the immutable version, use the bytes() method.
PARAMETERS
    source (Optional) - source to initialize the array of bytes.
    encoding (Optional) - if the source is a string, the encoding of the string.
    errors (Optional) - if the source is a string, the action to take when the encoding conversion fails (Read more: String encoding)
    
    Type                   	Description
    String            	        Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
    Integer             	    Creates an array of provided size, all initialized to null
    Object                    	A read-only buffer of the object will be used to initialize the byte array
    Iterable                	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
    No source (arguments)	    Creates an array of size 0.
RETURN VALUE
    The bytearray() method returns an array of bytes of the given size and initialization values.

"""

print('------------------------------\n')
string = "Python is interesting."
print(bytearray(string,encoding='utf-8'))
print('------------------------------\n')
size=5
print(bytearray(size))
print('------------------------------\n')
rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)

