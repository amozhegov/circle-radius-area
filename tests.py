import main
import unittest
import math

class TestArea(unittest.TestCase):
    def test_circle_negative_radius(self):
        radius = -1 
        with self.assertRaises(ValueError):
            main.AreaCalc.figure(radius)

    def test_circle_positive_radius(self):
        radius = 2
        expected = math.pi * radius ** 2
        result = main.AreaCalc.figure(radius)
        self.assertAlmostEqual(result, expected, places=10)
        #self.assertAlmostEqual(float(result.split()[-1]), expected, places=10)

    def test_circle_zero_radius(self):
        with self.assertRaises(ValueError):
            main.AreaCalc.figure(0)

    def test_triangle_negative_side(self):
        side_a, side_b, side_c = 1, 2, -3
        with self.assertRaises(ValueError):
            main.AreaCalc.figure(side_a, side_b, side_c)

    def test_triangle_positive_side(self):
        sides = [6, 8, 10]
        expected = 24.0
        result = main.AreaCalc.figure(*sides)
        self.assertAlmostEqual(result, expected, places=10)

    def test_triangle_is_orthogonal(self):
        sides = [3, 4, 5]  
        result = main.AreaCalc.is_triangle_orthogonal(*sides)        
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
