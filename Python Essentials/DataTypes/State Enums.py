# ENUMS
from enum import Enum
from re import error


class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
# Some people use enums to create a  constant and then nobody can reassing the value of the constant
print(list(State))