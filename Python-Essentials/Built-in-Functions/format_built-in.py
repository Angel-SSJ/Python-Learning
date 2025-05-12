# BUILT-IN FUNCTION FORMAT()
"""
The format() method returns a formatted value based on the specified formatter.

SYNTAX
    format(value, format_spec)
PARAMETERS
    value - the data we want to format
    format_spec - the specification on how we want to format the data
RETURN VAlUES
    The format() function returns a value in the string representation of the desired format.


"""

# EXAMPLE 1: Numeric Formatting Using format()
# decimal formatting
decimal_value = format(123, 'd')

print("Decimal Formatting:", decimal_value)

# binary formatting
binary_value = format(123, 'b')

print("Binary Formatting:", binary_value)
# EXAMPLE 2: Number Formatting With Sign

# using '+' and '-' format specifier
positive_with_plus = format(123, '+')
positive_with_minus = format(-123, '+')

print("Positive with '+':", positive_with_plus)
print("Positive with '-':", positive_with_minus)
"""
The sign option in formatting controls the display of the sign for the numbers. Here, + indicates that both positive and negative numbers will show their signs.
Note: The sign option - indicates only negative numbers will show their sign and ' ' will show a space for positive numbers and a minus for negative numbers.
"""

#EXAMPLE 3: Number Formatting With Precision
# set precision to 2 for floating-point number
precision_value = format(123.4567, '.2f')

print(precision_value)
print('hola {0}'.format('adam'))