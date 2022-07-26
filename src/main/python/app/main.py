from src.main.python.domain import rubik

cube = rubik.Cube()
#while True:
#    if cube.define():
#        cube.solve()
"""cube.cube = [
            ['o','o','o','b','w','o','r','y','y'],
            ['w','r','o','y','g','w','g','o','r'],
            ['w','o','b','w','o','g','g','b','y'],
            ['b','y','g','b','b','g','o','r','r'],
            ['b','w','w','b','r','r','b','g','y'],
            ['r','g','y','y','y','r','w','w','g']]"""
cube.solve()