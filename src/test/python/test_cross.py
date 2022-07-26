import unittest
from src.main.python.domain import rubik

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.r = rubik.Cube()

    def test_cross(self):
            self.r.cube = [
            ['o','o','o','b','w','o','r','y','y'],
            ['w','r','o','y','g','w','g','o','r'],
            ['w','o','b','w','o','g','g','b','y'],
            ['b','y','g','b','b','g','o','r','r'],
            ['b','w','w','b','r','r','b','g','y'],
            ['r','g','y','y','y','r','w','w','g']]

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
