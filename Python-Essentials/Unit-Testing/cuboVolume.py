import unittest

def cuboid_volume(l):
    if type(l) not in [int,float]:
        raise TypeError("l must be an integer or float")
    return (l*l*l)
#length = [2,1,1,-2.5,2j,'two']
#for i in range(len(length)):
#    print(f'The volume of cuboid: {cuboid_volume(length[i])}')


