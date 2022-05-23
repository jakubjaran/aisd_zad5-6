from graph import Graph
from euler import euler
from hamilton import Hamilton


def test():
    print('Input filename: ')
    # filename = input()
    filename = 'file.txt'
    f = open(filename, 'r')
    adjMatrix = []
    for line in f:
        line = line.rstrip("\n")
        line = line.replace(" ", "")
        row = []
        for i in line:
            row.append(int(i))
        adjMatrix.append(row)
    f.close()

    g = Graph(len(adjMatrix))
    g.set_adj_matrix(adjMatrix)
    g.print_matrix()

    h = Hamilton(g.adjMatrix, once=True)
    h.ham_cycle()

    euler(g)


test()