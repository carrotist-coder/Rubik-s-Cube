from src.main.python.domain import solve

class Cube:
    def __init__(self):
        self.solved = False
        self.cross_is = False
        self.f2l_is = False
        self.oll_is = False
        self.cube = [
            ['w','w','w','w','w','w','w','w','w'],
            ['g','g','g','g','g','g','g','g','g'],
            ['o','o','o','o','o','o','o','o','o'],
            ['b','b','b','b','b','b','b','b','b'],
            ['r','r','r','r','r','r','r','r','r'],
            ['y','y','y','y','y','y','y','y','y']]
        self.solution = ['z2']
        self.colors = ['w', 'g', 'o', 'b', 'r', 'y']
        self.msgs = ['White Side', 'Green Side', 'Orange Side', 'Blue Side', 'Red Side', 'Yellow Side']

        self.white = 0
        self.green = 1
        self.orange = 2
        self.blue = 3
        self.red = 4
        self.yellow = 5
        # positions in self.cube

        self.centre = 4
        self.edge_u = 7
        self.edge_l = 5
        self.edge_r = 3
        self.edge_d = 1
        self.corner_ul = 8
        self.corner_ur = 6
        self.corner_dl = 2
        self.corner_dr = 0
        # positions of centre, edges, corners
        # cube is being solved in accordance with yellow-up, green-front
        self.edge_blue_u = 1
        self.edge_blue_l = 3
        self.edge_blue_r = 5
        self.edge_blue_d = 7
        self.corner_blue_ul = 0
        self.corner_blue_ur = 2
        self.corner_blue_dl = 6
        self.corner_blue_dr = 8
        # blue side is vice versa

    def r(self):
        pocket = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r], self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_ur]=self.cube[self.green][self.corner_ur]
        self.cube[self.yellow][self.edge_r] = self.cube[self.green][self.edge_r]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.green][self.corner_dr]

        self.cube[self.green][self.corner_ur] = self.cube[self.white][self.corner_ur]
        self.cube[self.green][self.edge_r] = self.cube[self.white][self.edge_r]
        self.cube[self.green][self.corner_dr] = self.cube[self.white][self.corner_dr]

        self.cube[self.white][self.corner_ur] = self.cube[self.blue][self.corner_blue_ur]
        self.cube[self.white][self.edge_r] = self.cube[self.blue][self.edge_blue_r]
        self.cube[self.white][self.corner_dr] = self.cube[self.blue][self.corner_blue_dr]

        self.cube[self.blue][self.corner_blue_ur] = pocket[0]
        self.cube[self.blue][self.edge_blue_r] = pocket[1]
        self.cube[self.blue][self.corner_blue_dr] = pocket[2]

        pocket = self.cube[self.orange][self.edge_u]
        self.cube[self.orange][self.edge_u] = self.cube[self.orange][self.edge_l]
        self.cube[self.orange][self.edge_l] = self.cube[self.orange][self.edge_d]
        self.cube[self.orange][self.edge_d] = self.cube[self.orange][self.edge_r]
        self.cube[self.orange][self.edge_r] = pocket

        pocket = self.cube[self.orange][self.corner_ul]
        self.cube[self.orange][self.corner_ul] = self.cube[self.orange][self.corner_dl]
        self.cube[self.orange][self.corner_dl] = self.cube[self.orange][self.corner_dr]
        self.cube[self.orange][self.corner_dr] = self.cube[self.orange][self.corner_ur]
        self.cube[self.orange][self.corner_ur] = pocket

        self.solution.append("R")



    def r_x(self):
        write(self.cube)
        pocket = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r], self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_ur]=self.cube[self.blue][self.corner_blue_ur]
        self.cube[self.yellow][self.edge_r] = self.cube[self.blue][self.edge_blue_r]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.blue][self.corner_blue_dr]

        self.cube[self.blue][self.corner_blue_ur] = self.cube[self.white][self.corner_ur]
        self.cube[self.blue][self.edge_blue_r] = self.cube[self.white][self.edge_r]
        self.cube[self.blue][self.corner_blue_dr] = self.cube[self.white][self.corner_dr]

        self.cube[self.white][self.corner_ur] = self.cube[self.green][self.corner_ur]
        self.cube[self.white][self.edge_r] = self.cube[self.green][self.edge_r]
        self.cube[self.white][self.corner_dr] = self.cube[self.green][self.corner_dr]

        self.cube[self.green][self.corner_ur] = pocket[0]
        self.cube[self.green][self.edge_r] = pocket[1]
        self.cube[self.green][self.corner_dr] = pocket[2]

        pocket = self.cube[self.orange][self.edge_u]
        self.cube[self.orange][self.edge_u] = self.cube[self.orange][self.edge_r]
        self.cube[self.orange][self.edge_r] = self.cube[self.orange][self.edge_d]
        self.cube[self.orange][self.edge_d] = self.cube[self.orange][self.edge_l]
        self.cube[self.orange][self.edge_l] = pocket

        pocket = self.cube[self.orange][self.corner_ul]
        self.cube[self.orange][self.corner_ul] = self.cube[self.orange][self.corner_ur]
        self.cube[self.orange][self.corner_ur] = self.cube[self.orange][self.corner_dr]
        self.cube[self.orange][self.corner_dr] = self.cube[self.orange][self.corner_dl]
        self.cube[self.orange][self.corner_dl] = pocket

        self.solution.append("R'")

    def r2(self):
        pocket1 = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r],
                  self.cube[self.yellow][self.corner_dr]]
        pocket2 = [self.cube[self.white][self.corner_ur], self.cube[self.white][self.edge_r],
                  self.cube[self.white][self.corner_dr]]
        self.cube[self.yellow][self.corner_ur] = pocket2[0]
        self.cube[self.yellow][self.edge_r] = pocket2[1]
        self.cube[self.yellow][self.corner_dr] = pocket2[2]
        self.cube[self.white][self.corner_ur] = pocket1[0]
        self.cube[self.white][self.edge_r] = pocket1[1]
        self.cube[self.white][self.corner_dr] = pocket1[2]

        pocket1 = [self.cube[self.green][self.corner_ur], self.cube[self.green][self.edge_r],
                   self.cube[self.green][self.corner_dr]]
        pocket2 = [self.cube[self.blue][self.corner_blue_ur], self.cube[self.blue][self.edge_blue_r],
                   self.cube[self.blue][self.corner_blue_dr]]
        self.cube[self.green][self.corner_ur] = pocket2[0]
        self.cube[self.green][self.edge_r] = pocket2[1]
        self.cube[self.green][self.corner_dr] = pocket2[2]
        self.cube[self.blue][self.corner_blue_ur] = pocket1[0]
        self.cube[self.blue][self.edge_blue_r] = pocket1[1]
        self.cube[self.blue][self.corner_blue_dr] = pocket1[2]

        pocket1 = self.cube[self.orange][self.edge_u]
        pocket2 = self.cube[self.orange][self.edge_d]
        self.cube[self.orange][self.edge_d] = pocket1
        self.cube[self.orange][self.edge_u] = pocket2

        pocket1 = self.cube[self.orange][self.edge_l]
        pocket2 = self.cube[self.orange][self.edge_r]
        self.cube[self.orange][self.edge_r] = pocket1
        self.cube[self.orange][self.edge_l] = pocket2

        pocket1 = self.cube[self.orange][self.corner_ul]
        pocket2 = self.cube[self.orange][self.corner_dr]
        self.cube[self.orange][self.corner_dr] = pocket1
        self.cube[self.orange][self.corner_ul] = pocket2

        pocket1 = self.cube[self.orange][self.corner_ur]
        pocket2 = self.cube[self.orange][self.corner_dl]
        self.cube[self.orange][self.corner_dl] = pocket1
        self.cube[self.orange][self.corner_ur] = pocket2

        self.solution.append("R2")



    def l(self):
        pocket = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_l], self.cube[self.yellow][self.corner_dl]]

        self.cube[self.yellow][self.corner_ul]=self.cube[self.blue][self.corner_blue_ul]
        self.cube[self.yellow][self.edge_l] = self.cube[self.blue][self.edge_blue_l]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.blue][self.corner_blue_dl]

        self.cube[self.blue][self.corner_blue_dl] = self.cube[self.white][self.corner_dl]
        self.cube[self.blue][self.edge_blue_l] = self.cube[self.white][self.edge_l]
        self.cube[self.blue][self.corner_blue_ul] = self.cube[self.white][self.corner_ul]

        self.cube[self.white][self.corner_dl] = self.cube[self.green][self.corner_dl]
        self.cube[self.white][self.edge_l] = self.cube[self.green][self.edge_l]
        self.cube[self.white][self.corner_ul] = self.cube[self.green][self.corner_ul]

        self.cube[self.green][self.corner_dl] = pocket[2]
        self.cube[self.green][self.edge_l] = pocket[1]
        self.cube[self.green][self.corner_ul] = pocket[0]

        pocket = self.cube[self.red][self.edge_u]
        self.cube[self.red][self.edge_u] = self.cube[self.red][self.edge_l]
        self.cube[self.red][self.edge_l] = self.cube[self.red][self.edge_d]
        self.cube[self.red][self.edge_d] = self.cube[self.red][self.edge_r]
        self.cube[self.red][self.edge_r] = pocket

        pocket = self.cube[self.red][self.corner_ul]
        self.cube[self.red][self.corner_ul] = self.cube[self.red][self.corner_dl]
        self.cube[self.red][self.corner_dl] = self.cube[self.red][self.corner_dr]
        self.cube[self.red][self.corner_dr] = self.cube[self.red][self.corner_ur]
        self.cube[self.red][self.corner_ur] = pocket

        self.solution.append("L")

    def l_x(self):
        pocket = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_l], self.cube[self.yellow][self.corner_dl]]

        self.cube[self.yellow][self.corner_ul]=self.cube[self.green][self.corner_ul]
        self.cube[self.yellow][self.edge_l] = self.cube[self.green][self.edge_l]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.green][self.corner_dl]

        self.cube[self.green][self.corner_ul] = self.cube[self.white][self.corner_ul]
        self.cube[self.green][self.edge_l] = self.cube[self.white][self.edge_l]
        self.cube[self.green][self.corner_dl] = self.cube[self.white][self.corner_dl]

        self.cube[self.white][self.corner_ul] = self.cube[self.blue][self.corner_blue_ul]
        self.cube[self.white][self.edge_l] = self.cube[self.blue][self.edge_blue_l]
        self.cube[self.white][self.corner_dl] = self.cube[self.blue][self.corner_blue_dl]

        self.cube[self.blue][self.corner_blue_ul] = pocket[0]
        self.cube[self.blue][self.edge_blue_l] = pocket[1]
        self.cube[self.blue][self.corner_blue_dl] = pocket[2]

        pocket = self.cube[self.red][self.edge_u]
        self.cube[self.red][self.edge_u] = self.cube[self.red][self.edge_r]
        self.cube[self.red][self.edge_r] = self.cube[self.red][self.edge_d]
        self.cube[self.red][self.edge_d] = self.cube[self.red][self.edge_l]
        self.cube[self.red][self.edge_l] = pocket

        pocket = self.cube[self.red][self.corner_ul]
        self.cube[self.red][self.corner_ul] = self.cube[self.red][self.corner_ur]
        self.cube[self.red][self.corner_ur] = self.cube[self.red][self.corner_dr]
        self.cube[self.red][self.corner_dr] = self.cube[self.red][self.corner_dl]
        self.cube[self.red][self.corner_dl] = pocket

        self.solution.append("L'")

    def l2(self):
        pocket1 = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_l],
                  self.cube[self.yellow][self.corner_dl]]
        pocket2 = [self.cube[self.white][self.corner_ul], self.cube[self.white][self.edge_l],
                  self.cube[self.white][self.corner_dl]]
        self.cube[self.yellow][self.corner_ul] = pocket2[0]
        self.cube[self.yellow][self.edge_l] = pocket2[1]
        self.cube[self.yellow][self.corner_dl] = pocket2[2]
        self.cube[self.white][self.corner_ul] = pocket1[0]
        self.cube[self.white][self.edge_l] = pocket1[1]
        self.cube[self.white][self.corner_dl] = pocket1[2]

        pocket1 = [self.cube[self.green][self.corner_ul], self.cube[self.green][self.edge_l],
                   self.cube[self.green][self.corner_dl]]
        pocket2 = [self.cube[self.blue][self.corner_blue_ul], self.cube[self.blue][self.edge_blue_l],
                   self.cube[self.blue][self.corner_blue_dl]]
        self.cube[self.green][self.corner_ul] = pocket2[0]
        self.cube[self.green][self.edge_l] = pocket2[1]
        self.cube[self.green][self.corner_dl] = pocket2[2]
        self.cube[self.blue][self.corner_blue_ul] = pocket1[0]
        self.cube[self.blue][self.edge_blue_l] = pocket1[1]
        self.cube[self.blue][self.corner_blue_dl] = pocket1[2]

        pocket1 = self.cube[self.red][self.edge_u]
        pocket2 = self.cube[self.red][self.edge_d]
        self.cube[self.red][self.edge_d] = pocket1
        self.cube[self.red][self.edge_u] = pocket2

        pocket1 = self.cube[self.red][self.edge_l]
        pocket2 = self.cube[self.red][self.edge_r]
        self.cube[self.red][self.edge_r] = pocket1
        self.cube[self.red][self.edge_l] = pocket2

        pocket1 = self.cube[self.red][self.corner_ul]
        pocket2 = self.cube[self.red][self.corner_dr]
        self.cube[self.red][self.corner_dr] = pocket1
        self.cube[self.red][self.corner_ul] = pocket2

        pocket1 = self.cube[self.red][self.corner_ur]
        pocket2 = self.cube[self.red][self.corner_dl]
        self.cube[self.red][self.corner_dl] = pocket1
        self.cube[self.red][self.corner_ur] = pocket2

        self.solution.append("L2")

    def u(self):
        # in this case when we do U blue side doesn't care, it just turns around (as far as I understood)

        pocket = [self.cube[self.green][self.corner_ul], self.cube[self.green][self.edge_u],
                  self.cube[self.green][self.corner_ur]]

        self.cube[self.green][self.corner_ul] = self.cube[self.orange][self.corner_ul]
        self.cube[self.green][self.edge_u] = self.cube[self.orange][self.edge_u]
        self.cube[self.green][self.corner_ur] = self.cube[self.orange][self.corner_ur]

        self.cube[self.orange][self.corner_ul] = self.cube[self.blue][self.corner_ul]
        self.cube[self.orange][self.edge_u] = self.cube[self.blue][self.edge_u]
        self.cube[self.orange][self.corner_ur] = self.cube[self.blue][self.corner_ur]

        self.cube[self.blue][self.corner_ul] = self.cube[self.red][self.corner_ul]
        self.cube[self.blue][self.edge_u] = self.cube[self.red][self.edge_u]
        self.cube[self.blue][self.corner_ur] = self.cube[self.red][self.corner_ur]

        self.cube[self.red][self.corner_ul] = pocket[0]
        self.cube[self.red][self.edge_u] = pocket[1]
        self.cube[self.red][self.corner_ur] = pocket[2]

        pocket = self.cube[self.yellow][self.edge_u]
        self.cube[self.yellow][self.edge_u] = self.cube[self.yellow][self.edge_l]
        self.cube[self.yellow][self.edge_l] = self.cube[self.yellow][self.edge_d]
        self.cube[self.yellow][self.edge_d] = self.cube[self.yellow][self.edge_r]
        self.cube[self.yellow][self.edge_r] = pocket

        pocket = self.cube[self.yellow][self.corner_ul]
        self.cube[self.yellow][self.corner_ul] = self.cube[self.yellow][self.corner_dl]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.yellow][self.corner_dr]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.yellow][self.corner_ur]
        self.cube[self.yellow][self.corner_ur] = pocket

        self.solution.append("U")


    def u_x(self):
        pocket = [self.cube[self.green][self.corner_ul], self.cube[self.green][self.edge_u],
                  self.cube[self.green][self.corner_ur]]

        self.cube[self.green][self.corner_ul] = self.cube[self.red][self.corner_ul]
        self.cube[self.green][self.edge_u] = self.cube[self.red][self.edge_u]
        self.cube[self.green][self.corner_ur] = self.cube[self.red][self.corner_ur]

        self.cube[self.red][self.corner_ul] = self.cube[self.blue][self.corner_ul]
        self.cube[self.red][self.edge_u] = self.cube[self.blue][self.edge_u]
        self.cube[self.red][self.corner_ur] = self.cube[self.blue][self.corner_ur]
        # ?
        self.cube[self.blue][self.corner_ul] = self.cube[self.orange][self.corner_ul]
        self.cube[self.blue][self.edge_u] = self.cube[self.orange][self.edge_u]
        self.cube[self.blue][self.corner_ur] = self.cube[self.orange][self.corner_ur]

        self.cube[self.orange][self.corner_ul] = pocket[0]
        self.cube[self.orange][self.edge_u] = pocket[1]
        self.cube[self.orange][self.corner_ur] = pocket[2]

        pocket = self.cube[self.yellow][self.edge_u]
        self.cube[self.yellow][self.edge_u] = self.cube[self.yellow][self.edge_r]
        self.cube[self.yellow][self.edge_r] = self.cube[self.yellow][self.edge_d]
        self.cube[self.yellow][self.edge_d] = self.cube[self.yellow][self.edge_l]
        self.cube[self.yellow][self.edge_l] = pocket

        pocket = self.cube[self.yellow][self.corner_ul]
        self.cube[self.yellow][self.corner_ul] = self.cube[self.yellow][self.corner_ur]
        self.cube[self.yellow][self.corner_ur] = self.cube[self.yellow][self.corner_dr]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.yellow][self.corner_dl]
        self.cube[self.yellow][self.corner_dl] = pocket

        self.solution.append("U'")

    def u2(self):
        pocket1 = [self.cube[self.green][self.corner_ul], self.cube[self.green][self.edge_u],
                  self.cube[self.green][self.corner_ur]]
        pocket2 = [self.cube[self.blue][self.corner_ul], self.cube[self.blue][self.edge_u],
                  self.cube[self.blue][self.corner_ur]]
        self.cube[self.green][self.corner_ul] = pocket2[0]
        self.cube[self.green][self.edge_u] = pocket2[1]
        self.cube[self.green][self.corner_ur] = pocket2[2]
        self.cube[self.blue][self.corner_ul] = pocket1[0]
        self.cube[self.blue][self.edge_u] = pocket1[1]
        self.cube[self.blue][self.corner_ur] = pocket1[2]

        pocket1 = [self.cube[self.orange][self.corner_ul], self.cube[self.orange][self.edge_u],
                   self.cube[self.orange][self.corner_ur]]
        pocket2 = [self.cube[self.red][self.corner_ul], self.cube[self.red][self.edge_u],
                   self.cube[self.red][self.corner_ur]]
        self.cube[self.orange][self.corner_ul] = pocket2[0]
        self.cube[self.orange][self.edge_u] = pocket2[1]
        self.cube[self.orange][self.corner_ur] = pocket2[2]
        self.cube[self.red][self.corner_ul] = pocket1[0]
        self.cube[self.red][self.edge_u] = pocket1[1]
        self.cube[self.red][self.corner_ur] = pocket1[2]

        pocket1 = self.cube[self.yellow][self.edge_u]
        pocket2 = self.cube[self.yellow][self.edge_d]
        self.cube[self.yellow][self.edge_d] = pocket1
        self.cube[self.yellow][self.edge_u] = pocket2

        pocket1 = self.cube[self.yellow][self.edge_l]
        pocket2 = self.cube[self.yellow][self.edge_r]
        self.cube[self.yellow][self.edge_r] = pocket1
        self.cube[self.yellow][self.edge_l] = pocket2

        pocket1 = self.cube[self.yellow][self.corner_ul]
        pocket2 = self.cube[self.yellow][self.corner_dr]
        self.cube[self.yellow][self.corner_dr] = pocket1
        self.cube[self.yellow][self.corner_ul] = pocket2

        pocket1 = self.cube[self.yellow][self.corner_ur]
        pocket2 = self.cube[self.yellow][self.corner_dl]
        self.cube[self.yellow][self.corner_dl] = pocket1
        self.cube[self.yellow][self.corner_ur] = pocket2

        self.solution.append("U2")

    def d(self):
        pocket = [self.cube[self.green][self.corner_dl], self.cube[self.green][self.edge_d],
                  self.cube[self.green][self.corner_dr]]

        self.cube[self.green][self.corner_dl] = self.cube[self.red][self.corner_dl]
        self.cube[self.green][self.edge_d] = self.cube[self.red][self.edge_d]
        self.cube[self.green][self.corner_dr] = self.cube[self.red][self.corner_dr]

        self.cube[self.red][self.corner_dl] = self.cube[self.blue][self.corner_dl]
        self.cube[self.red][self.edge_d] = self.cube[self.blue][self.edge_d]
        self.cube[self.red][self.corner_dr] = self.cube[self.blue][self.corner_dr]

        self.cube[self.blue][self.corner_dl] = self.cube[self.orange][self.corner_dl]
        self.cube[self.blue][self.edge_d] = self.cube[self.orange][self.edge_d]
        self.cube[self.blue][self.corner_dr] = self.cube[self.orange][self.corner_dr]

        self.cube[self.orange][self.corner_dl] = pocket[0]
        self.cube[self.orange][self.edge_d] = pocket[1]
        self.cube[self.orange][self.corner_dr] = pocket[2]

        pocket = self.cube[self.white][self.edge_u]
        self.cube[self.white][self.edge_u] = self.cube[self.white][self.edge_l]
        self.cube[self.white][self.edge_l] = self.cube[self.white][self.edge_d]
        self.cube[self.white][self.edge_d] = self.cube[self.white][self.edge_r]
        self.cube[self.white][self.edge_r] = pocket

        pocket = self.cube[self.white][self.corner_ul]
        self.cube[self.white][self.corner_ul] = self.cube[self.white][self.corner_dl]
        self.cube[self.white][self.corner_dl] = self.cube[self.white][self.corner_dr]
        self.cube[self.white][self.corner_dr] = self.cube[self.white][self.corner_ur]
        self.cube[self.white][self.corner_ur] = pocket

        self.solution.append("D")

    def d_x(self):
        pocket = [self.cube[self.green][self.corner_dl], self.cube[self.green][self.edge_d],
                  self.cube[self.green][self.corner_dr]]

        self.cube[self.green][self.corner_dl] = self.cube[self.orange][self.corner_dl]
        self.cube[self.green][self.edge_d] = self.cube[self.orange][self.edge_d]
        self.cube[self.green][self.corner_dr] = self.cube[self.orange][self.corner_dr]

        self.cube[self.orange][self.corner_dl] = self.cube[self.blue][self.corner_dl]
        self.cube[self.orange][self.edge_d] = self.cube[self.blue][self.edge_d]
        self.cube[self.orange][self.corner_dr] = self.cube[self.blue][self.corner_dr]

        self.cube[self.blue][self.corner_dl] = self.cube[self.red][self.corner_dl]
        self.cube[self.blue][self.edge_d] = self.cube[self.red][self.edge_d]
        self.cube[self.blue][self.corner_dr] = self.cube[self.red][self.corner_dr]

        self.cube[self.red][self.corner_dl] = pocket[0]
        self.cube[self.red][self.edge_d] = pocket[1]
        self.cube[self.red][self.corner_dr] = pocket[2]

        pocket = self.cube[self.white][self.edge_u]
        self.cube[self.white][self.edge_u] = self.cube[self.white][self.edge_r]
        self.cube[self.white][self.edge_r] = self.cube[self.white][self.edge_d]
        self.cube[self.white][self.edge_d] = self.cube[self.white][self.edge_l]
        self.cube[self.white][self.edge_l] = pocket

        pocket = self.cube[self.white][self.corner_ul]
        self.cube[self.white][self.corner_ul] = self.cube[self.white][self.corner_ur]
        self.cube[self.white][self.corner_ur] = self.cube[self.white][self.corner_dr]
        self.cube[self.white][self.corner_dr] = self.cube[self.white][self.corner_dl]
        self.cube[self.white][self.corner_dl] = pocket

        self.solution.append("D'")



    def d2(self):
        pocket1 = [self.cube[self.green][self.corner_dl], self.cube[self.green][self.edge_d],
                  self.cube[self.green][self.corner_dr]]
        pocket2 = [self.cube[self.blue][self.corner_dl], self.cube[self.blue][self.edge_d],
                  self.cube[self.blue][self.corner_dr]]
        self.cube[self.green][self.corner_dl] = pocket2[0]
        self.cube[self.green][self.edge_d] = pocket2[1]
        self.cube[self.green][self.corner_dr] = pocket2[2]
        self.cube[self.blue][self.corner_dl] = pocket1[0]
        self.cube[self.blue][self.edge_d] = pocket1[1]
        self.cube[self.blue][self.corner_dr] = pocket1[2]

        pocket1 = [self.cube[self.orange][self.corner_dl], self.cube[self.orange][self.edge_d],
                   self.cube[self.orange][self.corner_dr]]
        pocket2 = [self.cube[self.red][self.corner_dl], self.cube[self.red][self.edge_d],
                   self.cube[self.red][self.corner_dr]]
        self.cube[self.orange][self.corner_dl] = pocket2[0]
        self.cube[self.orange][self.edge_d] = pocket2[1]
        self.cube[self.orange][self.corner_dr] = pocket2[2]
        self.cube[self.red][self.corner_dl] = pocket1[0]
        self.cube[self.red][self.edge_d] = pocket1[1]
        self.cube[self.red][self.corner_dr] = pocket1[2]

        pocket1 = self.cube[self.white][self.edge_u]
        pocket2 = self.cube[self.white][self.edge_d]
        self.cube[self.white][self.edge_d] = pocket1
        self.cube[self.white][self.edge_u] = pocket2

        pocket1 = self.cube[self.white][self.edge_l]
        pocket2 = self.cube[self.white][self.edge_r]
        self.cube[self.white][self.edge_r] = pocket1
        self.cube[self.white][self.edge_l] = pocket2

        pocket1 = self.cube[self.white][self.corner_ul]
        pocket2 = self.cube[self.white][self.corner_dr]
        self.cube[self.white][self.corner_dr] = pocket1
        self.cube[self.white][self.corner_ul] = pocket2

        pocket1 = self.cube[self.white][self.corner_ur]
        pocket2 = self.cube[self.white][self.corner_dl]
        self.cube[self.white][self.corner_dl] = pocket1
        self.cube[self.white][self.corner_ur] = pocket2

        self.solution.append("D2")



    def f(self):
        pocket = [self.cube[self.yellow][self.corner_dl], self.cube[self.yellow][self.edge_d],
                  self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_dr] = self.cube[self.red][self.corner_ur]
        self.cube[self.yellow][self.edge_d] = self.cube[self.red][self.edge_r]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.red][self.corner_dr]

        self.cube[self.red][self.corner_ur] = self.cube[self.white][self.corner_ul]
        self.cube[self.red][self.edge_r] = self.cube[self.white][self.edge_u]
        self.cube[self.red][self.corner_dr] = self.cube[self.white][self.corner_ur]

        self.cube[self.white][self.corner_ul] = self.cube[self.orange][self.corner_dl]
        self.cube[self.white][self.edge_u] = self.cube[self.orange][self.edge_l]
        self.cube[self.white][self.corner_ur] = self.cube[self.orange][self.corner_ul]

        self.cube[self.orange][self.corner_dl] = pocket[2]
        self.cube[self.orange][self.edge_l] = pocket[1]
        self.cube[self.orange][self.corner_ul] = pocket[0]

        pocket = self.cube[self.green][self.edge_u]
        self.cube[self.green][self.edge_u] = self.cube[self.green][self.edge_l]
        self.cube[self.green][self.edge_l] = self.cube[self.green][self.edge_d]
        self.cube[self.green][self.edge_d] = self.cube[self.green][self.edge_r]
        self.cube[self.green][self.edge_r] = pocket

        pocket = self.cube[self.green][self.corner_ul]
        self.cube[self.green][self.corner_ul] = self.cube[self.green][self.corner_dl]
        self.cube[self.green][self.corner_dl] = self.cube[self.green][self.corner_dr]
        self.cube[self.green][self.corner_dr] = self.cube[self.green][self.corner_ur]
        self.cube[self.green][self.corner_ur] = pocket

        self.solution.append("F")

    def f_x(self):
        pocket = [self.cube[self.yellow][self.corner_dl], self.cube[self.yellow][self.edge_d],
                  self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_dl] = self.cube[self.orange][self.corner_ul]
        self.cube[self.yellow][self.edge_d] = self.cube[self.orange][self.edge_l]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.orange][self.corner_dl]

        self.cube[self.orange][self.corner_ul] = self.cube[self.white][self.corner_ur]
        self.cube[self.orange][self.edge_l] = self.cube[self.white][self.edge_u]
        self.cube[self.orange][self.corner_dl] = self.cube[self.white][self.corner_ul]

        self.cube[self.white][self.corner_ur] = self.cube[self.red][self.corner_dr]
        self.cube[self.white][self.edge_u] = self.cube[self.red][self.edge_r]
        self.cube[self.white][self.corner_ul] = self.cube[self.red][self.corner_ur]

        self.cube[self.red][self.corner_dr] = pocket[0]
        self.cube[self.red][self.edge_r] = pocket[1]
        self.cube[self.red][self.corner_ur] = pocket[2]

        pocket = self.cube[self.green][self.edge_u]
        self.cube[self.green][self.edge_u] = self.cube[self.green][self.edge_r]
        self.cube[self.green][self.edge_r] = self.cube[self.green][self.edge_d]
        self.cube[self.green][self.edge_d] = self.cube[self.green][self.edge_l]
        self.cube[self.green][self.edge_l] = pocket

        pocket = self.cube[self.green][self.corner_ul]
        self.cube[self.green][self.corner_ul] = self.cube[self.green][self.corner_ur]
        self.cube[self.green][self.corner_ur] = self.cube[self.green][self.corner_dr]
        self.cube[self.green][self.corner_dr] = self.cube[self.green][self.corner_dl]
        self.cube[self.green][self.corner_dl] = pocket

        self.solution.append("F'")


    def f2(self):
        pocket1 = [self.cube[self.yellow][self.corner_dl], self.cube[self.yellow][self.edge_d],
                  self.cube[self.yellow][self.corner_dr]]
        pocket2 = [self.cube[self.white][self.corner_ur], self.cube[self.white][self.edge_u],
                  self.cube[self.white][self.corner_ul]]
        self.cube[self.yellow][self.corner_dl] = pocket2[0]
        self.cube[self.yellow][self.edge_d] = pocket2[1]
        self.cube[self.yellow][self.corner_dr] = pocket2[2]
        self.cube[self.white][self.corner_ur] = pocket1[0]
        self.cube[self.white][self.edge_u] = pocket1[1]
        self.cube[self.white][self.corner_ul] = pocket1[2]

        pocket1 = [self.cube[self.orange][self.corner_ul], self.cube[self.orange][self.edge_l],
                   self.cube[self.orange][self.corner_dl]]
        pocket2 = [self.cube[self.red][self.corner_dr], self.cube[self.red][self.edge_r],
                   self.cube[self.red][self.corner_ur]]
        self.cube[self.orange][self.corner_ul] = pocket2[0]
        self.cube[self.orange][self.edge_l] = pocket2[1]
        self.cube[self.orange][self.corner_dl] = pocket2[2]
        self.cube[self.red][self.corner_dr] = pocket1[0]
        self.cube[self.red][self.edge_r] = pocket1[1]
        self.cube[self.red][self.corner_ur] = pocket1[2]

        pocket1 = self.cube[self.green][self.edge_u]
        pocket2 = self.cube[self.green][self.edge_d]
        self.cube[self.green][self.edge_d] = pocket1
        self.cube[self.green][self.edge_u] = pocket2

        pocket1 = self.cube[self.green][self.edge_l]
        pocket2 = self.cube[self.green][self.edge_r]
        self.cube[self.green][self.edge_r] = pocket1
        self.cube[self.green][self.edge_l] = pocket2

        pocket1 = self.cube[self.green][self.corner_ul]
        pocket2 = self.cube[self.green][self.corner_dr]
        self.cube[self.green][self.corner_dr] = pocket1
        self.cube[self.green][self.corner_ul] = pocket2

        pocket1 = self.cube[self.green][self.corner_ur]
        pocket2 = self.cube[self.green][self.corner_dl]
        self.cube[self.green][self.corner_dl] = pocket1
        self.cube[self.green][self.corner_ur] = pocket2

        self.solution.append("F2")


    def b(self):
        pocket = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_u],
                  self.cube[self.yellow][self.corner_ur]]

        self.cube[self.yellow][self.corner_ul] = self.cube[self.orange][self.corner_ur]
        self.cube[self.yellow][self.edge_u] = self.cube[self.orange][self.edge_r]
        self.cube[self.yellow][self.corner_ur] = self.cube[self.orange][self.corner_dr]

        self.cube[self.orange][self.corner_ur] = self.cube[self.white][self.corner_dr]
        self.cube[self.orange][self.edge_r] = self.cube[self.white][self.edge_d]
        self.cube[self.orange][self.corner_dr] = self.cube[self.white][self.corner_dl]

        self.cube[self.white][self.corner_dr] = self.cube[self.red][self.corner_dl]
        self.cube[self.white][self.edge_d] = self.cube[self.red][self.edge_l]
        self.cube[self.white][self.corner_dl] = self.cube[self.red][self.corner_ul]

        self.cube[self.red][self.corner_dl] = pocket[0]
        self.cube[self.red][self.edge_l] = pocket[1]
        self.cube[self.red][self.corner_ul] = pocket[2]

        pocket = self.cube[self.blue][self.edge_u]
        self.cube[self.blue][self.edge_u] = self.cube[self.blue][self.edge_l]
        self.cube[self.blue][self.edge_l] = self.cube[self.blue][self.edge_d]
        self.cube[self.blue][self.edge_d] = self.cube[self.blue][self.edge_r]
        self.cube[self.blue][self.edge_r] = pocket

        pocket = self.cube[self.blue][self.corner_ul]
        self.cube[self.blue][self.corner_ul] = self.cube[self.blue][self.corner_dl]
        self.cube[self.blue][self.corner_dl] = self.cube[self.blue][self.corner_dr]
        self.cube[self.blue][self.corner_dr] = self.cube[self.blue][self.corner_ur]
        self.cube[self.blue][self.corner_ur] = pocket

        self.solution.append("B")


    def b_x(self):
        pocket = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_u],
                  self.cube[self.yellow][self.corner_ur]]

        self.cube[self.yellow][self.corner_ul] = self.cube[self.red][self.corner_dl]
        self.cube[self.yellow][self.edge_u] = self.cube[self.red][self.edge_l]
        self.cube[self.yellow][self.corner_ur] = self.cube[self.red][self.corner_ul]

        self.cube[self.red][self.corner_ul] = self.cube[self.white][self.corner_dl]
        self.cube[self.red][self.edge_l] = self.cube[self.white][self.edge_d]
        self.cube[self.red][self.corner_dl] = self.cube[self.white][self.corner_dr]

        self.cube[self.white][self.corner_dl] = self.cube[self.orange][self.corner_dr]
        self.cube[self.white][self.edge_d] = self.cube[self.orange][self.edge_r]
        self.cube[self.white][self.corner_dr] = self.cube[self.orange][self.corner_ur]

        self.cube[self.orange][self.corner_dr] = pocket[2]
        self.cube[self.orange][self.edge_r] = pocket[1]
        self.cube[self.orange][self.corner_ur] = pocket[0]

        pocket = self.cube[self.blue][self.edge_u]
        self.cube[self.blue][self.edge_u] = self.cube[self.blue][self.edge_r]
        self.cube[self.blue][self.edge_r] = self.cube[self.blue][self.edge_d]
        self.cube[self.blue][self.edge_d] = self.cube[self.blue][self.edge_l]
        self.cube[self.blue][self.edge_l] = pocket

        pocket = self.cube[self.blue][self.corner_ul]
        self.cube[self.blue][self.corner_ul] = self.cube[self.blue][self.corner_ur]
        self.cube[self.blue][self.corner_ur] = self.cube[self.blue][self.corner_dr]
        self.cube[self.blue][self.corner_dr] = self.cube[self.blue][self.corner_dl]
        self.cube[self.blue][self.corner_dl] = pocket

        self.solution.append("B'")


    def b2(self):
        pocket1 = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_u],
                  self.cube[self.yellow][self.corner_ur]]
        pocket2 = [self.cube[self.white][self.corner_dr], self.cube[self.white][self.edge_d],
                  self.cube[self.white][self.corner_dl]]
        self.cube[self.yellow][self.corner_ul] = pocket2[0]
        self.cube[self.yellow][self.edge_u] = pocket2[1]
        self.cube[self.yellow][self.corner_ur] = pocket2[2]
        self.cube[self.white][self.corner_dr] = pocket1[0]
        self.cube[self.white][self.edge_d] = pocket1[1]
        self.cube[self.white][self.corner_dl] = pocket1[2]

        pocket1 = [self.cube[self.orange][self.corner_ur], self.cube[self.orange][self.edge_r],
                   self.cube[self.orange][self.corner_dr]]
        pocket2 = [self.cube[self.red][self.corner_dl], self.cube[self.red][self.edge_l],
                   self.cube[self.red][self.corner_ul]]
        self.cube[self.orange][self.corner_ur] = pocket2[0]
        self.cube[self.orange][self.edge_r] = pocket2[1]
        self.cube[self.orange][self.corner_dr] = pocket2[2]
        self.cube[self.red][self.corner_dl] = pocket1[0]
        self.cube[self.red][self.edge_l] = pocket1[1]
        self.cube[self.red][self.corner_ul] = pocket1[2]

        pocket1 = self.cube[self.blue][self.edge_u]
        pocket2 = self.cube[self.blue][self.edge_d]
        self.cube[self.blue][self.edge_d] = pocket1
        self.cube[self.blue][self.edge_u] = pocket2

        pocket1 = self.cube[self.blue][self.edge_l]
        pocket2 = self.cube[self.blue][self.edge_r]
        self.cube[self.blue][self.edge_r] = pocket1
        self.cube[self.blue][self.edge_l] = pocket2

        pocket1 = self.cube[self.blue][self.corner_ul]
        pocket2 = self.cube[self.blue][self.corner_dr]
        self.cube[self.blue][self.corner_dr] = pocket1
        self.cube[self.blue][self.corner_ul] = pocket2

        pocket1 = self.cube[self.blue][self.corner_ur]
        pocket2 = self.cube[self.blue][self.corner_dl]
        self.cube[self.blue][self.corner_dl] = pocket1
        self.cube[self.blue][self.corner_ur] = pocket2

        self.solution.append("B2")


    def m(self):
        pocket = [self.cube[self.yellow][self.edge_u], self.cube[self.yellow][self.centre],
                  self.cube[self.yellow][self.edge_d]]
        self.cube[self.yellow][self.edge_u] = self.cube[self.blue][self.edge_blue_d]
        self.cube[self.yellow][self.centre] = self.cube[self.blue][self.centre]
        self.cube[self.yellow][self.edge_d] = self.cube[self.blue][self.edge_blue_u]

        self.cube[self.blue][self.edge_blue_d] = self.cube[self.white][self.edge_d]
        self.cube[self.blue][self.centre] = self.cube[self.white][self.centre]
        self.cube[self.blue][self.edge_blue_u] = self.cube[self.white][self.edge_u]

        self.cube[self.white][self.edge_d] = self.cube[self.green][self.edge_d]
        self.cube[self.white][self.centre] = self.cube[self.green][self.centre]
        self.cube[self.white][self.edge_u] = self.cube[self.green][self.edge_u]

        self.cube[self.green][self.edge_d] = pocket[0]
        self.cube[self.green][self.centre] = pocket[1]
        self.cube[self.green][self.edge_u] = pocket[2]

        self.solution.append("M")

    def m_x(self):
        pocket = [self.cube[self.yellow][self.edge_u], self.cube[self.yellow][self.centre],
                  self.cube[self.yellow][self.edge_d]]
        self.cube[self.yellow][self.edge_u] = self.cube[self.green][self.edge_u]
        self.cube[self.yellow][self.centre] = self.cube[self.green][self.centre]
        self.cube[self.yellow][self.edge_d] = self.cube[self.green][self.edge_d]

        self.cube[self.green][self.edge_u] = self.cube[self.white][self.edge_u]
        self.cube[self.green][self.centre] = self.cube[self.white][self.centre]
        self.cube[self.green][self.edge_d] = self.cube[self.white][self.edge_d]

        self.cube[self.white][self.edge_u] = self.cube[self.blue][self.edge_blue_u]
        self.cube[self.white][self.centre] = self.cube[self.blue][self.centre]
        self.cube[self.white][self.edge_d] = self.cube[self.blue][self.edge_blue_d]

        self.cube[self.blue][self.edge_blue_u] = pocket[0]
        self.cube[self.blue][self.centre] = pocket[1]
        self.cube[self.blue][self.edge_blue_d] = pocket[2]

        self.solution.append("M'")

    def m2(self):
        pocket1 = [self.cube[self.yellow][self.edge_u], self.cube[self.yellow][self.centre],
                  self.cube[self.yellow][self.edge_d]]
        pocket2 = [self.cube[self.white][self.edge_u], self.cube[self.white][self.centre],
                   self.cube[self.white][self.edge_d]]
        self.cube[self.yellow][self.edge_u] = pocket2[0]
        self.cube[self.yellow][self.centre] = pocket2[1]
        self.cube[self.yellow][self.edge_d] = pocket2[2]
        self.cube[self.white][self.edge_u] = pocket1[0]
        self.cube[self.white][self.centre] = pocket1[1]
        self.cube[self.white][self.edge_d] = pocket1[2]

        pocket1 = [self.cube[self.green][self.edge_u], self.cube[self.green][self.centre],
                   self.cube[self.green][self.edge_d]]
        pocket2 = [self.cube[self.blue][self.edge_blue_u], self.cube[self.blue][self.centre],
                   self.cube[self.blue][self.edge_blue_d]]
        self.cube[self.green][self.edge_u] = pocket2[0]
        self.cube[self.green][self.centre] = pocket2[1]
        self.cube[self.green][self.edge_d] = pocket2[2]
        self.cube[self.blue][self.edge_blue_u] = pocket1[0]
        self.cube[self.blue][self.centre] = pocket1[1]
        self.cube[self.blue][self.edge_blue_d] = pocket1[2]

        self.solution.append("M2")

    def e(self):
        pocket = [self.cube[self.green][self.edge_l], self.cube[self.green][self.centre],
                  self.cube[self.green][self.edge_r]]
        self.cube[self.green][self.edge_l] = self.cube[self.orange][self.edge_l]
        self.cube[self.green][self.centre] = self.cube[self.orange][self.centre]
        self.cube[self.green][self.edge_r] = self.cube[self.orange][self.edge_r]

        self.cube[self.orange][self.edge_l] = self.cube[self.blue][self.edge_l]
        self.cube[self.orange][self.centre] = self.cube[self.blue][self.centre]
        self.cube[self.orange][self.edge_r] = self.cube[self.blue][self.edge_r]

        self.cube[self.blue][self.edge_l] = self.cube[self.red][self.edge_l]
        self.cube[self.blue][self.centre] = self.cube[self.red][self.centre]
        self.cube[self.blue][self.edge_r] = self.cube[self.red][self.edge_r]

        self.cube[self.red][self.edge_l] = pocket[0]
        self.cube[self.red][self.centre] = pocket[1]
        self.cube[self.red][self.edge_r] = pocket[2]

        self.solution.append("E")

    def e_x(self):
        pocket = [self.cube[self.green][self.edge_l], self.cube[self.green][self.centre],
                  self.cube[self.green][self.edge_r]]
        self.cube[self.green][self.edge_l] = self.cube[self.red][self.edge_l]
        self.cube[self.green][self.centre] = self.cube[self.red][self.centre]
        self.cube[self.green][self.edge_r] = self.cube[self.red][self.edge_r]

        self.cube[self.red][self.edge_l] = self.cube[self.blue][self.edge_l]
        self.cube[self.red][self.centre] = self.cube[self.blue][self.centre]
        self.cube[self.red][self.edge_r] = self.cube[self.blue][self.edge_r]

        self.cube[self.blue][self.edge_l] = self.cube[self.orange][self.edge_l]
        self.cube[self.blue][self.centre] = self.cube[self.orange][self.centre]
        self.cube[self.blue][self.edge_r] = self.cube[self.orange][self.edge_r]

        self.cube[self.orange][self.edge_l] = pocket[0]
        self.cube[self.orange][self.centre] = pocket[1]
        self.cube[self.orange][self.edge_r] = pocket[2]

        self.solution.append("E'")

    def e2(self):
        pocket1 = [self.cube[self.green][self.edge_l], self.cube[self.green][self.centre],
                  self.cube[self.green][self.edge_r]]
        pocket2 = [self.cube[self.blue][self.edge_l], self.cube[self.blue][self.centre],
                   self.cube[self.blue][self.edge_r]]
        self.cube[self.green][self.edge_l] = pocket2[0]
        self.cube[self.green][self.centre] = pocket2[1]
        self.cube[self.green][self.edge_r] = pocket2[2]
        self.cube[self.blue][self.edge_l] = pocket1[0]
        self.cube[self.blue][self.centre] = pocket1[1]
        self.cube[self.blue][self.edge_r] = pocket1[2]

        pocket1 = [self.cube[self.orange][self.edge_l], self.cube[self.orange][self.centre],
                   self.cube[self.orange][self.edge_r]]
        pocket2 = [self.cube[self.red][self.edge_l], self.cube[self.red][self.centre],
                   self.cube[self.red][self.edge_r]]
        self.cube[self.orange][self.edge_l] = pocket2[0]
        self.cube[self.orange][self.centre] = pocket2[1]
        self.cube[self.orange][self.edge_r] = pocket2[2]
        self.cube[self.red][self.edge_l] = pocket1[0]
        self.cube[self.red][self.centre] = pocket1[1]
        self.cube[self.red][self.edge_r] = pocket1[2]

        self.solution.append("E2")

    def s(self):
        pocket = [self.cube[self.white][self.edge_l], self.cube[self.white][self.centre],
                  self.cube[self.white][self.edge_r]]
        self.cube[self.yellow][self.edge_l] = self.cube[self.red][self.edge_u]
        self.cube[self.yellow][self.centre] = self.cube[self.red][self.centre]
        self.cube[self.yellow][self.edge_r] = self.cube[self.red][self.edge_d]

        self.cube[self.red][self.edge_u] = self.cube[self.white][self.edge_l]
        self.cube[self.red][self.centre] = self.cube[self.white][self.centre]
        self.cube[self.red][self.edge_d] = self.cube[self.white][self.edge_r]

        self.cube[self.white][self.edge_r] = self.cube[self.orange][self.edge_d]
        self.cube[self.white][self.centre] = self.cube[self.orange][self.centre]
        self.cube[self.white][self.edge_l] = self.cube[self.orange][self.edge_u]

        self.cube[self.orange][self.edge_d] = pocket[0]
        self.cube[self.orange][self.centre] = pocket[1]
        self.cube[self.orange][self.edge_u] = pocket[2]

        self.solution.append("S")

    def s_x(self):
        pocket = [self.cube[self.white][self.edge_l], self.cube[self.white][self.centre],
                  self.cube[self.white][self.edge_r]]
        self.cube[self.yellow][self.edge_l] = self.cube[self.orange][self.edge_u]
        self.cube[self.yellow][self.centre] = self.cube[self.orange][self.centre]
        self.cube[self.yellow][self.edge_r] = self.cube[self.orange][self.edge_d]

        self.cube[self.orange][self.edge_u] = self.cube[self.white][self.edge_r]
        self.cube[self.orange][self.centre] = self.cube[self.white][self.centre]
        self.cube[self.orange][self.edge_d] = self.cube[self.white][self.edge_l]

        self.cube[self.white][self.edge_r] = self.cube[self.red][self.edge_d]
        self.cube[self.white][self.centre] = self.cube[self.red][self.centre]
        self.cube[self.white][self.edge_l] = self.cube[self.red][self.edge_u]

        self.cube[self.red][self.edge_d] = pocket[0]
        self.cube[self.red][self.centre] = pocket[1]
        self.cube[self.red][self.edge_u] = pocket[2]

        self.solution.append("S'")

    def s2(self):
        pocket1 = [self.cube[self.red][self.edge_u], self.cube[self.red][self.centre],
                  self.cube[self.red][self.edge_d]]
        pocket2 = [self.cube[self.orange][self.edge_d], self.cube[self.orange][self.centre],
                   self.cube[self.orange][self.edge_u]]
        self.cube[self.red][self.edge_u] = pocket2[0]
        self.cube[self.red][self.centre] = pocket2[1]
        self.cube[self.red][self.edge_d] = pocket2[2]
        self.cube[self.orange][self.edge_d] = pocket1[0]
        self.cube[self.orange][self.centre] = pocket1[1]
        self.cube[self.orange][self.edge_u] = pocket1[2]

        pocket1 = [self.cube[self.yellow][self.edge_l], self.cube[self.yellow][self.centre],
                   self.cube[self.yellow][self.edge_r]]
        pocket2 = [self.cube[self.white][self.edge_r], self.cube[self.white][self.centre],
                   self.cube[self.white][self.edge_l]]
        self.cube[self.yellow][self.edge_l] = pocket2[0]
        self.cube[self.yellow][self.centre] = pocket2[1]
        self.cube[self.yellow][self.edge_r] = pocket2[2]
        self.cube[self.white][self.edge_r] = pocket1[0]
        self.cube[self.white][self.centre] = pocket1[1]
        self.cube[self.white][self.edge_l] = pocket1[2]

        self.solution.append("S2")

    def rw(self):
        self.r()
        self.m_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Rw")

    def rw_x(self):
        self.r_x()
        self.m()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Rw'")

    def rw2(self):
        self.r2()
        self.m2()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Rw2")

    def lw(self):
        self.l()
        self.m()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Lw")

    def lw_x(self):
        self.l_x()
        self.m_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Lw'")

    def lw2(self):
        self.l2()
        self.m2()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Lw2")

    def uw(self):
        self.u()
        self.e()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Uw")

    def uw_x(self):
        self.u_x()
        self.e_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Uw'")

    def uw2(self):
        self.u2()
        self.e2()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Uw2")

    def dw(self):
        self.d()
        self.e_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Dw")

    def dw_x(self):
        self.d_x()
        self.e()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Dw'")

    def dw2(self):
        self.d2()
        self.e2()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Dw2")

    def fw(self):
        self.f()
        self.s()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Fw")

    def fw_x(self):
        self.f_x()
        self.s_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Fw'")

    def fw2(self):
        self.f2()
        self.s2()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("Fw2")

    # no bw

    def x(self):
        self.r()
        self.m_x()
        self.l_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("x")

    def x_x(self):
        self.r_x()
        self.m()
        self.l()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("x'")

    def x2(self):
        self.r2()
        self.m2()
        self.l2()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("x2")
        
    def y(self):
        self.u()
        self.e()
        self.d_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("y")

    def y_x(self):
        self.u_x()
        self.e_x()
        self.d()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("y'")

    def y2(self):
        self.u2()
        self.e2()
        self.d2()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("y2")

    def z(self):
        self.f()
        self.s()
        self.b_x()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("z")

    def z_x(self):
        self.f_x()
        self.s_x()
        self.b()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("z'")

    def z2(self):
        self.f2()
        self.s2()
        self.b2()
        self.solution.pop()
        self.solution.pop()
        self.solution.pop()
        self.solution.append("z2")

    def define(self):
        # data is defined in accordance with self.colors
        self.cube = []
        write("Put the cube's white side up and green side at the front.")
        for i in range(0,6):
            cube_scan = []
            while True:
                if i==5:
                    write(self.msgs[i]+' (Green at the back): ')
                else:
                    write(self.msgs[i]+': ')
                ans = input()
                if len(ans)!=9:
                    write('Please, enter 9 cells of the '+self.msgs[i]+'.')
                elif not(self.right_letters(ans)):
                    write('Please, enter only '+str(self.colors)+' letters without spaces, other letters are not allowed.')
                else:
                    for i1 in range(0,9):
                        cube_scan.append(ans[i1])
                    self.cube.append(cube_scan)
                    break
        check_msg = self.check()
        if check_msg=='OK':
            return True
        else:
            write(check_msg)
            return False

    def right_letters(self, side):
        for i in range(0,9):
            if side[i] in self.colors:
                continue
            else:
                return False
        return True


    def check(self):
        much = [0,0,0,0,0,0]
        for i in range(0,6):
            if self.cube[i][self.centre]!=self.colors[i]:
                return 'The centre of the ' + self.msgs[i] + ' does not match with your centre. Please try again.'
            for i1 in range(0,9):
                if i1==4:
                    continue
                much[self.colors.index(self.cube[i][i1])]+=1  #try
        for i in range(0,6):
            if much[i]!=8:
                return 'You entered too many ' + self.colors[i] + ' elements on your Cube. Please try again'
        #TODO: Add corners and edges check
        #TODO: where are centres
        return 'OK'

    def solve(self):
        write('begin: ' + str(self.cube))
        #solve.cfop()
        self.cross()
        write(self.solution)

    def cross(self):
        downs = ['g','o','b','r']
        for i in range(1, 5):
            found = False
            edges = self.edges_get()
            edges_reversed = self.edges_get_reversed()
            for i1 in range(0,12):
                if edges[i1]=='w':
                    if downs.index(edges_reversed[i1]) in downs:
                        self.cross_do(i1, False, downs.index(edges_reversed[i1]))
                        downs[downs.index(edges_reversed[i1])]=''
                        found = True
                    else:
                        pass
                elif edges_reversed[i1]=='w':
                    if downs.index(edges[i1]) in downs:
                        self.cross_do(i1, False, downs.index(edges_reversed[i1]))
                        downs[downs.index(edges_reversed[i1])]=''
                        found = True
                    else:
                        pass
            if found:
                continue

    def cross_do(self,pos, rev, color_edge):
        if color_edge == 'g':
            if not(rev):
                if pos==1:
                    self.r2()
                    self.u()
                    self.f2()
                elif pos==2:
                    self.b2()
                    self.u2()
                    self.f2()
                elif pos==3:
                    self.l2()
                    self.u_x()
                    self.f2()
                elif pos == 4:
                    self.d_x()
                    self.l()
                    self.d()
                elif pos == 5:
                    self.d()
                    self.r_x()
                    self.d_x()
                elif pos == 6:
                    self.d()
                    self.r()
                    self.d_x()
                elif pos == 7:
                    self.d_x()
                    self.l_x()
                    self.d()
                elif pos == 8:
                    self.u2()
                    self.f2()
                elif pos == 9:
                    self.u()
                    self.f2()
                elif pos == 10:
                    self.f2()
                elif pos == 11:
                    self.u_x()
                    self.f2()
            else:
                if pos==0:
                    self.f()
                    self.d_x()
                    self.l()
                    self.d()
                elif pos==1:
                    self.r()
                    self.f()
                elif pos==2:
                    self.b()
                    self.d()
                    self.r()
                    self.d_x()
                elif pos==3:
                    self.l_x()
                    self.f_x()
                elif pos == 4:
                    self.f_x()
                elif pos == 5:
                    self.f()
                elif pos == 6:
                    self.d2()
                    self.b_x()
                    self.d2()
                elif pos == 7:
                    self.d2()
                    self.b()
                    self.d2()
                elif pos == 8:
                    self.u()
                    self.r_x()
                    self.f()
                    self.r()
                elif pos == 9:
                    self.r_x()
                    self.f()
                    self.r()
                elif pos == 10:
                    self.u_x()
                    self.r_x()
                    self.f()
                    self.r()
                elif pos == 11:
                    self.l()
                    self.f_x()
                    self.l_x()
        elif color_edge == 'o':
            if not(rev):
                if pos==0:
                    self.f2()
                    self.u_x()
                    self.r2()
                elif pos==2:
                    self.b2()
                    self.u()
                    self.r2()
                elif pos==3:
                    self.l2()
                    self.u2()
                    self.r2()
                elif pos == 4:
                    self.f2()
                    self.r_x()
                    self.f2()
                elif pos == 5:
                    self.r_x()
                elif pos == 6:
                    self.r()
                elif pos == 7:
                    self.d2()
                    self.l_x()
                    self.d2()
                elif pos == 8:
                    self.u()
                    self.r2()
                elif pos == 9:
                    self.r2()
                elif pos == 10:
                    self.u_x()
                    self.r2()
                elif pos == 11:
                    self.u2()
                    self.r2()
            else:
                if pos==0:
                    self.f_x()
                    self.r_x()
                elif pos==1:
                    self.r()
                    self.d_x()
                    self.f()
                    self.d()
                elif pos==2:
                    self.b()
                    self.d()
                    self.r()
                    self.d_x()
                elif pos==3:
                    self.l_x()
                    self.d_x()
                    self.f_x()
                    self.d()
                elif pos == 4:
                    self.d_x()
                    self.f_x()
                    self.d()
                elif pos == 5:
                    self.d_x()
                    self.f()
                    self.d()
                elif pos == 6:
                    self.d()
                    self.b_x()
                    self.d_x()
                elif pos == 7:
                    self.d()
                    self.b()
                    self.d_x()
                elif pos == 8:
                    self.b()
                    self.r()
                    self.b_x()
                elif pos == 9:
                    self.u()
                    self.f()
                    self.r_x()
                    self.f_x()
                elif pos == 10:
                    self.f()
                    self.r_x()
                    self.f_x()
                elif pos == 11:
                    self.u_x()
                    self.f()
                    self.r_x()
                    self.f_x()
        elif color_edge == 'b':
            if not(rev):
                if pos==0:
                    self.f2()
                    self.u2()
                    self.b2()
                elif pos==1:
                    self.r2()
                    self.u_x()
                    self.b2()
                elif pos==3:
                    self.l2()
                    self.u()
                    self.b2()
                elif pos == 4:
                    self.d()
                    self.l()
                    self.d_x()
                elif pos == 5:
                    self.d_x()
                    self.r_x()
                    self.d()
                elif pos == 6:
                    self.d_x()
                    self.r()
                    self.d()
                elif pos == 7:
                    self.d()
                    self.l_x()
                    self.d_x()
                elif pos == 8:
                    self.b2()
                elif pos == 9:
                    self.u_x()
                    self.b2()
                elif pos == 10:
                    self.u2()
                    self.b2()
                elif pos == 11:
                    self.u()
                    self.b2()
            else:
                if pos==0:
                    self.f_x()
                    self.d_x()
                    self.r_x()
                    self.d()
                elif pos==1:
                    self.r_x()
                    self.b_x()
                    self.r()
                elif pos==2:
                    self.b()
                    self.d_x()
                    self.r()
                    self.d()
                elif pos==3:
                    self.l()
                    self.b()
                    self.l_x()
                elif pos == 4:
                    self.l2()
                    self.b()
                    self.l2()
                elif pos == 5:
                    self.r2()
                    self.b_x()
                    self.r2()
                elif pos == 6:
                    self.b_x()
                elif pos == 7:
                    self.b()
                elif pos == 8:
                    self.u()
                    self.r()
                    self.b_x()
                    self.r_x()
                elif pos == 9:
                    self.r()
                    self.b_x()
                    self.r_x()
                elif pos == 10:
                    self.u_x()
                    self.r()
                    self.b_x()
                    self.r_x()
                elif pos == 11:
                    self.l_x()
                    self.b()
                    self.l()
        elif color_edge == 'r':
            if not(rev):
                if pos==0:
                    self.f2()
                    self.u()
                    self.l2()
                elif pos==1:
                    self.r2()
                    self.u2()
                    self.l2()
                elif pos==2:
                    self.b2()
                    self.u_x()
                    self.l2()
                elif pos == 4:
                    self.l()
                elif pos == 5:
                    self.f2()
                    self.l()
                    self.f2()
                elif pos == 6:
                    self.b2()
                    self.l_x()
                    self.b2()
                elif pos == 7:
                    self.l_x()
                elif pos == 8:
                    self.u_x()
                    self.l2()
                elif pos == 9:
                    self.u2()
                    self.l2()
                elif pos == 10:
                    self.u()
                    self.l2()
                elif pos == 11:
                    self.l2()
            else:
                if pos==0:
                    self.f()
                    self.l()
                elif pos==1:
                    self.r()
                    self.d()
                    self.f()
                    self.d_x()
                elif pos==2:
                    self.b_x()
                    self.l_x()
                elif pos==3:
                    self.l_x()
                    self.d()
                    self.f_x()
                    self.d_x()
                elif pos == 4:
                    self.d()
                    self.f_x()
                    self.d_x()
                elif pos == 5:
                    self.d()
                    self.f()
                    self.d_x()
                elif pos == 6:
                    self.d_x()
                    self.b_x()
                    self.d()
                elif pos == 7:
                    self.d_x()
                    self.b()
                    self.d()
                elif pos == 8:
                    self.b()
                    self.l_x()
                    self.b_x()
                elif pos == 9:
                    self.u()
                    self.f_x()
                    self.l()
                    self.f()
                elif pos == 10:
                    self.f_x()
                    self.l()
                    self.f()
                elif pos == 11:
                    self.u_x()
                    self.f_x()
                    self.l()
                    self.f()



    def edges_get(self):
        edges = [
            self.cube[self.white][self.edge_u], #0
            self.cube[self.white][self.edge_r], #1
            self.cube[self.white][self.edge_d], #2
            self.cube[self.white][self.edge_l], #3

            self.cube[self.green][self.edge_l], #4
            self.cube[self.green][self.edge_r], #5
            self.cube[self.blue][self.edge_l], #6
            self.cube[self.blue][self.edge_r], #7

            self.cube[self.yellow][self.edge_u], #8
            self.cube[self.yellow][self.edge_r], #9
            self.cube[self.yellow][self.edge_d], #10
            self.cube[self.yellow][self.edge_l], #11
        ]
        return edges

    def edges_get_reversed(self):
        edges = [
            self.cube[self.green][self.edge_d],  #0
            self.cube[self.orange][self.edge_d], #1
            self.cube[self.blue][self.edge_d], #2
            self.cube[self.red][self.edge_d], #3

            self.cube[self.red][self.edge_r], #4
            self.cube[self.orange][self.edge_l], #5
            self.cube[self.orange][self.edge_r], #6
            self.cube[self.red][self.edge_l], #7

            self.cube[self.blue][self.edge_u], #8
            self.cube[self.orange][self.edge_u], #9
            self.cube[self.green][self.edge_u], #10
            self.cube[self.red][self.edge_u], #11

        ]
        return edges


def write(msg):
    print(msg)