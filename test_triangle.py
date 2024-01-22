import unittest
import triangle

# Constants for triangle types
'''INVALID = -1
SCALENE = 0
ISOSCELES = 1
EQUILATERAL = 2 '''

# Unit test class
class TestTriangleIdentifier(unittest.TestCase):

    def test_invalid_triangle(self):
        self.assertEqual(-1, triangle.triangle_identifier(1, 1, 3))
        self.assertEqual(-1, triangle.triangle_identifier(1, 3, 1))
        self.assertEqual(-1, triangle.triangle_identifier(3, 1, 1))

    def test_equilateral_triangle(self):
        self.assertEqual(2, triangle.triangle_identifier(3, 3, 3))

    def test_isosceles_triangle(self):
        self.assertEqual(1, triangle.triangle_identifier(2, 2, 3))
        self.assertEqual(1, triangle.triangle_identifier(2, 3, 2))
        self.assertEqual(1, triangle.triangle_identifier(3, 2, 2))

    def test_scalene_triangle(self):
        self.assertEqual(0, triangle.triangle_identifier(2, 3, 4))

    def test_edge_cases(self):
        self.assertEqual(-1, triangle.triangle_identifier(1, 1, 2))
        self.assertEqual(-1, triangle.triangle_identifier(2, 5, 3))

    def test_zero_and_negative_sides(self):
        self.assertEqual(-1, triangle.triangle_identifier(0, 0, 0))
        self.assertEqual(-1, triangle.triangle_identifier(-1, 2, 3))
        self.assertEqual(-1, triangle.triangle_identifier(2, -1, 3))
        self.assertEqual(-1, triangle.triangle_identifier(2, 3, -1))

    def test_large_value_sides(self):
        self.assertEqual(2, triangle.triangle_identifier(1e10, 1e10, 1e10))
        self.assertEqual(-1, triangle.triangle_identifier(1e10, 2e10, 3e10))

    def test_floating_point_sides(self):
        self.assertEqual(2, triangle.triangle_identifier(0.5, 0.5, 0.5))
        self.assertEqual(1, triangle.triangle_identifier(2.5, 2.5, 4.0))
        self.assertEqual(0, triangle.triangle_identifier(3.1, 4.2, 5.3))





if __name__ == '__main__':
    unittest.main()
