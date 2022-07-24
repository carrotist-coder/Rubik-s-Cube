from src.main.python.domain import rubik

cube = rubik.Cube()
#while True:
#    if cube.define():
#        cube.solve()
# cube.cube = [['w','w','g','w','w','g','w','w','g'],['g','g','y','g','g','y','g','g','y'],['o','o','o','o','o','o','o','o','o'],['w','b','b','w','b','b','w','b','b'],['r','r','r','r','r','r','r','r','r'],['y','y','b','y','y','b','y','y','b']]
cube.solve()