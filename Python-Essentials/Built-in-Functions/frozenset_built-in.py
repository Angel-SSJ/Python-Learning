# BUILT-IN FUNCTION  FROZENSET()
"""
    Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time,
    elements of the frozen set remain the same after creation.
    Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is
    not ordered (the elements can be set at any index).
SYNTAX
    frozenset([iterable])
PARAMETERS
    iterable (Optional) - the iterable which contains elements to initialize the frozenset with.
RETURN VAlUES
    The frozenset() function returns an immutable frozenset initialized with elements from the given iterable.
    If no parameters are passed, it returns an empty frozenset.
"""

# EXAMPLE 1: Working of Python frozenset()
numbers =[1,2,3,4,5,6,7,8,9,10]
fSet = frozenset(numbers)
print('The frozen set is:', fSet)
print('The empty frozen set is:',frozenset())
# EXAMPLE 2: frozenset() for Dictionary
"""
When you use a dictionary as an iterable for a frozen set, it only takes keys of the dictionary to create the set.
"""
person={'name':'Angel','Age':24,'sex':'male','hobbie':'play soccer'}
fSet = frozenset(person)
print(fSet)


#FROZENSET OPERATIONS
# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C= A.copy()
print(C)

    # union
print(A.union(B))

    # intersection
print(A.intersection(B))

    # difference
print(A.difference(B))

    #symmetric_difference
print(A.symmetric_difference(B))

    #Similarly, other set methods like isdisjoint(), issubset(), and issuperset() are also available.


