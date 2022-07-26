from src.main.python.domain import rubik

def cfop():
    cross()

def cross():
    for i in range(1,5):
        rubik.write('Hi there')
        cross_get()

def cross_get():
    edges = [rubik.Cube.cube[rubik.white][rubik.edge]]
