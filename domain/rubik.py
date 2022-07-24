class Cube:
    def __init__(self):
        self.solved = False
        self.cube = [['wwwwwwwww','ggggggggg','ooooooooo','bbbbbbbbb','rrrrrrrrr','yyyyyyyyy']]
        self.solution = []
        self.colors = ['w', 'g', 'o', 'b', 'r', 'y']

        self.white = self.colors[0]
        self.green = self.colors[1]
        self.orange = self.colors[2]
        self.blue = self.colors[3]
        self.red = self.colors[4]
        self.yellow = self.colors[5]

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



    def define(self):
        # data is defined in accordance with self.colors
        write("Put the cube's white side up and green side at the front.")
        msgs = ['White Side', 'Green Side', 'Orange Side', 'Blue Side', 'Red Side', 'Yellow Side (Green at the back)']
        cube_scan = []
        for i in range(0,6):
            while True:
                write(msgs[i]+': ')
                ans = input()
                if len(ans)!=9:
                    write('Please, enter 9 cells of the '+msgs[i]+'.')
                elif not(self.right_letters(ans)):
                    write('Please, enter only '+str(self.colors)+' letters without spaces, other letters are not allowed.')
                else:
                    break
            cube_scan.append(ans)

    def right_letters(self, side):
        for i in range(0,9):
            if side[i] in self.colors:
                continue
            else:
                return False
        return True


    def check(self):
        pass

def write(msg):
    print(msg)