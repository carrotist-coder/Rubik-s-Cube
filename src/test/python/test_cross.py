import unittest
from src.main.python.domain import rubik

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.r = rubik.Cube()

    def test_cross(self):
            self.r.cube = [
                ['y', 'w', 'y', 'y', 'w', 'y', 'y', 'w', 'y'],
                ['g', 'b', 'g', 'b', 'g', 'b', 'g', 'b', 'g'],
                ['r', 'r', 'r', 'o', 'o', 'o', 'r', 'r', 'r'],
                ['b', 'g', 'b', 'g', 'b', 'g', 'b', 'g', 'b'],
                ['o', 'o', 'o', 'r', 'r', 'r', 'o', 'o', 'o'],
                ['w', 'y', 'w', 'w', 'y', 'w', 'w', 'y', 'w']
            ]

            self.r.solve()
            self.assertEqual(self.r.cube, [
                ['b', 'w', 'y', 'g', 'w', 'y', 'b', 'w', 'y'],
                ['y', 'b', 'g', 'y', 'g', 'b', 'y', 'b', 'g'],
                ['r', 'o', 'r', 'r', 'o', 'r', 'r', 'o', 'r'],
                ['b', 'g', 'w', 'g', 'b', 'w', 'b', 'g', 'w'],
                ['o', 'o', 'o', 'r', 'r', 'r', 'o', 'o', 'o'],
                ['g', 'y', 'w', 'b', 'y', 'w', 'g', 'y', 'w']
            ])


if __name__ == '__main__':
    unittest.main()
