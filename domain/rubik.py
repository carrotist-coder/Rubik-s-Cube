class Cube:
    def __init__(self):
        self.solved = False
        self.cube = []
        self.solution = []

    def define(self):
        msgs = ['White Side', 'Green Side', 'Orange Side', 'Blue Side', 'Red Side', 'Yellow Side']
        cube_scan = []
        for i in range(0,5):
            ans = str()
            while len(ans)!=9:
                write(msgs[i]+': ')
                ans = input()
                if len(ans)!=9:
                    write('Please, enter 9 cells of the '+msgs[i]+'.')
                else:
                    break
            cube_scan.append(ans)


    def check(self):
        pass

class Const:
    def __init__(self):
        self.colors = ['w','g','o','b','r','y']

def write(msg):
    print(msg)