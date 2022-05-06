from graph import random_graph
from euler import euler
from hamilton import Hamilton


def main():
    g = random_graph(12, 0.5)
    g.print_matrix()
    # euler(g)
    h = Hamilton(g, False)
    h.ham_cycle()


main()