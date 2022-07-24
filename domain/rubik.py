class Cube:
    def __init__(self):
        self.solved = False
        self.cube = [['w','w','w','w','w','w','w','w','w'],['g','g','g','g','g','g','g','g','g'],['o','o','o','o','o','o','o','o','o'],['b','b','b','b','b','b','b','b','b'],['r','r','r','r','r','r','r','r','r'],['y','y','y','y','y','y','y','y','y']]
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

    def r(self):
        pocket = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r], self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_ur]=self.cube[self.green][self.corner_ur]
        self.cube[self.yellow][self.edge_r] = self.cube[self.green][self.edge_r]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.green][self.corner_dr]

        self.cube[self.green][self.corner_ur] = self.cube[self.white][self.corner_ur]
        self.cube[self.green][self.edge_r] = self.cube[self.white][self.edge_r]
        self.cube[self.green][self.corner_dr] = self.cube[self.white][self.corner_dr]

        self.cube[self.white][self.corner_ur] = self.cube[self.blue][self.corner_ur]
        self.cube[self.white][self.edge_r] = self.cube[self.blue][self.edge_r]
        self.cube[self.white][self.corner_dr] = self.cube[self.blue][self.corner_dr]

        self.cube[self.blue][self.corner_ur] = pocket[0]
        self.cube[self.blue][self.edge_r] = pocket[1]
        self.cube[self.blue][self.corner_dr] = pocket[2]

        pocket = self.cube[self.orange][self.edge_u]
        self.cube[self.orange][self.edge_u] = self.cube[self.orange][self.edge_l]
        self.cube[self.orange][self.edge_l] = self.cube[self.orange][self.edge_d]
        self.cube[self.orange][self.edge_d] = self.cube[self.orange][self.edge_r]
        self.cube[self.orange][self.edge_r] = pocket

        pocket = self.cube[self.orange][self.corner_ul]
        self.cube[self.orange][self.corner_ul] = self.cube[self.orange][self.corner_dl]
        self.cube[self.orange][self.corner_dl] = self.cube[self.orange][self.corner_dr]
        self.cube[self.orange][self.corner_dr] = self.cube[self.orange][self.corner_ur]
        self.cube[self.orange][self.corner_dr] = pocket




    def r_x(self):
        write(self.cube)
        pocket = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r], self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_ur]=self.cube[self.blue][self.corner_ur]
        self.cube[self.yellow][self.edge_r] = self.cube[self.blue][self.edge_r]
        self.cube[self.yellow][self.corner_dr] = self.cube[self.blue][self.corner_dr]

        self.cube[self.blue][self.corner_ur] = self.cube[self.white][self.corner_ur]
        self.cube[self.blue][self.edge_r] = self.cube[self.white][self.edge_r]
        self.cube[self.blue][self.corner_dr] = self.cube[self.white][self.corner_dr]

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
        pocket2 = [self.cube[self.blue][self.corner_ur], self.cube[self.blue][self.edge_r],
                   self.cube[self.blue][self.corner_dr]]
        self.cube[self.green][self.corner_ur] = pocket2[0]
        self.cube[self.green][self.edge_r] = pocket2[1]
        self.cube[self.green][self.corner_dr] = pocket2[2]
        self.cube[self.blue][self.corner_ur] = pocket1[0]
        self.cube[self.blue][self.edge_r] = pocket1[1]
        self.cube[self.blue][self.corner_dr] = pocket1[2]

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

        self.cube[self.yellow][self.corner_ul]=self.cube[self.blue][self.corner_ul]
        self.cube[self.yellow][self.edge_l] = self.cube[self.blue][self.edge_l]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.blue][self.corner_dl]

        self.cube[self.blue][self.corner_ul] = self.cube[self.white][self.corner_ul]
        self.cube[self.blue][self.edge_l] = self.cube[self.white][self.edge_l]
        self.cube[self.blue][self.corner_dl] = self.cube[self.white][self.corner_dl]

        self.cube[self.white][self.corner_ul] = self.cube[self.green][self.corner_ul]
        self.cube[self.white][self.edge_l] = self.cube[self.green][self.edge_l]
        self.cube[self.white][self.corner_dl] = self.cube[self.green][self.corner_dl]

        self.cube[self.green][self.corner_ul] = pocket[0]
        self.cube[self.green][self.edge_l] = pocket[1]
        self.cube[self.green][self.corner_dl] = pocket[2]

        pocket = self.cube[self.red][self.edge_u]
        self.cube[self.red][self.edge_u] = self.cube[self.red][self.edge_l]
        self.cube[self.red][self.edge_l] = self.cube[self.red][self.edge_d]
        self.cube[self.red][self.edge_d] = self.cube[self.red][self.edge_r]
        self.cube[self.red][self.edge_r] = pocket

        pocket = self.cube[self.red][self.corner_ul]
        self.cube[self.red][self.corner_ul] = self.cube[self.red][self.corner_dl]
        self.cube[self.red][self.corner_dl] = self.cube[self.red][self.corner_dr]
        self.cube[self.red][self.corner_dr] = self.cube[self.red][self.corner_ur]
        self.cube[self.red][self.corner_dr] = pocket

    def l_x(self):
        pocket = [self.cube[self.yellow][self.corner_ul], self.cube[self.yellow][self.edge_l], self.cube[self.yellow][self.corner_dl]]

        self.cube[self.yellow][self.corner_ul]=self.cube[self.green][self.corner_ul]
        self.cube[self.yellow][self.edge_l] = self.cube[self.green][self.edge_l]
        self.cube[self.yellow][self.corner_dl] = self.cube[self.green][self.corner_dl]

        self.cube[self.green][self.corner_ul] = self.cube[self.white][self.corner_ul]
        self.cube[self.green][self.edge_l] = self.cube[self.white][self.edge_l]
        self.cube[self.green][self.corner_dl] = self.cube[self.white][self.corner_dl]

        self.cube[self.white][self.corner_ul] = self.cube[self.blue][self.corner_ul]
        self.cube[self.white][self.edge_l] = self.cube[self.blue][self.edge_l]
        self.cube[self.white][self.corner_dl] = self.cube[self.blue][self.corner_dl]

        self.cube[self.blue][self.corner_ul] = pocket[0]
        self.cube[self.blue][self.edge_l] = pocket[1]
        self.cube[self.blue][self.corner_dl] = pocket[2]

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
        pocket2 = [self.cube[self.blue][self.corner_ul], self.cube[self.blue][self.edge_l],
                   self.cube[self.blue][self.corner_dl]]
        self.cube[self.green][self.corner_ul] = pocket2[0]
        self.cube[self.green][self.edge_l] = pocket2[1]
        self.cube[self.green][self.corner_dl] = pocket2[2]
        self.cube[self.blue][self.corner_ul] = pocket1[0]
        self.cube[self.blue][self.edge_l] = pocket1[1]
        self.cube[self.blue][self.corner_dl] = pocket1[2]

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








    def define(self):
        # data is defined in accordance with self.colors
        write("Put the cube's white side up and green side at the front.")
        cube_scan = []
        for i in range(0,6):
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
        self.cube = cube_scan
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
        return 'OK'

    def solve(self):
        self.r()


def write(msg):
    print(msg)