from PythonEssentials.UnitTesting.cuboVolume import *

import unittest

class TestCuboId(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1), 1)
        self.assertAlmostEqual(cuboid_volume(0), 0)

    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)
