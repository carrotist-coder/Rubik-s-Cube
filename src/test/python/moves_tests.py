import unittest
from src.main.python.domain import rubik

class Test(unittest.TestCase):
    def setUp(self):
        self.r = rubik.Cube()

    def test_move_r(self):
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

    def test_move_r_x(self):
        self.r.cube = [['w','w','w','w','w','w','w','w','w'],
                       ['g','g','g','g','g','g','g','g','g'],
                       ['o','o','o','o','o','o','o','o','o'],
                       ['b','b','b','b','b','b','b','b','b'],
                       ['r','r','r','r','r','r','r','r','r'],
                       ['y','y','y','y','y','y','y','y','y']]

        self.r.solve()
        self.assertEqual(self.r.cube, [
                       ['g','w','w','g','w','w','g','w','w'],
                       ['y','g','g','y','g','g','y','g','g'],
                       ['o','o','o','o','o','o','o','o','o'],
                       ['b','b','w','b','b','w','b','b','w'],
                       ['r','r','r','r','r','r','r','r','r'],
                       ['b','y','y','b','y','y','b','y','y']])

    def test_move_r2(self):
        self.r.cube = [['b','o','g','y','w','b','w','g','r'],
                       ['o','w','w','b','g','y','o','w','w'],
                       ['r','g','b','g','o','r','r','w','y'],
                       ['r','b','w','r','b','o','o','r','y'],
                       ['g','y','y','o','r','g','g','w','b'],
                       ['g','b','o','r','y','o','b','y','y']]

        self.r.solve()
        self.assertEqual(self.r.cube,
            [['g', 'o', 'g', 'r', 'w', 'b', 'b', 'g', 'r'],
             ['y', 'w', 'w', 'o', 'g', 'y', 'w', 'w', 'w'],
             ['y', 'w', 'r', 'r', 'o', 'g', 'b', 'g', 'r'],
             ['r', 'b', 'o', 'r', 'b', 'b', 'o', 'r', 'o'],
             ['g', 'y', 'y', 'o', 'r', 'g', 'g', 'w', 'b'],
             ['b', 'b', 'o', 'y', 'y', 'o', 'w', 'y', 'y']])

    def test_move_l(self):
        self.r.solve()
        self.assertEqual(self.r.cube,
            [['w', 'w', 'g', 'w', 'w', 'g', 'w', 'w', 'g'],
             ['g', 'g', 'y', 'g', 'g', 'y', 'g', 'g', 'y'],
             ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
             ['w', 'b', 'b', 'w', 'b', 'b', 'w', 'b', 'b'],
             ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
             ['y', 'y', 'b', 'y', 'y', 'b', 'y', 'y', 'b']])


if __name__ == '__main__':
    unittest.main()
