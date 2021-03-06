import math
import unittest
from hopfield.input import *

class TestInput(unittest.TestCase):

    def test_three_points(self):
        matrix = distance_matrix([(0, 0), (0, 2), (4, 0)])
        self.assertAlmostEqual(matrix[0][0], 0.0)
        self.assertAlmostEqual(matrix[0][1], 2.0)
        self.assertAlmostEqual(matrix[0][2], 4.0)

        self.assertAlmostEqual(matrix[1][0], 2.0)
        self.assertAlmostEqual(matrix[1][1], 0.0)
        self.assertAlmostEqual(matrix[1][2], 2 * math.sqrt(5), 2)

        self.assertAlmostEqual(matrix[2][0], 4.0)
        self.assertAlmostEqual(matrix[2][1], 2 * math.sqrt(5), 2)
        self.assertAlmostEqual(matrix[2][2], 0.0)

    def test_four_points(self):
        matrix = distance_matrix([(1, 3), (2, 1), (4, 4), (6, 2)])

        self.assertAlmostEqual(matrix[0][0], 0.0)
        self.assertAlmostEqual(matrix[0][1], 2.23, 1)
        self.assertAlmostEqual(matrix[0][2], 3.16, 1)
        self.assertAlmostEqual(matrix[0][3], 5.09, 1)

        self.assertAlmostEqual(matrix[1][0], 2.23, 1)
        self.assertAlmostEqual(matrix[1][1], 0.0, 1)
        self.assertAlmostEqual(matrix[1][2], 3.60, 1)
        self.assertAlmostEqual(matrix[1][3], 4.12, 1)

        self.assertAlmostEqual(matrix[2][0], 3.16, 1)
        self.assertAlmostEqual(matrix[2][1], 3.60, 1)
        self.assertAlmostEqual(matrix[2][2], 0.0, 1)
        self.assertAlmostEqual(matrix[2][3], 2.82, 1)

        self.assertAlmostEqual(matrix[3][0], 5.09, 1)
        self.assertAlmostEqual(matrix[3][1], 4.12, 1)
        self.assertAlmostEqual(matrix[3][2], 2.82, 1)
        self.assertAlmostEqual(matrix[3][3], 0.0, 1)

    def test_normalisation(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 10],
        ]
        matrix = normalize(matrix)
        self.assertAlmostEqual(matrix[0][0], 0.1)
        self.assertAlmostEqual(matrix[0][1], 0.2)
        self.assertAlmostEqual(matrix[0][2], 0.3)

        self.assertAlmostEqual(matrix[1][0], 0.4)
        self.assertAlmostEqual(matrix[1][1], 0.5)
        self.assertAlmostEqual(matrix[1][2], 0.6)

        self.assertAlmostEqual(matrix[2][0], 0.7)
        self.assertAlmostEqual(matrix[2][1], 0.8)
        self.assertAlmostEqual(matrix[2][2], 1.0)


if __name__ == '__main__':
    unittest.main()
