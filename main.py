import time
import pandas

from graph import random_graph
from euler import euler
from hamilton import Hamilton
from graphs import graphs


def test_graph(size, density):
    g = random_graph(size, density)
    # g.print_matrix()
    t1_ham = time.time()
    h = Hamilton(g, once=True)
    has_cycle = h.ham_cycle()
    t2_ham = time.time()
    if has_cycle == False:
        print('Graph without Hamiltonian Cycle')
        return 0, 0
    t1_eul = time.time()
    euler(g)
    t2_eul = time.time()
    return t2_ham - t1_ham, t2_eul - t1_eul


def test(size, density):
    ham, eul = test_graph(size, density)
    while ham == 0 and eul == 0:
        ham, eul = test_graph(size, density)
    return ham, eul


# def main():

#     print('First graph size: ')
#     size = int(input())
#     print('Size step: ')
#     step = int(input())
#     print('Density:')
#     density = float(input())
#     print(density)
#     writer = pandas.ExcelWriter(f'out/zad5_{size}__{step}_{density}.xlsx',
#                                 engine='openpyxl')

#     SIZE = []
#     HAM = []
#     EUL = []
#     for _ in range(0, 15):
#         SIZE.append(size)
#         ham, eul = test(size, density)
#         HAM.append(ham)
#         EUL.append(eul)
#         size += step
#     data = pandas.DataFrame({
#         'Graph Size': SIZE,
#         'Hamilton': HAM,
#         'Euler': EUL
#     })

#     data.to_excel(writer, sheet_name=f'{density}', index=False)

#     writer.save()


def main():
    # print('Graph size: ')
    # size = int(input())
    # print('Density:')
    # density = float(input())
    size = 15
    density = 0.5

    g = random_graph(size, density)
    t1 = time.time()
    h = Hamilton(g.adjMatrix, False)
    h.ham_cycle()
    t2 = time.time()
    print(t2 - t1)
    # t1 = time.time()
    # euler(g)
    # t2 = time.time()
    # print(t2 - t1)


# def main():
#     for graph in graphs:
#         t1 = time.time()
#         h = Hamilton(graph, once=True)
#         h.ham_cycle()
#         t2 = time.time()
#         print(t2 - t1)

main()
