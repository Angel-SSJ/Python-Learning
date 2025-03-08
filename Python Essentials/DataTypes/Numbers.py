#complex numbers
num1 = 2 + 3j
num2 = complex(2, 3)
# the complex function is used to create a complex number, the first argument is the real part and the second argument is the imaginary part

print(num1.real, num2.imag)


# INTEGER #
age = 2
print(f' is age value integer? {isinstance(age, int)}')
print(f' is age value float? {isinstance(age, float)}')
#float
height = 2.4
print(f' is height value integer? {isinstance(height, int)}')
print(f' is height value float? {isinstance(height, float)}')
# I can create  a variable of a specific type by using the class constructor passing a value literal or a variable name like for instance

height2 = float(2)
print(isinstance(height2, int))

# I can convert a type to another
age = '2'
ageInt = int(age)  # search to convert int to string

print(isinstance(ageInt, int))
