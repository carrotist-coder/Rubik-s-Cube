import unittest
from src.main.python.domain import rubik

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.r = rubik.Cube()

    def test_cross1(self):  # R2 F2 U L D2 B' R' D'
            self.r.cube = [
            ['o','o','o','b','w','o','r','y','y'],
            ['w','r','o','y','g','w','g','o','r'],
            ['w','o','b','w','o','g','g','b','y'],
            ['b','y','g','b','b','g','o','r','r'],
            ['b','w','w','b','r','r','b','g','y'],
            ['r','g','y','y','y','r','w','w','g']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross2(self):  # B2 D B2 R' D' L' D' R' F
            self.r.cube = [
            ['g','y','g','g','w','y','g','o','w'],
            ['y','y','g','b','g','g','o','b','b'],
            ['o','o','o','o','o','y','w','r','w'],
            ['r','r','w','w','b','w','y','o','r'],
            ['r','g','y','w','r','b','y','r','o'],
            ['b','r','r','g','y','w','b','b','b']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross3(self):  # D
            self.r.cube = [
            ['w','w','w','w','w','w','w','w','w'],
            ['g','g','g','g','g','g','o','o','o'],
            ['o','o','o','o','o','o','b','b','b'],
            ['b','b','b','b','b','b','r','r','r'],
            ['r','r','r','r','r','r','g','g','g'],
            ['y','y','y','y','y','y','y','y','y']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross4(self):  # L2 D2 F L2 B2 R2 F U2 B' L2 F2 U' B L2 F2 L D' F' U' R2 U2
            self.r.cube = [
            ['o','b','r','r','w','o','r','y','o'],
            ['y','b','y','g','g','g','w','w','w'],
            ['w','g','g','b','o','y','y','o','b'],
            ['b','o','g','r','b','r','b','w','o'],
            ['g','g','y','w','r','w','r','r','w'],
            ['o','o','g','y','y','y','b','b','r']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross5(self):  # D' F L' F2 D' L U D2 F L' U2 R' L' B2 L D2 R U2 D2 L
            self.r.cube = [
            ['b','w','b','o','w','r','w','y','r'],
            ['r','b','g','o','g','r','g','y','o'],
            ['o','g','g','b','o','b','o','o','w'],
            ['r','o','y','b','b','w','y','g','y'],
            ['y','y','w','g','r','r','b','w','b'],
            ['o','g','w','y','y','r','g','w','r']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross6(self):  # L2 R2 U F2 U' F2 D2 F2 U' R2 D2 F L' B' L2 F2 D F' U' B R
            self.r.cube = [
            ['y','y','o','b','w','w','r','g','y'],
            ['g','o','o','g','g','r','r','o','r'],
            ['o','w','w','w','o','r','w','b','b'],
            ['b','g','g','y','b','o','r','y','o'],
            ['b','g','w','b','r','r','b','w','g'],
            ['w','y','y','o','y','r','g','b','y']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])

    def test_cross7(self):  # F2 R2 U2 L2 D' F2 L2 D L2 R2 D L' R U B U L2 U' R2 F L
            self.r.cube = [
            ['y','b','r','y','w','b','o','b','w'],
            ['w','r','r','w','g','r','b','o','y'],
            ['b','b','g','o','o','r','g','w','o'],
            ['y','w','o','y','b','g','b','y','r'],
            ['b','o','g','g','r','o','o','g','r'],
            ['w','w','g','g','y','y','w','r','y']]

            self.r.solve()
            self.assertEqual([self.r.cube[self.r.white][1],self.r.cube[self.r.white][3],self.r.cube[self.r.white][5],
                              self.r.cube[self.r.white][7],
                              self.r.cube[self.r.green][self.r.edge_d],self.r.cube[self.r.orange][self.r.edge_d],
                              self.r.cube[self.r.blue][self.r.edge_d],self.r.cube[self.r.red][self.r.edge_d]],
                             ['w','w','w','w','g','o','b','r'])


if __name__ == '__main__':
    unittest.main()
