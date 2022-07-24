from src.main.python.domain import rubik

cube = rubik.Cube()
#while True:
#    if cube.define():
#        cube.solve()
# cube.cube = [['w','w','g','w','w','g','w','w','g'],['g','g','y','g','g','y','g','g','y'],['o','o','o','o','o','o','o','o','o'],['w','b','b','w','b','b','w','b','b'],['r','r','r','r','r','r','r','r','r'],['y','y','b','y','y','b','y','y','b']]
#"""cube.cube = [
#             ['y','y','y','g','w','g','g','g','g'],
#            ['o','o','o','o','g','o','o','o','o'],
#            ['g','w','w','g','o','w','g','w','w'],
#            ['r','r','r','r','b','r','r','r','r'],
#            ['y','y','b','y','r','b','y','y','b'],
#             ['b','b','b','b','y','b','w','w','w']
#         ]"""
cube.solve()