class Cube:
    def __init__(self):
        self.solved = False
        self.cube = []
        self.solution = []
        self.colors = ['w', 'g', 'o', 'b', 'r', 'y']

    def define(self):
        msgs = ['White Side', 'Green Side', 'Orange Side', 'Blue Side', 'Red Side', 'Yellow Side']
        cube_scan = []
        for i in range(0,6):
            ans = str()
            while len(ans)!=9:
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