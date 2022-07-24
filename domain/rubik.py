class Cube:
    def __init__(self):
        self.solved = False
        self.cube = [['wwwwwwwww','ggggggggg','ooooooooo','bbbbbbbbb','rrrrrrrrr','yyyyyyyyy']]
        self.solution = ['y2']
        self.colors = ['w', 'g', 'o', 'b', 'r', 'y']
        self.msgs = ['White Side', 'Green Side', 'Orange Side', 'Blue Side', 'Red Side', 'Yellow Side']

        """self.white = self.cube[0]
        self.green = self.cube[1]
        self.orange = self.cube[2]
        self.blue = self.cube[3]
        self.red = self.cube[4]
        self.yellow = self.cube[5]"""

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
        write(self.cube)
        pocket = [self.cube[self.yellow][self.corner_ur], self.cube[self.yellow][self.edge_r], self.cube[self.yellow][self.corner_dr]]

        self.cube[self.yellow][self.corner_ur]=self.cube[self.green][self.corner_ur]
        self.cube[self.yellow][self.corner_ur] = self.cube[self.green][self.edge_r]
        self.cube[self.yellow][self.corner_ur] = self.cube[self.green][self.corner_dr]

        self.cube[self.green][self.corner_ur] = self.cube[self.white][self.corner_ur]
        self.cube[self.green][self.corner_ur] = self.cube[self.white][self.edge_r]
        self.cube[self.green][self.corner_ur] = self.cube[self.white][self.corner_dr]

        self.cube[self.white][self.corner_ur] = self.cube[self.blue][self.corner_ur]
        self.cube[self.white][self.corner_ur] = self.cube[self.blue][self.edge_r]
        self.cube[self.white][self.corner_ur] = self.cube[self.blue][self.corner_dr]

        self.cube[self.blue][self.corner_ur] = pocket[0]
        self.cube[self.blue][self.corner_ur] = pocket[1]
        self.cube[self.blue][self.corner_ur] = pocket[2]

        write(self.cube)


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
                    break
            cube_scan.append(ans)
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
        #self.update()
        return 'OK'


    """def update(self):
        self.white = self.cube[0]
        self.green = self.cube[1]
        self.orange = self.cube[2]
        self.blue = self.cube[3]
        self.red = self.cube[4]
        self.yellow = self.cube[5]"""

    def solve(self):
        self.r()


def write(msg):
    print(msg)