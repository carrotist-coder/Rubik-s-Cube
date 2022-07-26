class Cube:
    def __init__(self):
        self.solved = False
        self.cube = [
            ['w','w','w','w','w','w','w','w','w'],
            ['g','g','g','g','g','g','g','g','g'],
            ['o','o','o','o','o','o','o','o','o'],
            ['b','b','b','b','b','b','b','b','b'],
            ['r','r','r','r','r','r','r','r','r'],
            ['y','y','y','y','y','y','y','y','y']]
        self.solution = ['y2']
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

    def rw(self):
        self.r()
        self.m_x()

    def rw_x(self):
        self.r_x()
        self.m()

    def rw2(self):
        self.r2()
        self.m2()

    def lw(self):
        self.l()
        self.m()

    def lw_x(self):
        self.l_x()
        self.m_x()

    def lw2(self):
        self.l2()
        self.m2()

    def uw(self):
        self.u()
        self.e()

    def uw_x(self):
        self.u_x()
        self.e_x()

    def uw2(self):
        self.u2()
        self.e2()

    def dw(self):
        self.d()
        self.e_x()

    def dw_x(self):
        self.d_x()
        self.e()

    def dw2(self):
        self.d2()
        self.e2()

    def fw(self):
        self.f()
        self.s()

    def fw_x(self):
        self.f_x()
        self.s_x()

    def fw2(self):
        self.f2()
        self.s2()

    # no bw

    def x(self):
        self.r()
        self.m_x()
        self.l_x()

    def x_x(self):
        self.r_x()
        self.m()
        self.l()

    def x2(self):
        self.r2()
        self.m2()
        self.l2()
        
    def y(self):
        self.u()
        self.e()
        self.d_x()

    def y_x(self):
        self.u_x()
        self.e_x()
        self.d()

    def y2(self):
        self.u2()
        self.e2()
        self.d2()

    def z(self):
        self.f()
        self.s()
        self.b_x()

    def z_x(self):
        self.f_x()
        self.s_x()
        self.b()

    def z2(self):
        self.f2()
        self.s2()
        self.b2()





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
        #self.r()
        #self.u()
        for zzz in range(0,2):
            self.f()
            write(self.cube)
            self.r()
            write(self.cube)
            self.u_x()
            write(self.cube)
            self.r_x()
            write(self.cube)
            self.u_x()
            write(self.cube)
            self.r()
            write(self.cube)
            self.u()
            write(self.cube)
            self.r_x()
            write(self.cube)
            self.f_x()
            write(self.cube)
            self.r()
            write(self.cube)
            self.u()
            write(self.cube)
            self.r_x()
            write(self.cube)
            self.u_x()
            write(self.cube)
            self.r_x()
            write(self.cube)
            self.f()
            write(self.cube)
            self.r()
            write(self.cube)
            self.f_x()
            write(self.cube)
            write(zzz+1)


def write(msg):
    print(msg)