from domain import rubik

cube = rubik.Cube()
while True:
    if cube.define():
        cube.solve()
