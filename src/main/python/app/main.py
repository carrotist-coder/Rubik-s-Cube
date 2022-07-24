from src.main.python.domain import rubik

cube = rubik.Cube()
#while True:
#    if cube.define():
#        cube.solve()
cube.cube = [
            ['w','w','y','w','w','y','w','w','y'],
            ['g','g','b','g','g','b','o','o','o'],
            ['o','o','o','o','o','o','g','b','b'],
            ['g','b','b','g','b','b','r','r','r'],
            ['r','r','r','r','r','r','g','g','b'],
            ['y','y','y','y','y','y','w','w','w']]
cube.solve()